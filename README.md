# 班级论文协作与代码邮箱计划

本仓库用于班长提出的两项班级事务：**论文协作（含 LaTeX 模板与查重指引）**与**「代码邮箱计划」分组任务**。

## 1. 论文协作

| 内容 | 路径 |
|------|------|
| LaTeX 论文模板（中文） | [`latex-template/`](latex-template/) |
| 查重说明与辅助脚本 | [`tools/plagiarism/`](tools/plagiarism/) |

### 班级仓库地址

- **GitHub**：https://github.com/Cynthia879/Class-Assignment

### 推送到本仓库（本地已有内容时）

在仓库根目录 `d:\biyerenwu` 执行（若尚未添加远程）：

```bash
git remote add origin https://github.com/Cynthia879/Class-Assignment.git
git branch -M main
git push -u origin main
```

若已存在名为 `origin` 的远程，可改为：

```bash
git remote set-url origin https://github.com/Cynthia879/Class-Assignment.git
git branch -M main
git push -u origin main
```

### 协作设置（班长）

1. 在仓库 **Settings → Collaborators** 中添加全班同学为协作者（或 Organization **Team**）。
2. 建议为 `main` 开启 **Branch protection**（需 Pull Request 合并），便于论文与技巧稿留痕。

## 2. 代码邮箱计划

| 内容 | 路径 |
|------|------|
| 任务说明与规则 | [`code-email-plan/README.md`](code-email-plan/README.md) |
| 小组认领表 | [`code-email-plan/GROUPS.md`](code-email-plan/GROUPS.md) |
| 各组技巧提交目录 | [`code-email-plan/tips/`](code-email-plan/tips/) |

**要求（班长口径）**：每个小组为班级贡献 **1 条** 本组在课程/项目中**真实学到**的编程技巧，按模板写成 Markdown，放入 `code-email-plan/tips/` 并由组长发 PR 或在课上约定的方式合并。

---

如有问题，在仓库 Issues 中 `@班长` 或课程群沟通。
