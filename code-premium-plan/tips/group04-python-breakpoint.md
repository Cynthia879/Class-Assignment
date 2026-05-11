# Python `breakpoint()`：零依赖打断点

> **预置稿**：第 04 组认领后请据实修改组名、作者。

- **小组**：第 04 组
- **作者**：（待填写）
- **环境**：Python 3.7+

## 适用场景

排查循环里某次迭代的变量值，临时又不想改 IDE 配置。在怀疑行插入一行 `breakpoint()`，解释器会进入 pdb（或环境变量 `PYTHONBREAKPOINT` 指定的调试器）。

## 核心思路

`breakpoint()` 是内置函数，等价于可配置的「在此暂停」。默认进入 `pdb.post_mortem` 风格交互：可 `p 变量名` 打印、`n` 下一行、`c` 继续。提交代码前记得删掉或加条件，避免生产环境停住。

## 最小示例

```python
def total(items):
    s = 0
    for i, x in enumerate(items):
        breakpoint()  # 调试完删除
        s += x
    return s

print(total([1, 2, 3]))
```

运行后在第一次循环进入调试器，检查 `i`、`x`、`s`。

## 常见坑

- 忘记删除 `breakpoint()` 会导致脚本在服务器上挂起等人输入。  
- 在只读或无 TTY 环境（某些 CI）中会失败或阻塞，应改用日志或条件断点。  
- 想用 ipdb：可 `export PYTHONBREAKPOINT=ipdb.set_trace`。

## 延伸阅读（可选）

- [breakpoint() — Python 文档](https://docs.python.org/3/library/functions.html#breakpoint)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
