# Vue Web 风格证据

## 共同基线

四个 Web 仓库以 Vue 3、Vite、Pinia 和 Vue Router 为主，新业务 Vue 文件绝大多数使用 `<script setup>`。格式以各仓库 `.oxfmtrc.json` 和 `.oxlintrc.json` 为准。

| 关注点 | 证据路径 | 可复用模式 |
| --- | --- | --- |
| 格式 | `mall4cloud-platform/.oxfmtrc.json` | 单引号、无分号、2 空格、Vue 多属性排版 |
| 自动导入 | `mall4cloud-platform/vite.config.js` | Vue、router、stores、hooks、utils 和组件自动导入 |
| 请求封装 | `mall4cloud-platform/src/utils/request.js` | token、语言、业务码和未授权处理 |
| 领域 API | `mall4cloud-platform/src/api/product/brand.js` | page/get/save/update/deleteById 具名函数 |
| 列表页 | `mall4cloud-platform/src/views/modules/product/brand/index.vue` | 搜索、表格、分页、确认操作和刷新 |
| 表单弹窗 | `mall4cloud-platform/src/views/modules/product/brand/add-or-update.vue` | reactive 表单、validate、defineExpose(init) |
| 组件契约 | `mall4cloud-platform/src/components/pagination/index.vue` | defineProps、defineEmits 和双向分页状态 |
| Store | `mall4cloud-platform/src/stores/modules/user.js` | `useUserStore` 和 Options Store actions |
| 路由 | `mall4cloud-platform/src/router/index.js` | 基础路由、Layout 和动态权限配合 |
| i18n | `mall4cloud-platform/src/i18n/index.js` | locale 聚合和语言切换 |

## 仓库差异

### Platform

- 管理平台页面集中在 `src/views/modules/`。
- 请求按领域放在 `src/api/`，统一走 `src/utils/request.js`。
- 代表样例：`mall4cloud-platform/src/views/modules/product/brand/index.vue`。

### Multishop

- 商家后台同样使用领域 API 和管理端页面结构。
- 商品分类代表样例：`mall4cloud-multishop/src/views/modules/product/manage/category/index.vue`。
- API 代表样例：`mall4cloud-multishop/src/api/product/brand.js`。
- Vitest 代表样例：`mall4cloud-multishop/src/utils/shop-login-ui.test.js`。

### Slipper

- 保持独立仓库的 API、store 和页面组织，不假设与 platform 完全相同。
- API 样例：`mall4cloud-slipper/src/api/product/price.js`。
- 页面样例：`mall4cloud-slipper/src/views/modules/product/price-manage/log/index.vue`。
- Store 样例：`mall4cloud-slipper/src/stores/modules/prod.js`。

### PC

- 请求封装：`mall4cloud-pc/src/plugins/http.js`。
- 路由生成：`mall4cloud-pc/src/router/index.js`，使用 `import.meta.glob` 和用户中心子路由。
- Store：`mall4cloud-pc/src/stores/user.js`。
- 组件：`mall4cloud-pc/src/components/pagination/index.vue`。
- 不要求把所有页面请求迁入后台式领域 API 文件；新增代码先跟随所在领域。

## 样式与交互检查

- Element Plus 表单：model、rules、ref、validate。
- 危险操作：确认框、loading、防重复提交、完成后刷新。
- 弹窗组件：父级 ref + 子级 `defineExpose({ init })`，并跟随相邻的 `v-if`/`nextTick` 生命周期。
- i18n：使用现有命名空间 key；同步目标仓库要求的 locale 文件。
- scoped SCSS：组件边界内维护，Element Plus 内部覆盖使用 `:deep`。

规则只用于新增或实际触及的代码。不要以“统一风格”为理由改写整个历史页面。
