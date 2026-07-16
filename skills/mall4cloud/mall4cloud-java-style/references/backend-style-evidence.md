# Java 后端风格证据

这些路径用于确认规则来源。实现变更前仍应读取目标模块的相邻代码，因为历史模块之间存在差异。

## 分层与统一契约

| 关注点 | 证据路径 | 可复用模式 |
| --- | --- | --- |
| Controller | `mall4cloud/mall4cloud-product/src/main/java/com/mall4j/cloud/product/controller/platform/CategoryController.java` | 端别分包、REST/OpenAPI、统一响应、请求校验 |
| Service 接口 | `mall4cloud/mall4cloud-product/src/main/java/com/mall4j/cloud/product/service/CategoryService.java` | JavaDoc 业务契约、DTO/VO 边界 |
| Service 实现 | `mall4cloud/mall4cloud-product/src/main/java/com/mall4j/cloud/product/service/impl/CategoryServiceImpl.java` | `@Service`、显式 `@Override`、业务异常、事务和缓存 |
| Mapper | `mall4cloud/mall4cloud-product/src/main/java/com/mall4j/cloud/product/mapper/CategoryMapper.java` | 普通接口和显式 `@Param` |
| Mapper XML | `mall4cloud/mall4cloud-product/src/main/resources/mapper/CategoryMapper.xml` | resultMap、公共列、动态条件和 foreach |
| Model | `mall4cloud/mall4cloud-product/src/main/java/com/mall4j/cloud/product/model/Category.java` | `BaseModel`、Serializable、手写访问器 |
| DTO 校验 | `mall4cloud/mall4cloud-user/src/main/java/com/mall4j/cloud/user/dto/UserAddrDTO.java` | 字段约束和跨字段校验 |
| 分页请求 | `mall4cloud/mall4cloud-common/mall4cloud-common-database/src/main/java/com/mall4j/cloud/common/database/dto/PageDTO.java` | 页大小、排序方向和排序字段保护 |
| 分页响应 | `mall4cloud/mall4cloud-common/mall4cloud-common-database/src/main/java/com/mall4j/cloud/common/database/vo/PageVO.java` | `pages`、`total`、`list` |
| 分页执行 | `mall4cloud/mall4cloud-common/mall4cloud-common-database/src/main/java/com/mall4j/cloud/common/database/util/PageUtil.java` | PageHelper lambda 查询 |
| 统一响应 | `mall4cloud/mall4cloud-common/mall4cloud-common-core/src/main/java/com/mall4j/cloud/common/response/ServerResponseEntity.java` | success、fail、showFailMsg |
| 业务异常 | `mall4cloud/mall4cloud-common/mall4cloud-common-core/src/main/java/com/mall4j/cloud/common/exception/LuckException.java` | i18n key 和 `ResponseEnum` |

## 远程调用、权限与数据域

| 关注点 | 证据路径 | 可复用模式 |
| --- | --- | --- |
| API 契约 | `mall4cloud/mall4cloud-api/mall4cloud-api-user/src/main/java/com/mall4j/cloud/api/user/feign/UserFeignClient.java` | API 模块中的跨服务接口 |
| Dubbo 实现 | `mall4cloud/mall4cloud-user/src/main/java/com/mall4j/cloud/user/feign/UserFeignController.java` | `@DubboService` 实现历史 Feign 命名契约 |
| Dubbo 消费 | `mall4cloud/mall4cloud-product/src/main/java/com/mall4j/cloud/product/service/impl/CategoryServiceImpl.java` | `@DubboReference` 和远程响应检查 |
| 当前用户 | `mall4cloud/mall4cloud-user/src/main/java/com/mall4j/cloud/user/controller/app/UserAddrController.java` | `AuthUserContext` 和用户资源归属 |
| 全局 RBAC | `mall4cloud/mall4cloud-common/mall4cloud-common-security/src/main/java/com/mall4j/cloud/common/security/filter/AuthFilter.java` | URI、HTTP method、sysType、bizScene 权限检查 |
| 局部权限 | `mall4cloud/mall4cloud-product/src/main/java/com/mall4j/cloud/product/controller/supplier/TakeStockSpuController.java` | 特定资源的 `@PreAuthorize` 补充 |
| Mapper 扫描 | `mall4cloud/mall4cloud-common/mall4cloud-common-database/src/main/java/com/mall4j/cloud/common/database/config/MybatisConfig.java` | 全局 MapperScan，Mapper 无需逐个加注解 |

## 测试

| 测试类型 | 证据路径 | 可复用模式 |
| --- | --- | --- |
| Controller 单测 | `mall4cloud/mall4cloud-product/src/test/java/com/mall4j/cloud/product/controller/platform/CategoryControllerTest.java` | MockitoExtension、中文 DisplayName、ArgumentCaptor |
| DTO 校验 | `mall4cloud/mall4cloud-user/src/test/java/com/mall4j/cloud/user/dto/UserAddrDTOTest.java` | 真实 Jakarta Validator |
| Mapper XML 契约 | `mall4cloud/mall4cloud-order/src/test/java/com/mall4j/cloud/order/mapper/OrderMapperXmlTest.java` | XML 映射和 SQL 片段回归 |
| Service 单测 | `mall4cloud/mall4cloud-user/src/test/java/com/mall4j/cloud/user/service/impl/UserServiceImplTest.java` | Mockito 驱动的成功、失败和边界分支 |

## 规则分级

- **必须遵循**：接口包装、参数校验、SQL 参数化、远程失败处理、事务边界、权限与数据域、安全日志。
- **跟随邻近代码**：依赖注入、对象转换、Logger 声明、JavaDoc 密度和 XML 排版。
- **遗留例外**：错误拼写、裸远程返回、宽泛异常兼容、旧路径命名和少量特殊分页实现。

不要为了匹配“多数”而复制明显缺陷；也不要在单一业务变更中顺手现代化整个模块。
