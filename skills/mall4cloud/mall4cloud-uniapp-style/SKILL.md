---
name: mall4cloud-uniapp-style
version: 0.1.0
description: 基于 Mall4Cloud 三个 UniApp 仓库的多数约定实施或审查 H5、微信小程序、App 页面、请求、状态、条件编译、i18n、移动端样式和测试变更时使用。
user-invocable: true
tags:
  - mall4cloud
  - uniapp
  - multiplatform
  - style
---

# Mall4Cloud UniApp Style

## 适用范围

用于以下独立仓库：

- `mall4cloud-uniapp/`
- `mall4cloud-multishop-uniapp/`
- `mall4cloud-station/`

先读取目标仓库 `package.json`、`pages.json`、`src/utils/http.js`、i18n 配置和相邻页面。三个仓库的平台脚本、请求返回形状和状态管理并不相同。

## 工作顺序

1. 明确目标仓库和受影响平台：H5、微信小程序、App 或自定义平台。
2. 检查页面注册/分包、请求封装、登录授权、locale 和相邻条件编译。
3. 把共享业务逻辑放在条件块外，只对平台 API 和必要差异做最小条件编译。
4. 保证分页、表单、提交锁、下拉刷新和失败路径状态闭合。
5. 运行 lint/test 及所有受影响平台构建，并逐平台汇报。

## 必须遵循

- 新业务页面使用 `<script setup>`、Composition API 和 UniApp 生命周期，如 `onLoad`、`onShow`、`onReachBottom`、`onPullDownRefresh`。
- 模板优先使用 `view`、`text`、`image`、`scroll-view` 等跨端组件，主要交互沿用 `@tap`。
- 导航、存储、提示、确认、扫码和网络使用 UniApp API，不把 Web DOM 模式直接移入。
- 请求必须经过目标仓库 `src/utils/http.js`；调用前确认该仓库 resolve 的响应形状。
- H5 DOM/SDK、微信小程序 API、App `plus` 能力必须由正确条件编译保护。
- 条件编译标记必须成对、嵌套正确、作用域最小；共享流程不得复制成多个平台版本。
- 页面注册、分包和导航方式沿用目标仓库 `pages.json` 及现有 router 约定。
- 用户可见新文案使用 namespaced `$t(...)`；请求语言使用仓库 i18n 提供的后端 locale 转换。
- 页面和组件样式默认 `lang="scss" scoped`，移动端尺寸优先使用 `rpx` 和已有主题变量。
- 校验失败立即返回；提交、刷新和分页状态在成功与失败路径都要恢复。
- 仅在目标仓库已有 Pinia 时使用 `useXxxStore`；不为 station 的局部需求擅自引入全局状态库。

## 仓库差异

- `mall4cloud-uniapp`：请求成功通常直接得到业务 data；使用 Pinia，并包含 H5、微信小程序和 Android/iOS 等构建脚本。
- `mall4cloud-multishop-uniapp`：请求通常保留响应对象，页面常从中读取 `data`；使用 Pinia，覆盖 H5、微信小程序和 App。
- `mall4cloud-station`：请求通常保留响应对象，当前不使用 Pinia，现有脚本重点覆盖 H5 和测试模式。
- 差异以目标仓库当前 `src/utils/http.js` 和 `package.json` 为准，不凭记忆解构返回值或选择构建命令。

## 跟随邻近代码

- 简单移动表单可使用条件校验和 `uni.showToast`；复杂商家表单跟随 `uni-forms`、rules 和 `formRef.validate()`。
- 列表分页沿用相邻页面的 current/pages/loadAll 状态，搜索、tab 切换或下拉刷新时完整重置。
- 自动导入已有的 Vue、UniApp 生命周期、utils 和 stores 不做机械显式 import。
- 同目录使用 `@use` 时继续 `@use`；历史目录使用 `@import` 时不夹带无关迁移。
- 可测试的请求参数、权限、locale 和场景判断提取为纯函数并补 Vitest。

## 遗留例外勿复制

- 不新增 Options API 业务页面来匹配少量兼容组件。
- 不假设三个仓库的 `http.request` 返回相同结构。
- 不直接调用 `uni.request` 绕过 token、语言、业务码和登录处理。
- 不修改 `uni_modules` 来表达项目业务风格。
- 不把 Element Plus、HTML 标签、Vue Router 或固定 px Web 布局直接移植到 UniApp。
- 不只验证 H5 就宣称涉及微信小程序或 App 的改动完成。
- 不批量调整未涉及页面的条件编译、样式导入或历史命名。

## 按需读取

- [UniApp 平台差异与证据](references/uniapp-style-evidence.md)
- [UniApp 验证矩阵](references/uniapp-validation.md)

## 输出要求

说明目标仓库、目标平台、请求返回形状、页面/分包影响、条件编译分支、状态恢复逻辑以及每个平台的验证结果。
