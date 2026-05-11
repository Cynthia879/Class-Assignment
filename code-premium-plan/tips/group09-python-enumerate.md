# `enumerate`：同时需要下标和元素时别手写 `range(len)`

> **预置稿**：第 09 组认领后请据实修改组名、作者。

- **小组**：第 09 组
- **作者**：（待填写）
- **环境**：Python 3.x

## 适用场景

遍历列表时要打印「第几条」、要在原列表旁维护索引、或要把索引当行号写入 CSV。用 `for i in range(len(xs))` 再 `xs[i]` 可读性差且容易越界感弱。`enumerate` 把索引和元素成对给出，更 Pythonic。

## 核心思路

`enumerate(iterable, start=0)` 产生 `(索引, 元素)`。需要 1-based 行号时设 `start=1`。

## 最小示例

```python
lines = ["a", "b", "c"]

for i, line in enumerate(lines, start=1):
    print(f"{i:02d}: {line}")

# 需要索引改原列表时
nums = [1, 2, 3]
for i, v in enumerate(nums):
    nums[i] = v * 10
```

## 常见坑

- 在循环里对正在遍历的列表做**结构性**修改（插入/删元素）仍可能乱序，与 `enumerate` 无关但常见踩坑。  
- 对极大生成器 `enumerate` 仍是惰性，但若要先 `list()` 化再枚举会占内存。  
- 只要值不要下标时别强行用 `enumerate`，直接 `for x in xs` 更简单。

## 延伸阅读（可选）

- [enumerate — Python 文档](https://docs.python.org/3/library/functions.html#enumerate)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
