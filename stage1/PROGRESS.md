# Stage 1 — LLM 基础（进行中）

> 练习 1/6 ✅ | 下次：练习 2（Token 实验）

## 当前水平

Stage 0 全部完成 ✅（2026-05-30）
Stage 1 开始（2026-06-01）

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
- 分支：`master`（JSON）/ `yaml`（YAML）
- 旧代码：`stage0/`

## 学习风格 → 见根目录 CLAUDE.md

## 练习进度

| # | 练习 | 状态 |
|---|------|------|
| 1 | Hello World API 调用 | ✅ |
| 2 | Token 实验 | ⬜ |
| 3 | 成本/延迟计算 | ⬜ |
| 4 | 跨厂商比较 | ⬜ |
| 5 | Error Handling + Retry | ⬜ |
| 6 | 本地 LLM（Ollama） | ⬜ |

## 核心概念

| 概念 | 一句话 |
|------|--------|
| **token** | LLM 计算/计费的基本单位（中文 1 字 ≈ 1.5-2 token） |
| **context window** | 模型一次能看多少内容（有上限） |
| **temperature** | 控制回答稳定(0)还是发散(1) |

## 运行模式

- **当前**：DeepSeek API + OpenAI SDK
- **Path A（默认）**：Ollama 本地 → $0，但慢
- **Path B（可选）**：Anthropic API → 快但花钱

## 自我检查（完成后）

- [x] 写一个 5 行脚本调用 LLM API
- [ ] 理解 token 概念（如"Hello" = 1 token）
- [ ] 比较至少两个模型的 per-token 价格
- [ ] 体验至少 2 个不同 LLM

## 全局路线

```
Stage 0 ✅ → Stage 1(当前) → Stage 2
                                ↓
            Track A(用工具)    Track B(造 agent)
                                ↓
                          Stage 3-8 → Capstone
```
