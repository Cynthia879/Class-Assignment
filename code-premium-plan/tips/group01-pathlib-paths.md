# 用 `pathlib` 跨平台拼路径

> **预置稿**：第 01 组认领后请据实修改组名、作者，并替换/补充为你们真实在项目中用过的案例。

- **小组**：第 01 组
- **作者**：（待填写）
- **环境**：Python 3.10+ / Windows、macOS、Linux 均可

## 适用场景

需要读写数据文件、遍历目录时，若手写 `"data" + "/" + "raw"` 或混用反斜杠与正斜杠，在 Windows 与 Linux 之间拷贝代码容易踩坑。用标准库 `pathlib` 可以把路径当成对象处理，拼接与解析都更稳。

## 核心思路

`Path` 表示文件系统路径；用 `/` 运算符把多段路径接在一起，库会按当前系统使用正确分隔符。需要字符串给旧 API 时用 `str(path)`，但新代码应尽量一路传 `Path`。

## 最小示例

```python
from pathlib import Path

root = Path("data") / "raw"
csv_path = root / "input.csv"
root.mkdir(parents=True, exist_ok=True)
text = csv_path.read_text(encoding="utf-8")
print(csv_path.resolve())
```

先拼出 `data/raw/input.csv`，需要时创建父目录，再按 UTF-8 读入文本；`resolve()` 打印绝对路径便于日志对照。

## 常见坑

- 不能用 `Path("a") + "b"`，必须用 `/` 连接另一 `Path` 或字符串段。  
- Windows 下 `Path` 打印可能带反斜杠，日志里若需统一风格可用 `as_posix()`。  
- 注意区分相对路径与 `resolve()` 后的绝对路径，避免在 CI 与本地路径不一致时误判。

## 延伸阅读（可选）

- [pathlib — 官方文档](https://docs.python.org/3/library/pathlib.html)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
