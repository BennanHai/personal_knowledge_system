> 这是自己学习logging的笔记及学习资料

## 参考文档及书籍
- 官方中文教程文档：[Python官方教程](https://docs.python.org/zh-cn/3.13/tutorial/index.html)
- 日志指南：[Python 日志指南](https://docs.python.org/zh-cn/3.13/howto/logging.html)
- 日志标准库：[Python 的日志记录工具](https://docs.python.org/zh-cn/3.13/library/logging.html)
- 知乎文章：[Python 日志记录的进阶之路：从 logging 到 loguru](https://zhuanlan.zhihu.com/p/26410775296)
- [Python logging 模块详解](https://mp.weixin.qq.com/s?__biz=MzkxNDI3NjcwMw==&mid=2247493338&idx=1&sn=9f12511a569a6ac735cb53784f862898&chksm=c1724eeaf605c7fc552582d57d2b79dc053baa6f1cbccdb67987d87649ab29171883c389c855&scene=21#wechat_redirect)


## 日志执行流程
- [流程图](https://docs.python.org/zh-cn/3.13/howto/logging.html#logging-flow)
- **流程描述**
1. 判断日志的等级是否大于 Logger 对象的等级，如果大于，则往下执行，否则，流程结束。

2. 产生日志：第一步，判断是否有异常，如果有，则添加异常信息。第二步，处理日志记录方法(如 debug，info 等)中的占位符，即一般的字符串格式化处理。

3. 使用注册到 Logger 对象中的 Filters 进行过滤。如果有多个过滤器，则依次过滤；只要有一个过滤器返回假，则过滤结束，且该日志信息将丢弃，不再处理，而处理流程也至此结束。否则，处理流程往下执行。

4. 在当前 Logger 对象中查找 Handlers，如果找不到任何 Handler，则往上到该 Logger 对象的父 Logger 中查找；如果找到一个或多个 Handler，则依次用 Handler 来处理日志信息。但在每个 Handler 处理日志信息过程中，会首先判断日志信息的等级是否大于该 Handler 的等级，如果大于，则往下执行(由 Logger 对象进入 Handler 对象中)，否则，处理流程结束。

5. 执行 Handler 对象中的 filter 方法，该方法会依次执行注册到该 Handler 对象中的 Filter。如果有一个 Filter 判断该日志信息为假，则此后的所有 Filter 都不再执行，而直接将该日志信息丢弃，处理流程结束。

6. 使用 Formatter 类格式化最终的输出结果。注：Formatter 同上述第 2 步的字符串格式化不同，它会添加额外的信息，比如日志产生的时间，产生日志的源代码所在的源文件的路径等等。

7. 真正地输出日志信息(到网络，文件，终端，邮件等)。至于输出到哪个目的地，由 Handler 的种类来决定。

