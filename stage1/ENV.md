# Stage 1 — 环境状态

## 已安装

| 组件 | 版本 | 备注 |
|------|------|------|
| Python | 3.14 | |
| openai SDK | 2.38.0 | `pip install openai` |
| DeepSeek API Key | ✅ | 环境变量 `DEEPSEEK_API_KEY` |

## 待安装

| 组件 | 备注 |
|------|------|
| Ollama | 等免费 WiFi 时下载 |
| anthropic SDK | 暂不需要（不走 Anthropic 路线） |

## API 配置

```bash
# 当前窗口（临时）
$env:DEEPSEEK_API_KEY="你的key"

# 永久（新窗口生效）
setx DEEPSEEK_API_KEY "你的key"
```
