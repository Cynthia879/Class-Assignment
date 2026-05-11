# 班级论文协作与代码邮箱计划

本仓库用于班长提出的两项班级事务：**论文协作（含 LaTeX 模板与查重指引）**与**「代码邮箱计划」分组任务**。

## 1. 论文协作

| 内容 | 路径 |
|------|------|
| LaTeX 论文模板（中文） | [`latex-template/`](latex-template/) |
| 查重说明与辅助脚本 | [`tools/plagiarism/`](tools/plagiarism/) |

### 发布到 GitHub 的步骤（班长或仓库管理员）

1. 在 GitHub 新建 **Organization** 或 **个人仓库**，名称建议：`ClassName-Paper-Collab`（按班级实际命名）。
2. 本地初始化并推送（在仓库根目录执行）：

```bash
git init
git add .
git commit -m "Initial: LaTeX template, plagiarism tools, code email plan"
git branch -M main
git remote add origin https://github.com/<组织或用户名>/<仓库名>.git
git push -u origin main
```

3. 在仓库 **Settings → Collaborators** 中添加全班同学为协作者，或全班加入同一 Organization 后设为 **Team** 访问。
4. 建议开启 **Branch protection**：`main` 分支需 Pull Request 合并，便于论文版本留痕。

## 2. 代码邮箱计划

| 内容 | 路径 |
|------|------|
| 任务说明与规则 | [`code-email-plan/README.md`](code-email-plan/README.md) |
| 小组认领表 | [`code-email-plan/GROUPS.md`](code-email-plan/GROUPS.md) |
| 各组技巧提交目录 | [`code-email-plan/tips/`](code-email-plan/tips/) |

**要求（班长口径）**：每个小组为班级贡献 **1 条** 本组在课程/项目中**真实学到**的编程技巧，按模板写成 Markdown，放入 `code-email-plan/tips/` 并由组长发 PR 或在课上约定的方式合并。

---

如有问题，在仓库 Issues 中 `@班长` 或课程群沟通。
