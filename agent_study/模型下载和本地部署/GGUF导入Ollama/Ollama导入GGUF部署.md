# GGUF 下载 → Ollama 导入部署（以 Xiaomi-OCR-0 为例）

> 适用场景：模型不在 Ollama 官方库，但魔塔/抱抱脸上有社区转换的 GGUF，需要自己下载并导入 Ollama。
> 本文所有命令和结果均在本机（Windows + Ollama 0.40.13 + AMD 780M）实测通过。

---

## 0. 原理

Ollama 的模型目录（本例 `D:\dev_soft\ollma\models`）是**内容寻址仓库**：`blobs/` 存权重层，`manifests/` 存模型定义。

- 直接把 `.gguf` 拷进去，`ollama list` **不会识别**
- 必须让 Ollama 自己写入：`ollama pull`（registry 包）或 `ollama create`（本地 GGUF 导入）
- 视觉模型需要两个文件：**语言模型 GGUF + mmproj 视觉投影器**，Modelfile 里写两个 `FROM`
- `ollama create` 会把源文件复制进 blobs，**源目录放哪都行**，不需要放进 models 目录
- 导入后单个模型约占源文件同等大小（本例源文件 736MB，导入后 736MB）

---

## 1. 下载 GGUF

魔塔仓库：`prithivMLmods/Xiaomi-OCR-0-GGUF`
需要的文件：

| 文件 | 大小 | 作用 |
| ---- | ---- | ---- |
| `Xiaomi-OCR-0.Q4_K_M.gguf` | 529 MB | 语言模型主权重（Q4_K_M） |
| `Xiaomi-OCR-0.mmproj-bf16.gguf` | 207 MB | 视觉投影器，缺了图片输入会被忽略 |

### 方式 A：直链下载（不依赖 Python 环境，推荐）

```powershell
mkdir D:\dev_soft\models\Xiaomi-OCR-0

curl.exe -L --retry 4 -o "D:\dev_soft\models\Xiaomi-OCR-0\Xiaomi-OCR-0.Q4_K_M.gguf" `
  "https://modelscope.cn/api/v1/models/prithivMLmods/Xiaomi-OCR-0-GGUF/repo?Revision=master&FilePath=Xiaomi-OCR-0.Q4_K_M.gguf"

curl.exe -L --retry 4 -o "D:\dev_soft\models\Xiaomi-OCR-0\Xiaomi-OCR-0.mmproj-bf16.gguf" `
  "https://modelscope.cn/api/v1/models/prithivMLmods/Xiaomi-OCR-0-GGUF/repo?Revision=master&FilePath=Xiaomi-OCR-0.mmproj-bf16.gguf"
```

### 方式 B：modelscope CLI

```powershell
uv tool run --from modelscope modelscope download `
  --model prithivMLmods/Xiaomi-OCR-0-GGUF `
  --include "Xiaomi-OCR-0.Q4_K_M.gguf" "Xiaomi-OCR-0.mmproj-bf16.gguf" `
  --local_dir D:\dev_soft\models\Xiaomi-OCR-0
```

> 若提示 `uvx` 不是命令，用 `uv tool run` 代替 `uvx`。

---

## 2. 写 Modelfile

路径用正斜杠 `/` 避免转义问题：

```dockerfile
FROM D:/dev_soft/models/Xiaomi-OCR-0/Xiaomi-OCR-0.Q4_K_M.gguf
FROM D:/dev_soft/models/Xiaomi-OCR-0/Xiaomi-OCR-0.mmproj-bf16.gguf

PARAMETER temperature 0
PARAMETER top_p 0.8
PARAMETER num_ctx 8192
PARAMETER num_predict 4096
```

参数说明：

| 参数 | 作用 |
| ---- | ---- |
| `temperature 0` | OCR 任务要确定性输出 |
| `num_ctx 8192` | 上下文长度；大页面/长文档可调到 16384、32768 |
| `num_predict 4096` | 最大输出 token，整页 OCR 输出很长，别用默认值 |

---

## 3. 导入 Ollama

```powershell
ollama create xiaomi-ocr:q4 -f "D:\dev_soft\models\Xiaomi-OCR-0\Modelfile"
```

成功输出：

```text
gathering model components
parsing GGUF
using existing layer sha256:1e497ff06b91a3d822c543066df3e9ef69c62c5423be09d739dfa1db55630d3a
using existing layer sha256:634d6bc95781ebf4a3f06570a59859fa5082d488db540fd474bc6b4061aec90e
using existing layer sha256:7d0738d45b8ebae012d64e8cad877050693f9751d77b142789000772f7df4fc6
writing manifest
success
```

---

## 4. 验证

```powershell
ollama list          # 应出现 xiaomi-ocr:q4  736 MB
ollama show xiaomi-ocr:q4
```

本机实际输出：

```text
Model
  architecture        qwen35
  parameters          752.39M
  context length      262144
  embedding length    1024
  quantization        Q4_K_M
  template source     gguf_chat_template

Capabilities
  tools
  thinking
  completion
  vision          ← 关键：说明投影器已生效

Projector
  architecture        clip
  parameters          100.59M
  embedding length    768
  dimensions          1024

Parameters
  num_ctx        8192
  temperature    0
  top_p          0.8
```

`Capabilities` 里出现 `vision`、`Projector` 段有内容，才算视觉模型导入成功。

---

## 5. 调用

### 命令行

```powershell
ollama run xiaomi-ocr:q4 "Extract the text in the image. D:\pics\demo.png"
```

提示词 + 图片路径写在同一个字符串里，用空格分开。

### Python（见同目录 `ocr_ollama.py`）

```powershell
uv run python ocr_ollama.py "D:\pics\demo.png"
uv run python ocr_ollama.py "D:\pics\demo.png" --task document
uv run python ocr_ollama.py "D:\pics\demo.png" --stream    # 流式逐块输出
```

脚本通过 `POST http://localhost:11434/api/chat`，把图片 base64 放进 `messages[0].images`；默认非流式，`--stream` 时逐块打印。输出结束后会打印摘要（字符数 / 行数 / 表格行 / 公式数 / 开头预览），并写入同目录的 `ollama_sessions.jsonl`，用 `ollama_stats.py --report` 汇总所有 OCR / 聊天会话。

---

## 6. 任务提示词（官方模型卡）

| 任务 | 提示词 |
| ---- | ------ |
| 整页解析 | `Extract all information from the main body of the document image and represent it in markdown format, ignoring headers and footers. Tables should be expressed in OTSL format, formulas in the document should be represented using LATEX format, and the parsing should be organized according to the reading order.` |
| 纯文本区域 | `Extract the text in the image.` |
| 表格 | `Parse the table in the image into OTSL.` |
| 公式 | `Identify the formula in the image and represent it using LATEX format.` |
| 关键信息抽取 | `Extract key information in the image` + JSON schema |

---

## 7. 本机实测记录

| 图片 | 提示词 | 结果 |
| ---- | ------ | ---- |
| `example_pics/dense-equations.jpg` | 整页解析 | 正常输出整页 Markdown，公式为 LaTeX，约 30 秒 |
| `example_pics/qianziwen.jpeg`（书法竖排） | 纯文本 | 只输出前几行即结束（`done_reason=stop`，24 tokens），属于图片预处理/排版问题，非部署失败 |

结论：**常规文档解析可用**；书法竖排、超小字等场景要追平官方分数，需改用官方 Transformers 脚本（自带预处理和提示词）。

---

## 8. 常见坑

| 现象 | 原因 / 处理 |
| ---- | ----------- |
| 图片不生效，只输出文字 | 漏了 mmproj 投影器，或 Modelfile 少了第二个 `FROM` |
| `ollama list` 看不到模型 | 直接把 gguf 拷进了 models 目录，没用 `ollama create` |
| 输出被截断 | `num_ctx` 太小或 `num_predict` 太小，调大后重新 create |
| `ollama create` 报架构不支持 | 当前 Ollama 内置 llama.cpp 不认识该架构，升级 Ollama |
| 输出开头有 `<｜end▁of▁thinking｜>` | 模型默认思考模式，OCR 可忽略，或用模板/提示词关闭 |
| `uvx` 不是命令 | 用 `uv tool run --from ...` |
| `uv add` 报 `pypi.douban.com` 错误 | 该镜像已停服，从 `uv.toml` 的 `extra-index-url` 移除 |
| 下载很慢 | 用魔塔直链（国内速度约 10MB/s），别走 ollama.com |

---

## 9. 清理

```powershell
ollama rm xiaomi-ocr:q4        # 只删 Ollama 里的模型
Remove-Item -Recurse D:\dev_soft\models\Xiaomi-OCR-0   # 再删源文件
```
