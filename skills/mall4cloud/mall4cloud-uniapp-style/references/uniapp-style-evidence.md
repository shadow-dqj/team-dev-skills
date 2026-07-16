# UniApp 风格证据

## 共同基线

三个仓库的新业务页面以 `<script setup>` 和 Composition API 为主，使用 UniApp 生命周期、跨端组件、UniApp API、条件编译、vue-i18n 和 scoped SCSS。

| 关注点 | 证据路径 | 可复用模式 |
| --- | --- | --- |
| 用户端构建 | `mall4cloud-uniapp/package.json` | H5、微信小程序、Android/iOS、lint、test 和专项检查 |
| 自动导入/平台构建 | `mall4cloud-uniapp/vite.config.js` | UniApp 生命周期和平台 build target |
| 页面注册 | `mall4cloud-uniapp/src/pages.json` | 页面、tabBar、分包和平台配置 |
| 请求封装 | `mall4cloud-uniapp/src/utils/http.js` | uni.request、token、语言、业务码和登录过期 |
| 路由兼容 | `mall4cloud-uniapp/src/router/index.js` | 用户端 router 钩子及 H5 条件编译 |
| 页面生命周期 | `mall4cloud-uniapp/src/pages/category/category.vue` | onLoad、onShow、跨端组件和业务请求 |
| 组件契约 | `mall4cloud-uniapp/src/components/show-price/show-price.vue` | defineProps 和展示计算 |
| Store | `mall4cloud-uniapp/src/stores/modules/cart-count.js` | Pinia Options Store |
| i18n | `mall4cloud-uniapp/src/i18n/index.js` | locale 标准化、分包 locale 和后端 locale |
| 测试 | `mall4cloud-uniapp/src/utils/login-auth.test.js` | 请求参数构造纯函数的 Vitest |

## 条件编译

项目使用 UniApp 原生条件编译：

- 模板：`<!-- #ifdef H5 -->` 和 `<!-- #endif -->`
- JavaScript：`// #ifdef MP-WEIXIN` 和 `// #endif`
- CSS：`/* #ifdef APP-PLUS */` 和 `/* #endif */`

浏览器 `window`/`document`、微信小程序对象、App `plus` 和平台支付/扫码能力必须位于对应分支。共享参数校验、业务状态和响应处理应留在条件块外。

## 仓库差异

### 用户端

- 请求封装：`mall4cloud-uniapp/src/utils/http.js`。
- 请求成功通常 resolve 业务 data，调用方不应再次机械解构同一层 `data`。
- 页面样例：`mall4cloud-uniapp/src/pages/category/category.vue`。
- Store 样例：`mall4cloud-uniapp/src/stores/modules/cart-count.js`。

### 商家移动端

- 请求封装：`mall4cloud-multishop-uniapp/src/utils/http.js`。
- API 样例：`mall4cloud-multishop-uniapp/src/api/rbac/menu.js`。
- Store 样例：`mall4cloud-multishop-uniapp/src/stores/modules/user.js`。
- 首页/扫码的平台分支样例：`mall4cloud-multishop-uniapp/src/pages/index/index.vue`。
- 复杂表单样例：`mall4cloud-multishop-uniapp/src/package-settings/pages/store-settings-basic/store-settings-basic.vue`。

### Station

- 请求封装：`mall4cloud-station/src/utils/http.js`。
- 分页样例：`mall4cloud-station/src/pages/order-list/order-list.vue`。
- 组件契约：`mall4cloud-station/src/components/area-picker/area-picker.vue`。
- i18n：`mall4cloud-station/src/i18n/index.js`。
- 当前没有 Pinia 基线；局部状态优先留在页面/组件。

## 变更检查

- 页面是否已在正确主包或分包注册。
- 导航 API 是否匹配 tabBar、普通页面和替换当前页语义。
- 请求返回形状是否来自目标仓库真实封装。
- 未登录、语言和全局业务码是否由封装统一处理。
- 条件编译是否成对，且所有引用的平台对象都在保护范围内。
- 分页和下拉刷新是否正确重置页码、列表和完成状态。
- 用户文案是否同步 locale；移动端尺寸和安全区域是否沿用相邻页面。
