# Vue Web 验证矩阵

所有命令在目标独立仓库根目录执行。执行前检查本机 `node` 和 `pnpm`，不要在工作区整合根目录运行。

## 标准验证顺序

```powershell
pnpm format:check
pnpm lint
pnpm test:run
pnpm build
```

先执行与改动最相关的检查，再按风险扩大。不要用 `format` 或 `lint:fix` 改写未涉及文件，除非用户明确要求。

## 仓库矩阵

| 仓库 | 基础命令 | 条件命令 |
| --- | --- | --- |
| `mall4cloud-platform` | `pnpm format:check`、`pnpm lint`、`pnpm test:run`、`pnpm build` | 无 |
| `mall4cloud-multishop` | `pnpm format:check`、`pnpm lint`、`pnpm test:run`、`pnpm build` | 无 |
| `mall4cloud-pc` | `pnpm format:check`、`pnpm lint`、`pnpm test:run`、`pnpm build` | 测试环境相关改动追加 `pnpm build:test` |
| `mall4cloud-slipper` | `pnpm format:check`、`pnpm lint`、`pnpm test:run`、`pnpm build` | 无 |

以目标仓库当前 `package.json` 为最终依据；脚本变化后更新本矩阵。

## 变更类型与附加检查

| 变更类型 | 附加检查 |
| --- | --- |
| API | method、params/data、响应形状、全局错误处理和所有调用页面 |
| 列表页 | 搜索重置、分页重置、loading、空态、删除后页码和刷新 |
| 表单/弹窗 | 默认值、编辑回填、rules、提交锁、关闭后清理和错误路径 |
| Store | 初始化、持久化、退出清理、并发请求和路由守卫依赖 |
| 路由 | 目标仓库的动态路由或 glob 机制、权限、404 和懒加载路径 |
| i18n | 所需 locale key、动态文本、语言切换和后端 locale |
| 样式 | scoped 边界、`:deep`、窄屏/宽屏、主题变量和资源路径 |

## 结果汇报

记录目标仓库、准确命令和结果。跨仓库任务逐个列出，不用一个仓库的构建结果代表其他仓库。
