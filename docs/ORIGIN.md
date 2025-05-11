# ErisPulse 模块源配置指南

## 全功能源列表
| 源名称 | 类型 | 协议 | 地址 |
|--------|------|------|------|
| AsyncRBPS | 异步 | HTTPS | `https://raw.githubusercontent.com/wsu2059q/AsyncRBPS-Origin/refs/heads/main/map.json`
| SDKFrame CDN | 异步 | HTTPS | `https://sdkframe.anran.xyz/`
| r1a 同步 | 同步 | HTTPS | `https://runoneall.serv00.net/ryhsdk2/`

## 如何添加自定义源

1. 通过 CLI 命令添加：
   ```bash
   epsdk origin add https://your.domain/source.json
   ```
2. 添加后建议执行 `epsdk update` 更新模块索引。

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

### 常见源配置错误及排查

- **JSON 格式错误**：请使用 JSON 校验工具检查格式。
- **路径错误**：确保 `base` 和 `path` 拼接后可直接访问模块文件。
- **依赖未声明**：所有依赖模块需在 `dependencies` 中声明，否则安装时可能失败。

### 源安全性建议

- 建议使用 HTTPS 协议托管源文件，防止中间人攻击。
- 不要轻信第三方源，避免下载恶意模块。
- 定期检查源内容的完整性和安全性。

### 最佳实践
- **模块体积**：尽量保持单个模块小于 10MB。
- **版本管理**：每次更新时递增版本号，确保版本清晰可追溯。
- **依赖说明**：提供完整的依赖列表及说明，避免遗漏。
- **测试覆盖**：对所有可能的依赖组合进行充分测试，确保兼容性。
