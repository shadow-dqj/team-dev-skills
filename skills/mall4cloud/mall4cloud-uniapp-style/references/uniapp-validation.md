# UniApp 验证矩阵

所有命令从目标独立仓库根目录执行。以当前 `package.json` 为最终依据，先检查 `node` 和 `pnpm`。

## 用户端 `mall4cloud-uniapp`

基础检查：

```powershell
pnpm lint
pnpm test:run
pnpm check:mall-type
pnpm i18n:check-main
```

平台构建：

```powershell
pnpm build:h5
pnpm build:mp-weixin
```

涉及 App 时追加：

```powershell
pnpm build:app-android
pnpm build:app-ios
```

测试模式或自定义微信平台变更时，使用 `package.json` 中对应的 testing/custom 构建脚本。

## 商家端 `mall4cloud-multishop-uniapp`

```powershell
pnpm lint
pnpm test:run
pnpm build:h5
pnpm build:mp-weixin
```

涉及 App 时追加：

```powershell
pnpm build:app
```

## Station `mall4cloud-station`

当前仓库没有标准 `lint` script。只在确认本地依赖存在时使用：

```powershell
pnpm exec eslint --ext .js,.vue src
pnpm test:run
pnpm build:h5
```

测试环境相关改动追加：

```powershell
pnpm build:h5-test
```

## 平台选择

| 代码影响 | 最小构建 |
| --- | --- |
| 无条件共享页面/请求/i18n | 目标仓库支持的 H5 + 微信小程序；App 仓库按风险追加 App |
| `#ifdef H5` | H5 |
| `#ifdef MP-WEIXIN` | 微信小程序 |
| `#ifdef APP`/`APP-PLUS` | 对应 App 构建 |
| `pages.json`、分包、公共组件 | 所有受影响平台 |
| 登录、支付、扫码、上传 | 对应平台构建，加真实设备/开发者工具验证说明 |

## 结果汇报

逐平台记录命令和结果。构建通过不等于设备行为通过；需要开发者工具、真机、授权账号或外部服务时明确列为待人工验证。
