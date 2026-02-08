
# 如何把项目的三方依赖包导出到一个requirements.txt文件？

## 方法一：pip freeze > requirements.txt

## 方法二：pipreqs库
1. 安装pipreqs库
pip install pipreqs
2. 生成requirements.txt文件
3. 命令  
```
pipreqs 生成requirements文件的路径 --encoding=utf8
```
>如： 
```pipreqs ./ --encoding=utf8```   
参数解释：  
-encoding=utf8 ：为使用utf8编码  
–force ：强制执行，当 生成目录下的requirements.txt存在时覆盖  
-./: 在哪个文件生成requirements.txt 文件


