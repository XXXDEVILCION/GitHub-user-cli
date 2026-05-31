# Stage 1 — 起点

## 当前水平

Stage 0 全部完成 ✅（2026-05-30）

| 技能 | 说明 |
|------|------|
| GET 请求 | `requests.get()` + 状态码处理 |
| JSON/YAML | 读写配置文件，切换格式 |
| 文件读写 | open / write / 异常处理 |
| class 类 | `History` 类：`__init__`、实例方法、属性 |
| Token 认证 | GitHub API Bearer Token |
| async/await | `asyncio.gather` + `asyncio.to_thread` 并发查询 |
| Git | clone / branch / commit / push / fork |
| 模块化 | 拆分 api / config / history / info 模块 |

## 项目

- 仓库：https://github.com/XXXDEVILCION/GitHub-user-cli
- 项目：GitHub 用户查询器 CLI
- 分支：`master`（JSON 配置）/ `yaml`（YAML 配置）
- 代码在 `stage0/` 目录下

## 技术栈

- requests + Python 标准库
- 不使用其他第三方库

## 学习风格 → 见根目录 CLAUDE.md

## Stage 1 目标 — LLM 基础

> 路线图文件：`desktop/awesome-agentic-ai-zh-main/stages/01-llm-basics.zh-Hans.md`
> 预计 5-8 小时

### 三个核心概念

| 概念 | 一句话 |
|------|--------|
| **token** | LLM 计算/计费的基本单位（中文 1 字 ≈ 1.5-2 token） |
| **context window** | 模型一次能看多少内容（有上限） |
| **temperature** | 控制回答稳定(0)还是发散(1) |

### 6 个动手练习

1. **Hello World API** — 5 行代码调用 LLM，拿到第一个回复
2. **Token 实验** — 同一 prompt 跑多次，观察 token 变化
3. **成本/延迟计算** — 算 1000 次调用要花多少钱
4. **跨厂商比较** — 同一 prompt 发给 Claude / GPT / Gemini
5. **Error Handling** — 触发错误 + 写 retry
6. **本地 LLM** — 装 Ollama，跑一个本机模型（不花钱）

### 运行模式

- **Path A（默认）**：Ollama 本地跑 → $0，但慢
- **Path B（可选）**：Anthropic API → 快但花钱
- 练习 1-3 有完整起手码，4-5 有 starter 范本在 `examples/stage-1/`

### 进入条件（已具备 ✅）

- ✅ 编写 Python 脚本
- ✅ HTTP/REST 基础
- ✅ 获取并使用 API key

### 需要安装

```bash
pip install anthropic openai
# + 安装 Ollama: https://ollama.com
```

### 自我检查（完成后）

- [ ] 写一个 5 行脚本调用 LLM API
- [ ] 理解 token 概念（如"Hello" = 1 token）
- [ ] 比较至少两个模型的 per-token 价格
- [ ] 体验至少 2 个不同 LLM（Claude/GPT/Gemini/Ollama）

### 全局路线速览（备忘）

```
Stage 0 ✅ → Stage 1(当前) → Stage 2
                                ↓
            Track A(用工具)    Track B(造 agent)
                                ↓
                          Stage 3-8 → Capstone
```
