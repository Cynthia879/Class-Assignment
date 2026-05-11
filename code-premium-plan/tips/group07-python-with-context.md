# Python `with`：自动关文件、释放锁

> **预置稿**：第 07 组认领后请据实修改组名、作者。

- **小组**：第 07 组
- **作者**：（待填写）
- **环境**：Python 3.9+（示例无版本硬依赖）

## 适用场景

读写完文件后忘记 `close()`，在异常路径上尤其容易泄漏句柄；多线程里拿到锁后若中间抛错，可能永远不 `release()`。把资源放进 `with`，退出块时由上下文管理器负责清理。

## 核心思路

实现了 `__enter__` / `__exit__` 的对象可作为上下文管理器。`open()` 返回的文件对象即如此：离开 `with` 块（含异常）时会关闭文件。标准库 `threading.Lock` 同样支持 `with lock:`。

## 最小示例

```python
from pathlib import Path

path = Path("note.txt")
with path.open("w", encoding="utf-8") as f:
    f.write("hello\n")
    # 若此处异常，文件仍会被关闭

with path.open("r", encoding="utf-8") as f:
    content = f.read()
```

## 常见坑

- 在 `with` 外继续使用已关闭的文件句柄会报错。  
- 需要同一文件又读又写时，注意分两个 `with` 或合理用 `r+` 模式。  
- 自写上下文管理器时，`__exit__` 里应吞掉或再抛出异常，逻辑要仔细测。

## 延伸阅读（可选）

- [上下文管理器 — Python 文档](https://docs.python.org/3/library/contextlib.html)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
