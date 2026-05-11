# `git stash`：临时切分支不伤半成品

> **预置稿**：第 02 组认领后请据实修改组名、作者与案例。

- **小组**：第 02 组
- **作者**：（待填写）
- **环境**：Git 2.x / 任意系统

## 适用场景

正在 `feature` 分支改到一半，突然需要切到 `main` 拉 hotfix 或帮同学看另一个分支；工作区有未提交修改，直接 `checkout` 可能被拒绝或把改动带过去。此时先把当前修改**压栈**再起跳。

## 核心思路

`git stash push -m "说明"` 把工作区（默认含已跟踪文件的修改）存成一条 stash 记录，工作区恢复干净；处理完别的事后再 `git stash pop` 或 `git stash apply` 取回。带未跟踪文件时常用 `git stash -u`。

## 最小示例

```bash
git status                    # 确认有未提交修改
git stash push -m "WIP 登录表单"
git switch main
git pull
# ... 处理 main 上的事 ...
git switch feature
git stash list
git stash pop                 # 取回并删除该条 stash；若想保留记录用 apply
```

## 常见坑

- `stash pop` 若产生冲突，stash 可能仍保留，需手动解决后 `git stash drop`。  
- 不要把二进制大文件长期堆在 stash 里，容易忘。  
- 与 `commit` 不同，stash 默认不进远程；换电脑后别人看不到你的 stash。

## 延伸阅读（可选）

- [Git Stash 文档](https://git-scm.com/docs/git-stash)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
