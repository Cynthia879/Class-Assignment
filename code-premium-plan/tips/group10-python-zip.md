# `zip`：并行遍历两个（或多个）列表

> **预置稿**：第 10 组认领后请据实修改组名、作者。

- **小组**：第 10 组
- **作者**：（待填写）
- **环境**：Python 3.x

## 适用场景

有两列数据：`names` 与 `scores`，要逐行组成「姓名—分数」；或要对齐处理两个等长序列。不必维护同一个 `i` 去下标两个数组，用 `zip` 一次迭代成对元素。

## 核心思路

`zip(a, b, ...)` 在最短输入耗尽时停止。Python 3 中 `zip` 返回迭代器，省内存。若必须等长且要多出来的报错，可用 `zip(..., strict=True)`（3.10+）。

## 最小示例

```python
names = ["Ann", "Bob", "Chen"]
scores = [92, 88, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 严格等长（3.10+）
list(zip(names, scores, strict=True))
```

## 常见坑

- 两个列表长度不同时，`zip` 静默截断较短一方，易出隐蔽 bug；长列表用 `strict=True` 或先断言长度。  
- `zip(*matrix)` 常用于矩阵转置，但要保证内层序列长度一致。  
- 需要索引时可用 `enumerate(zip(a, b))`，或 `zip(count(), xs)`。

## 延伸阅读（可选）

- [zip — Python 文档](https://docs.python.org/3/library/functions.html#zip)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
