# ErisPulse 模块源配置指南

## 全功能源列表
| 源名称 | 类型 | 协议 | 地址 |
|--------|------|------|------|
| AsyncRBPS | 异步 | HTTPS | `https://raw.githubusercontent.com/wsu2059q/AsyncRBPS-Origin/refs/heads/main/map.json`
| SDKFrame CDN | 异步 | HTTPS | `https://sdkframe.anran.xyz/`
| r1a 同步 | 同步 | HTTPS | `https://runoneall.serv00.net/ryhsdk2/`

## 自定义源配置

### 基础配置
```json
{
  "name": "源名称",
  "base": "基础URL地址",
  "modules": {
    "模块名": {
      "path": "模块路径",
      "meta": {
        "name": "模块名",
        "author": "作者",
        "description": "描述",
        "version": "版本",
        "license": "协议",
        "homepage": "网站"
      },
    }
  }
}
```

### 高级配置
```json
{
  "dependencies": {
    "requires": ["必需依赖模块"],
    "optional": [
      "可选模块",
      ["可选模块"]
      ["可选组依赖模块1", "可选组依赖模块2"]
    ],
    "pip": ["Python依赖包"]
  }
}
```

### 配置说明
1. **组依赖规则**：
   - 可选模块与组依赖模块（如 `["组依赖模块1", "组依赖模块2"]`）构成“或”关系，即满足其中一组即可。
   - 组依赖模块以数组形式表示，视为一个整体（例如：`组依赖模块1 + 组依赖模块2` 和 `可选模块` 中任意一组存在即符合要求）。

2. **版本规范**：
   - 遵循语义化版本控制（SemVer），格式为：`主版本号.次版本号.修订号`。

3. **路径规则**：
   - 模块路径为相对路径，基于 `base URL`。
   - 支持 `.zip` 格式压缩包。

### 最佳实践
- **模块体积**：尽量保持单个模块小于 10MB。
- **版本管理**：每次更新时递增版本号，确保版本清晰可追溯。
- **依赖说明**：提供完整的依赖列表及说明，避免遗漏。
- **测试覆盖**：对所有可能的依赖组合进行充分测试，确保兼容性。

> 💡 提示：可以使用JSON验证工具检查配置格式是否正确
