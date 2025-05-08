# 🚀 ErisPulse - 异步机器人开发框架

> "基于 [RyhBotPythonSDK V2](https://github.com/runoneall/RyhBotPythonSDK2) 和 [SDKFrame](https://github.com/runoneall/sdkFrame) 构建"

---

## 🔍 项目简介

ErisPulse 是一个**轻量级、异步化、模块化**的 Python 机器人开发框架，支持快速构建功能丰富、可扩展性强的机器人应用。适用于聊天机器人、消息处理、自动化运维等多个场景。

- ✅ 支持异步编程模型
- ✅ 提供模块化架构设计
- ✅ 可通过 CLI 管理模块和源
- ✅ 内置依赖管理和日志系统
- ✅ 支持多种适配器（如 OneBot）

---

## 📦 功能特性

### ✨ 模块化设计
你可以通过实现规范化的模块接口，轻松扩展功能：
- 定义 `moduleInfo` 字典描述元信息
- 实现 Main 类作为入口
- 支持依赖注入（必需依赖/可选依赖/Pip 包）

### ⚙️ CLI 管理工具
提供完整的命令行接口用于管理模块和源：

#### 模块管理
| 命令       | 参数                      | 描述                                  | 示例                          |
|------------|---------------------------|---------------------------------------|-------------------------------|
| `enable`   | `<module> [--init]`       | 激活指定模块                          | `epsdk enable chatgpt --init` |
| `disable`  | `<module> [--init]`       | 停用指定模块                          | `epsdk disable weather`       |
| `list`     | `[--module=<name>]`       | 列出模块（可筛选）                   | `epsdk list --module=payment` |
| `update`   | -                         | 更新模块索引                           | `epsdk update`                |
| `upgrade`  | `[--force] [--init]`      | 升级模块（`--force` 强制覆盖）        | `epsdk upgrade --force`       |
| `install`  | `<module...>`             | 安装一个或多个模块                    | `epsdk install translator analyzer` |
| `uninstall`| `<module>`                | 移除指定模块                          | `epsdk uninstall old-module`  |

#### 源管理
| 命令 | 参数 | 描述 | 示例 |
|------|------|------|------|
| `origin add` | `<url>` | 添加源 | `epsdk origin add https://example.com/source.json` |
| `origin list` | - | 源列表 | `epsdk origin list` |
| `origin del` | `<url>` | 删除源 | `epsdk origin del https://example.com/source.json` |

---

## 🧱 开发者指南

### 🛠️ 开发建议
- **日志记录**：使用内置 [logger](file://d:\devs\ErisPulse\ErisPulse\modules\AIChat\Core.py#L0-L0) 记录关键操作
- **减少第三方依赖**：优先使用 Python 原生库
- **性能优化**：
  - 使用异步编程模型
  - 避免阻塞操作
  - 引入缓存机制以提升性能

### 📁 模块结构推荐
```plaintext
模块名/
├── __init__.py        # 模块入口文件
└── Core.py            # 核心逻辑实现
```

### 📦 moduleInfo 字典示例
```python
moduleInfo = {
    "meta": {
        "name": "logger",  # 模块名称（必填）
        "author": "ErisPulse",  # 开发者姓名（选填）
        "description": "Test Logger Module",  # 模块功能描述（选填）
        "version": "1.0.0",  # 版本号（选填）
        "license": "MIT",  # 许可证（选填）
        "homepage": "",  # 项目主页（选填）
    },
    "dependencies": {
        "requires": [],  # 必需依赖模块列表
        "optional": [],  # 可选依赖模块列表
        "pip": [["mod1", "mod2"], ["mod3"], "mod4"],  # 第三方 pip 依赖列表
    },
}
```

---

## 🧪 最佳实践

### 📝 日志记录的最佳实践
- 分级记录：根据问题严重性选择合适的日志级别
- 上下文信息：在日志中添加上下文信息（如用户 ID、请求 ID），便于排查问题

### ⏱️ 异步编程注意事项
- 避免阻塞操作：尽量使用异步库替代阻塞式库（如 `aiohttp` 替代 `requests`）
- 任务管理：使用 `asyncio.create_task` 创建后台任务，并确保任务异常被捕获

### 🛡️ 异常处理
务必在入口方法中使用 `try...except` 捕获异常，避免线程意外退出。

---

## 📚 相关文档

- [CHANGELOG.md](https://github.com/ErisPulse/ErisPulse/edit/main/docs/CHANGELOG.md): 查看版本更新历史
- [CLI.md](https://github.com/ErisPulse/ErisPulse/edit/main/docs/CLI.md): 命令行工具使用说明
- [DEVELOPMENT.md](https://github.com/ErisPulse/ErisPulse/edit/main/docs/DEVELOPMENT.md): 开发指南
- [ORIGIN.md](https://github.com/ErisPulse/ErisPulse/edit/main/docs/ORIGIN.md): 模块源配置指南

---

## 🌐 在线资源

- [GitHub 仓库](https://github.com/ErisPulse/ErisPulse)
- [模块市场](RdZN5A/modules.html)
- [官方模块源](https://github.com/ErisPulse/ErisPulse-ModuleRepo)

---

## 🤝 贡献指南

欢迎参与项目贡献！请参考我们的 [开发指南](https://github.com/ErisPulse/ErisPulse/edit/main/docs/DEVELOPMENT.md) 获取更多信息。

---

## 📄 许可协议

本项目采用 MIT License，请查看具体条款。
