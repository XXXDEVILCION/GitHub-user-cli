# Stage 1 — 学习日志

## 练习 1：Hello World API（2026-06-01 晚）✅

**代码**：`stage1/practice_1_hello_api.py`
**对话记录**：`stage1/logs/chat_log_2026-06-01.txt`

### 过程回顾

从阅读 OpenAI Quickstart 开始 → 不理解 SDK 是什么 → 发现自己没有 OpenAI key 但有 DeepSeek key → 学会改 `base_url` 连 DeepSeek → 跑通。

### 核心收获

1. **SDK 是什么**：某家公司写好的 Python 库，装了直接调函数跟服务通信，不用自己拼 HTTP 请求。SDK 本质上封装了 `requests.post()` 那一套——拼 URL、设 header、序列化、解析 JSON。

2. **构造器 vs 参数**：`OpenAI(api_key, base_url)` 放"不变的"（服务器地址、身份），`.chat.completions.create(model, messages)` 放"每次都变的"（模型名、消息内容）。几乎所有 API SDK 都用这个模式。

3. **API 文档看 Schema**：Request Schema（发过去的参数结构）和 Response Schema（返回的数据结构）。读文档时 Schema 比文字描述更精确。

4. **response.choices[0].message.content** 路径展开：
   - `response` → SDK 创建的对象
   - `.choices` → 列表（通常只有一个元素）
   - `[0]` → 第一个 choice
   - `.message` → 消息对象
   - `.content` → 文本内容

5. **DeepSeek API 兼容 OpenAI**：行业把 OpenAI 的 API 格式当成事实标准，后来者主动兼容，所以同一个 SDK 改 `base_url` 就能用。

### 关键转折

认识到自己不止是在"跑通练习 1"，顺便学会了**怎么看 API 文档**——找 API Reference → 看 Request Schema → 看 Response Schema → 写代码 → 跑 → 看报错 → 改。这个能力比练习 1 本身重要。
