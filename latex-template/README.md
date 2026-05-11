# 班级论文 LaTeX 模板

## 环境要求

- 完整 TeX 发行版：**TeX Live**（跨平台）或 **MiKTeX**（Windows）。
- 本模板使用 **XeLaTeX** 以正确排版中文。

## 编译

在 `latex-template` 目录下：

```bash
xelatex -output-directory=build main.tex
bibtex build/main
xelatex -output-directory=build main.tex
xelatex -output-directory=build main.tex
```

若不用参考文献，可只执行两次 `xelatex`。

## 与协作者协作

- 每人可在分支上撰写章节，通过 **Pull Request** 合并到 `main`。
- 大图、数据集勿提交进 Git：用 `.gitignore` 忽略，在 README 中写网盘或学校存储链接。
