# Bash `set -euo pipefail`：让脚本早失败、少翻车

> **预置稿**：第 05 组认领后请据实修改组名、作者。

- **小组**：第 05 组
- **作者**：（待填写）
- **环境**：Bash 4+ / Linux、macOS、Git Bash

## 适用场景

写部署或批处理脚本时，某条命令失败了但脚本继续跑，后面用空变量覆盖文件，造成更难排查的烂摊子。在脚本开头打开「严格模式」，让错误尽早暴露。

## 核心思路

- `set -e`：任一命令返回非零则退出（少数复合命令例外）。  
- `set -u`：使用未定义变量时报错退出。  
- `set -o pipefail`：管道中任一环节失败，整条管道返回非零。

## 最小示例

```bash
#!/usr/bin/env bash
set -euo pipefail

NAME="${1:?请传入名称参数}"
echo "hello, $NAME"
missing_command || true   # 确需忽略错误时显式处理
```

第三行若未传参会直接失败并提示；误写 `$NAM` 会因 `-u` 立刻退出。

## 常见坑

- 有些命令「正常」时也返回非零（如 `grep` 未匹配），需 `grep ... || true` 或判断 `$?`。  
- 子 shell 内 `set` 不继承到父 shell，每个脚本文件都要写。  
- `zsh` 语法与 bash 略有不同，本技巧针对 bash shebang。

## 延伸阅读（可选）

- [Bash 手册 set 内建命令](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
