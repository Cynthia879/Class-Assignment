# 班级 GitHub 论文协作库与代码邮箱计划

本仓库面向班级协作，包含两项内容：

1. **论文协作**：LaTeX 中文论文模板、查重相关说明与本地辅助工具。  
2. **代码邮箱计划**：分组认领任务，**每个小组**向全班提交 **1 篇** 学习过程中掌握的编程技巧（Markdown，见 `code-email-plan/`）。

## 1. 论文协作

| 内容 | 路径 |
|------|------|
| LaTeX 论文模板（中文） | [`latex-template/`](latex-template/) |
| 查重说明与辅助脚本 | [`tools/plagiarism/`](tools/plagiarism/) |

### 仓库地址

- **GitHub**：https://github.com/Cynthia879/Class-Assignment

### 克隆与推送（协作者）

```bash
git clone https://github.com/Cynthia879/Class-Assignment.git
cd Class-Assignment
# 修改后
git add .
git commit -m "描述你的修改"
git push origin main
```

首次在本机关联远程（若从零初始化）：

```bash
git remote add origin https://github.com/Cynthia879/Class-Assignment.git
git branch -M main
git push -u origin main
```

### 协作建议

1. 在仓库 **Settings → Collaborators** 中添加课程同学为协作者（或使用 Organization **Team**）。  
2. 可为 `main` 开启 **Branch protection**（通过 Pull Request 合并），便于论文与技巧稿版本留痕。

## 2. 代码邮箱计划

| 内容 | 路径 |
|------|------|
| 任务说明与规则 | [`code-email-plan/README.md`](code-email-plan/README.md) |
| 小组认领表 | [`code-email-plan/GROUPS.md`](code-email-plan/GROUPS.md) |
| 各组技巧提交目录 | [`code-email-plan/tips/`](code-email-plan/tips/) |

**任务要求**：每个小组贡献 **1 条** 在课程或项目中**真实掌握**的编程技巧，按 [`tips/_TEMPLATE.md`](code-email-plan/tips/_TEMPLATE.md) 写成 Markdown，放入 `code-email-plan/tips/`，通过 Pull Request 合并，或由仓库管理员按课程约定代为合并。

---

问题与改进建议在仓库 **Issues** 中提出，或通过课程群沟通。
