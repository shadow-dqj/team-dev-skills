---
name: mall4cloud-vue-web-style
version: 0.1.0
description: 基于 Mall4Cloud 四个 Vue 3 Web 仓库的多数约定实施或审查页面、组件、API、Pinia、路由、Element Plus、i18n、样式和测试变更时使用。
user-invocable: true
tags:
  - mall4cloud
  - vue
  - web
  - style
---

# Mall4Cloud Vue Web Style

## 适用范围

用于以下独立仓库：

- `mall4cloud-platform/`
- `mall4cloud-multishop/`
- `mall4cloud-pc/`
- `mall4cloud-slipper/`

先读取目标仓库的 `package.json`、格式配置和相邻业务页面。四个仓库共享 Vue 3 风格，但请求层和路由机制并不完全相同。

## 工作顺序

1. 确认目标端职责和独立 Git 仓库，不在工作区根目录执行 pnpm 或 Git 命令。
2. 查找同仓库、同领域的页面、API、store、路由和 locale 样例。
3. 使用目标仓库已有请求封装和路由机制完成最小变更。
4. 保持异步 loading、提交锁、分页和弹窗生命周期闭合。
5. 依次执行格式检查、lint、最小测试和构建，并按仓库汇报。

## 必须遵循

- 新建或实质重写的 Vue 文件使用 `<script setup>` 和 Composition API；未触及的 Options API 遗留组件保持原状。
- 采用目标仓库 oxfmt 规则：2 空格、LF、单引号、无分号、无尾随逗号；不要套用其他格式器默认值。
- 跨目录模块使用 `@/` 别名，相邻组件可使用相对路径；自动导入配置已有的 API 不做机械显式导入。
- 请求必须经过目标仓库现有 `request`/`http` 封装，不在页面创建 axios 实例，也不重复处理全局业务码。
- Props 使用清晰的对象声明，事件使用 `defineEmits`；弹窗初始化沿用相邻组件的 `defineExpose({ init })` 模式。
- Store 使用 `useXxxStore` 命名并沿用目标仓库现有 Options Store、目录和持久化设置。
- 用户可见新文案使用现有 i18n 命名空间，不硬编码 token、语言头、后端 base URL 或环境地址。
- Element Plus 表单显式维护 model、rules 和 form ref，提交前调用 `validate`。
- 删除、下架等破坏性操作先使用现有确认交互；异步成功、失败路径都必须恢复 loading 或操作锁。
- 新页面/组件样式默认 scoped；覆盖 Element Plus 内部样式使用 `:deep(...)`。
- 新路由严格沿用目标仓库当前机制。

## 仓库差异

- `mall4cloud-platform`、`mall4cloud-multishop`、`mall4cloud-slipper`：领域请求通常放在 `src/api/<domain>/`，通过 `@/utils/request` 导出具名函数。
- `mall4cloud-pc`：大量页面沿用 `src/plugins/http.js` 的 `http`，路由大量由 `import.meta.glob` 生成。不要把三个后台仓库的 API/路由模板机械移入 PC。
- 管理端常用集中基础路由加动态权限路由；PC 使用目录扫描和用户中心子路由。修改前读取对应 router。
- 响应数据形状由目标请求封装决定；先看封装和相邻调用，不从另一个仓库猜测。

## 跟随邻近代码

- 页面组织可沿用搜索区、操作区、表格/内容区、分页和弹窗组件，但不强制改造不适用的展示页面。
- 管理端 API 函数优先使用现有 CRUD 或业务语义命名；页面常通过 `import * as api` 调用。
- 复杂 SCSS 可拆到同目录文件，并优先跟随该目录的 `@use`/`@import` 选择。
- 导入分组在历史代码中不完全统一；只由 oxfmt 处理，不做无价值批量重排。
- 可独立验证的请求参数、权限判断和业务计算提取到 utils/hooks，并补邻近 Vitest。

## 遗留例外勿复制

- 不新增 Options API 页面、`var`、分号风格或双引号风格来匹配少量旧文件。
- 不复制历史目录拼写错误、超大组件或页面内重复请求封装。
- 不把 PC 的直接 `http` 风格强推给后台项目，也不为一次需求重构整个 API 层。
- 不因测试覆盖稀疏而省略适合的纯逻辑测试。
- 不批量格式化或重命名未涉及的历史组件。

## 按需读取

- [Web 仓库差异与证据](references/web-style-evidence.md)
- [Web 验证矩阵](references/web-validation.md)

## 输出要求

说明目标仓库、请求和路由模式、相邻样例、修改文件、用户交互状态、i18n 影响及执行的 pnpm 命令。多个 Web 仓库联动时逐仓库汇报。
