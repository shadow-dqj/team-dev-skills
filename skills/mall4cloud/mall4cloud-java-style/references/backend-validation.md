# Java 后端验证矩阵

所有命令从 `mall4cloud/` 后端仓库根目录执行。先确认 Maven 可用，再从最小受影响模块开始。

## 按模块测试

| 影响范围 | 首选命令 |
| --- | --- |
| 商品 | `mvn -pl mall4cloud-product -am test` |
| 订单/配送 | `mvn -pl mall4cloud-order -am test` |
| 用户 | `mvn -pl mall4cloud-user -am test` |
| 平台管理 | `mvn -pl mall4cloud-admin -am test` |
| 支付 | `mvn -pl mall4cloud-payment -am test` |
| 营销 | `mvn -pl mall4cloud-marketing -am test` |
| 搜索 | `mvn -pl mall4cloud-search -am test` |

`-am` 会连同依赖模块构建。不要在工作区整合根目录直接执行 Maven 命令。

## 按测试类快速回归

使用目标模块已有测试类名替换占位符：

```powershell
mvn -pl <module> -am -Dtest=<TestClass> test
```

如果依赖模块没有匹配测试而导致 Surefire 报错，先检查项目现有 Maven 配置，不要用跳过失败参数掩盖真实测试问题。

## 仅验证可打包性

只有在测试已单独完成或用户明确要求跳过测试时使用：

```powershell
mvn -pl <module> -am package -DskipTests
```

## 变更类型与附加检查

| 变更类型 | 附加检查 |
| --- | --- |
| Controller/DTO | 请求校验、OpenAPI 注解、统一响应、端别路径和调用方 |
| Mapper/XML | `@Param` 与 XML 名称、resultMap、动态 SQL、空集合、分页和 XML 契约测试 |
| 跨服务 API | `mall4cloud-api-*`、Dubbo 实现、所有消费者、错误响应和序列化兼容 |
| 事务 | 本地/全局事务范围、远程失败、消息/缓存副作用和幂等 |
| 权限 | AuthFilter 路径、sysType、bizScene、tenant/shop/user 资源归属 |
| 公共模块 | 所有直接依赖模块；必要时扩大 Maven 模块列表 |

## 结果汇报

记录准确命令、退出状态和失败原因。跨模块修改时分别说明每个模块的测试结果；不要用“后端验证通过”代替具体范围。
