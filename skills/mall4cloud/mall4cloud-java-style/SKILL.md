---
name: mall4cloud-java-style
version: 0.1.0
description: 基于 Mall4Cloud 现有多数代码约定实施或审查 Java 17 后端变更。修改 mall4cloud 微服务的 Controller、Service、Mapper、DTO/VO/BO、Dubbo 契约、事务、权限或测试时使用。
user-invocable: true
tags:
  - mall4cloud
  - java
  - backend
  - style
---

# Mall4Cloud Java Style

## 适用范围

仅用于工作区中的 `mall4cloud/` Java 17 Maven 后端。它约束代码如何融入现有项目，不代替需求分析、接口设计或跨端联调。

开始前读取根目录 `AGENTS.md` 和 `PROJECT_MAP.md`，再确认目标 Maven 模块及调用端：`app`、`platform`、`multishop`、`supplier`、`admin` 或 `ua`。

## 工作顺序

1. 在目标模块找到同端、同领域、同职责的相邻实现，不从其他模块机械复制。
2. 追踪受影响的 Controller、Service、Mapper/XML、model、DTO/VO/BO、`mall4cloud-api-*` 契约、Dubbo 实现和调用方。
3. 先保持接口契约和数据域安全，再按相邻代码实现最小变更。
4. 添加最小相关 JUnit 5 测试，优先使用 Mockito 单元测试或现有 XML/DTO 契约测试模式。
5. 从受影响模块开始执行 Maven 验证，并按独立仓库汇报结果。

## 必须遵循

- 包名保持在 `com.mall4j.cloud` 下，沿用现有 `controller`、`service`、`service.impl`、`mapper`、`model`、`dto`、`vo`、`bo`、`feign`、`manager` 等职责分层。
- 新对象按职责使用 `XxxDTO`、`XxxVO`、`XxxBO`；Service、实现、Mapper 和远程契约使用现有后缀。
- REST Controller 使用 `ServerResponseEntity<T>`；无响应数据的写操作使用 `ServerResponseEntity<Void>`。
- JSON 请求体使用 `@Valid @RequestBody`，字段约束放 DTO；复杂跨字段约束沿用 Jakarta Validation 或 `@AssertTrue`。
- 关系库分页沿用 `PageDTO`、`PageVO<T>` 和 `PageUtil.doPage`；ES、Mongo 保留各自分页类型。
- 业务失败使用 `LuckException`，优先复用已有 i18n key 或 `ResponseEnum`。
- 远程调用返回 `ServerResponseEntity` 时必须检查 `isSuccess()`，失败不得继续消费数据。
- 本地多写操作按需使用 `@Transactional(rollbackFor = Exception.class)`；只有确有跨服务一致性要求时才使用 `@GlobalTransactional`。
- Mapper 参数名、XML `#{...}` 和 `<foreach collection="...">` 必须一致；动态值使用参数化绑定。
- 权限变更同时检查 URI RBAC、`AuthUserContext` 和 tenant/shop/user 等资源归属，不能信任前端传入的数据域。
- 日志不得记录密码、Token、密钥、完整敏感配置、完整支付数据或真实用户隐私。

## 跟随邻近代码

- 当前多数类使用 `@Autowired` 字段注入和手写 getter/setter。小范围变更保持文件或模块一致，不夹带依赖注入或 Lombok 重构。
- DTO/model/VO 转换优先使用项目 `BeanUtil`，特殊字段显式处理。
- Logger 沿用 `LoggerFactory`；注释解释权限、幂等、缓存、事务、兼容等非显然原因。
- 公共契约保留 JavaDoc；新名称使用正确英文和标准 `DTO/VO/BO` 大写。
- SQL 延续目标 XML 的缩进和 resultMap 方式，优先显式列，不无理由改成另一套 ORM 风格。

## 遗留例外勿复制

- `FeignClient`、`FeignController` 是历史命名，实际远程实现使用 Dubbo；不要因此引入 Spring Cloud OpenFeign。
- 不复制历史拼写错误、大小写不一致或旧 snake_case Java 符号。已有公共 API 路径需要兼容时保持原值。
- 不把直接返回 `void`/裸集合、吞掉远程失败、宽泛 `catch (Exception)` 后继续执行等旧写法作为新模板。
- 不机械添加 `@PreAuthorize`；先确认该端是否由全局 `AuthFilter` 管理，再按资源需要补充方法权限。
- 不在无关需求中批量改 imports、注释、注入方式或旧接口命名。

## 禁止事项

- Controller 不直接操作 Mapper、数据库、Redis 或消息队列。
- 公共 API 不使用裸 `Map`/`Object` 代替明确 DTO/VO，也不直接暴露新的数据库 model。
- 不拼接用户输入生成 SQL、排序列或 `IN` 条件。
- 不无视远程失败、空返回、租户边界或资源归属。
- 不声明项目不存在的 Checkstyle、Spotless、PMD 或 Java lint 命令。

## 按需读取

- [后端风格证据](references/backend-style-evidence.md)
- [后端验证矩阵](references/backend-validation.md)

## 输出要求

说明目标模块、遵循的相邻样例、契约和数据域影响、修改文件、测试命令及结果。跨模块变更逐模块说明；未执行验证时给出具体原因。
