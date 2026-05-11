# 用 `pathlib` 跨平台拼路径

- **小组**：第 00 组 — 示例（提交前请删除本文件或改为真实组号）
- **作者**：示例
- **环境**：Python 3.10+ / 任意系统

## 适用场景

需要读写文件、拼接目录与文件名时，避免手写 `/` 与 `\` 导致在 Windows 与 Linux 上行为不一致。

## 核心思路

使用标准库 `pathlib.Path` 表示路径，用 `/` 运算符拼接；`Path` 在各自系统上显示为合法分隔形式。

## 最小示例

```python
from pathlib import Path

root = Path("data") / "raw"
file = root / "input.csv"
print(file.as_posix())   # 便于日志里统一用正斜杠
print(file.resolve())    # 绝对路径
```

## 常见坑

- `Path("a") + "b"` 无效，必须用 `/` 拼接另一路径或字符串段。
- 需要字符串给旧 API 时，用 `str(path)`，但优先把下游也改成接受 `Path`。

## 延伸阅读（可选）

- [pathlib 官方文档](https://docs.python.org/3/library/pathlib.html)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
