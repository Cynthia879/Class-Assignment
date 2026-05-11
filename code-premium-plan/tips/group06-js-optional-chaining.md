# JavaScript 可选链 `?.`：少写一层层判空

> **预置稿**：第 06 组认领后请据实修改组名、作者。

- **小组**：第 06 组
- **作者**：（待填写）
- **环境**：现代浏览器、Node 14+（ES2020）

## 适用场景

从接口 JSON 取深层字段，中间某层可能是 `null`。以前要写 `a && a.b && a.b.c`，冗长且易漏。可选链在路径上任意一环为 `null`/`undefined` 时短路为 `undefined`，不抛异常。

## 核心思路

`obj?.prop`、`obj?.[expr]`、`func?.()` 三种形式。与空值合并 `??` 搭配，可给默认值：`const city = user?.address?.city ?? "未知"`。

## 最小示例

```javascript
const user = { profile: { name: "Lee" } };

console.log(user?.profile?.name);        // Lee
console.log(user?.settings?.theme);    // undefined，不报错

const first = arr?.[0]?.toUpperCase?.();
```

最后一行在 `arr` 为空或首元素无 `toUpperCase` 时得到 `undefined`。

## 常见坑

- `?.` 只防 `null`/`undefined`，不防「属性存在但值为 `0`/`""`」被当成假值；需要时用 `??`。  
- 过深的可选链往往说明数据结构不稳定，接口层可做校验与归一化。  
- 旧构建目标需确认 Babel/TS 配置是否降级转译。

## 延伸阅读（可选）

- [MDN：可选链](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

---

**诚信声明**：本技巧为小组原创整理；引用他人内容已在上文或链接中注明。
