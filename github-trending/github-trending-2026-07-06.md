# GitHub Trending 每日自动总结报告 (2026-07-06)

作为一名世界顶尖的 AI 软件架构师，我将为您深度剖析今日 GitHub Trending 榜单。今日的榜单展现了 AI Agent 生态系统的爆发式演进，尤其是围绕 **Claude Code** 与 **模型上下文协议 (MCP)** 的工具、技能包（Skills）和多智能体协同管理工具占据了半壁江山。

---

## 1. Trending Top 20 榜单表格

| 项目名称与链接 | 语言 | 总Star | 今日新增Star | 功能描述 |
| :--- | :--- | :--- | :--- | :--- |
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Rust | 16,755 | 1,409 | 隐私优先的本地 AI 会议助手，支持极速 Whisper 转录和 Ollama 摘要 |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | JavaScript | 25,379 | 1,519 | 在 Claude Code 中调用 OpenAI Codex 进行代码审查与任务分发的插件 |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 49,827 | 981 | 收集并定期更新各大主流 AI 模型（如 GPT-5.5、Claude 5 等）系统提示词的项目 |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | JavaScript | 57,360 | 850 | 赋予 AI “良好品味”以防止生成千篇一律、枯燥无聊内容的技能库 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Python | 20,491 | 394 | 包含 337 个针对 Claude Code 及其他编码代理的专业技能与插件库 |
| [rommapp/romm](https://github.com/rommapp/romm) | Python | 10,496 | 411 | 界面美观、功能强大的自托管复古游戏 ROM 管理器与网页播放器 |
| [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | Rust | 11,996 | 650 | 运行在终端内的高性能智能体多路复用器（Agent Multiplexer） |
| [alibaba/page-agent](https://github.com/alibaba/page-agent) | TypeScript | 23,784 | 801 | 阿里巴巴开源的网页内置 GUI 智能体，用自然语言控制网页交互 |
| [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | Python | 26,807 | 333 | 哈佛大学开源的《机器学习系统》（Machine Learning Systems）课程教科书 |
| [usestrix/strix](https://github.com/usestrix/strix) | Python | 36,997 | 1,121 | 开源 AI 渗透测试工具，可自主寻找并修复应用程序中的漏洞 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Python | 48,306 | 188 | 针对 Anthropic 顶级编码代理 Claude Code 的精选资源、插件与工具大合集 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | JavaScript | 36,375 | 209 | 为 Claude Code 等智能体量身定制的营销、SEO、文案及增长技能包 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | JavaScript | 84,783 | 1,043 | 极简主义技能包，让 Claude Code 模仿“原始人”说话，直接砍掉 65% Token 消耗 |
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | C# | 11,896 | 415 | Unity 编辑器的模型上下文协议（MCP）桥梁，允许 AI 助手管理资产、编辑脚本 |
| [facebook/astryx](https://github.com/facebook/astryx) | TypeScript | 5,835 | 540 | Meta 开源的天然对 AI 智能体友好且完全可定制的现代化设计系统 |
| [immich-app/immich](https://github.com/immich-app/immich) | TypeScript | 106,047 | 475 | 高性能开源自托管多媒体照片/视频管理器，具机器学习人脸识别功能 |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 76,676 | 198 | 将普通 WiFi 信号转化为实时空间智能、生命体征监测和存在检测的系统 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Go | 16,344 | 48 | 基于 Go 语言开发的多智能体并发工作空间及沙箱管理器 |
| [dotnet/skills](https://github.com/dotnet/skills) | C# | 4,015 | 247 | 微软官方开源，辅助 AI 编码代理进行 .NET 和 C# 高效开发的技能仓库 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Python | 24,664 | 61 | 基于物理文件、具有抗崩溃和状态共享特征的 AI 智能体长任务规划工具 |

---

## 2. 项目详细分析

### Zackriya-Solutions/meetily
* **核心功能与技术特点**：Meetily 是一款专注于极致隐私和本地推断的 AI 会议助手，支持 macOS 和 Windows 双平台。它能够在完全不依赖任何云端资源的情况下，提供比传统云服务快 4 倍的实时语音转文字、发言人识别（Diarization）和智能会议摘要。
* **主要技术栈和实现方式**：该项目底层采用高并发且内存安全的 **Rust** 语言构建，结合了 Parakeet 和 Whisper 模型的硬件加速本地推断。文本摘要与分析通过本地运行的 **Ollama**（运行 Llama 或 Mistral 等模型）实现。
* **适用的应用场景**：特别适用于对机密信息合规性、知识产权保护有严苛要求的企业内部会议、政企涉密交流以及医疗、学术研讨会等全本地运行场景。

### openai/codex-plugin-cc
* **核心功能与技术特点**：该项目是 OpenAI 官方推出的 Codex 插件，允许开发者在 Anthropic 的终端编码 Agent——**Claude Code** 中，调用 OpenAI Codex 强大的代码生成和分析能力。它打破了单一模型和生态的孤立性，实现了多模型混合式编码。
* **主要技术栈和实现方式**：采用 **JavaScript** 构建，通过标准化 API 桥接层与 Claude Code 的运行上下文环境融合。它将 Claude 的规划推理能力与 Codex 的代码库生成直觉完美结合。
* **适用的应用场景**：适用于复杂的跨平台大项目重构、深度代码审查，以及需要多模型“红蓝对抗”校验的高标准软件研发场景。

### asgeirtj/system_prompts_leaks
* **核心功能与技术特点**：这是一个针对全球顶尖商业 AI 模型（包含最新 ChatGPT 5.5 Thinking、Claude 5、Gemini 3.5、Grok、Cursor 等）系统提示词（System Prompts）进行提取和逆向汇总的开源仓库。
* **主要技术栈和实现方式**：虽然主要标记语言为 **JavaScript**，但其核心价值在于收录的安全分析报告和原始 Prompt 结构。它深入剖析了各大模型在防注入、安全对齐以及长文本推理时的内部“元指令”。
* **适用的应用场景**：极其适合提示词工程师（Prompt Engineers）、大模型安全研究员、以及需要为自建 Agent 构建高质量“防御性”系统提示词的系统架构师。

### Leonxlnx/taste-skill
* **核心功能与技术特点**：Taste-Skill 是一套能赋予大语言模型“良好品味（Good Taste）”的约束性扩展技能库。它的主要作用在于抑制 AI 在内容生成时常见的套路化、空洞乏味、极具“AI 味”的垃圾内容（slop）。
* **主要技术栈和实现方式**：利用 **JavaScript** 编写，通过高度定制的上下文惩罚逻辑、多样性注入机制和审美范式模板，对大模型的输出流进行实时引导与格式重塑。
* **适用的应用场景**：广泛适用于 AI 辅助文案写作、自动化产品宣发材料生成，以及希望保持独特个性和高级语感的创意内容生成系统。

### alirezarezvani/claude-skills
* **核心功能与技术特点**：这是一个极为强悍的 Claude Code 技能大百科全书，内含 337 个跨界技能、30 多个定制 Agent 和 70 多个自定义命令。其能力边界大大超出了纯软件开发，辐射至商务运营、合规审计、C-Level 战略决策等。
* **主要技术栈和实现方式**：项目使用 **Python** 开发，通过模块化的 SKILL.md 规范与各大终端编码工具（如 Claude Code, Codex, Cursor）无缝贴合，允许动态加载脚本。
* **适用的应用场景**：非常适合全栈开发者、初创企业技术负责人以及致力于为企业打造全能“数字员工”架构的转型团队。

### rommapp/romm
* **核心功能与技术特点**：RomM 是一款极其现代、高颜值且功能完备的自托管复古游戏 ROM 管理器与 Web 播放器。它能够自动通过网络 API 抓取游戏封套、年代及元数据，并直接在网页中启动模拟器进行游玩。
* **主要技术栈和实现方式**：该项目基于 **Python** 构建其健壮的后端，提供高效的多媒体元数据检索与本地文件存储映射；前端则提供流畅的响应式 Web UI，支持 Docker 容器化一键部署。
* **适用的应用场景**：非常适合私有云玩家、家庭实验室（HomeLab）发烧友以及希望在一个统一入口内整理和游玩数万款怀旧游戏的游戏收藏家。

### ogulcancelik/herdr
* **核心功能与技术特点**：herdr 是一款旨在提高终端极客工作效率的智能体多路复用器（Agent Multiplexer）。它允许开发者在单个终端命令行窗口内，同时唤醒、调度、监控并并发运行多个不同的 AI 编码代理。
* **主要技术栈和实现方式**：项目使用高性能的 **Rust** 开发，通过多线程、异步 I/O 以及精心设计的终端多窗口管理层，实现对各种 CLI 代理标准输入输出的精准控制。
* **适用的应用场景**：适合重度命令行极客、DevOps 专家，以及需要同时调度多个自动化 Agent 并发处理大规模重构任务的高级工程师。

### alibaba/page-agent
* **核心功能与技术特点**：Page-Agent 是阿里巴巴开源的、运行在网页内置的 GUI 智能体。它能够让用户在不编写任何定位选择器（Selector）或模拟代码的情况下，直接通过自然语言命令控制网页交互。
* **主要技术栈和实现方式**：项目深度依赖 **TypeScript**。核心实现方式是将网页 DOM 结构及其可视渲染状态直接转化为结构化数据，由内嵌的多模态轻量级 Agent 引擎进行实时决策并派发物理鼠标/键盘事件。
* **适用的应用场景**：最适用于无脚本化的 UI 自动化测试、无障碍网页浏览辅助、电商数据采集以及跨系统的 Web 工作流自动化（RPA）。

### harvard-edge/cs249r_book
* **核心功能与技术特点**：cs249r_book 是哈佛大学 Edge 计算实验室《机器学习系统》（Machine Learning Systems）课程配套的开源书籍源码库。它专注于将机器学习算法推向物理世界的“边缘”，重点讨论软硬件协同与端侧计算。
* **主要技术栈和实现方式**：核心采用 **Python** 示例。它全面涵盖了 TinyML（微型机器学习）、模型压缩（剪枝、量化）、端侧低功耗推理框架以及针对专有硬件的编译优化技术。
* **适用的应用场景**：适用于想要从纯算法研究向高性能计算（HPC）、物联网 AI、端侧芯片编译器方向转型的硬核系统工程师和学生。

### usestrix/strix
* **核心功能与技术特点**：Strix 是一款前沿的开源 AI 渗透测试平台。它利用自主决策 Agent 来扫描应用系统的潜在漏洞，并能够像人类安全专家一样进行多步漏洞利用链验证，甚至直接生成用于闭环安全漏洞的补丁。
* **主要技术栈和实现方式**：底层基于 **Python**，内置了丰富的已知安全规则和推理大脑。它能够自动理解复杂的应用架构，动态生成攻击 Payload，并将测试过程以可视化的形式复盘。
* **适用的应用场景**：适用于 DevSecOps 流程中的静态/动态安全左移测试，帮助中大型企业研发团队在发布产品前进行全自动化的红蓝对抗模拟。

### hesreallyhim/awesome-claude-code
* **核心功能与技术特点**：这是目前整个开源社区中最为全面和优质的 Anthropic Claude Code 专属生态资源大合集。它收录了最顶尖的自定义 Skills、终端高亮状态栏样式、开发辅助脚本和各行业专属 Agents 模板。
* **主要技术栈和实现方式**：项目以 **Python** 相关的维护脚本为依托。本质是一个高度精选的信息枢纽，通过社区协作将零散的 Claude Code 生态资源结构化。
* **适用的应用场景**：适合所有希望对 Claude Code 进行深度定制、建立团队统一 AI 编码规范及开发流的资深技术人员。

### coreyhaines31/marketingskills
* **核心功能与技术特点**：marketingskills 是一套赋予 AI 编码 Agent（如 Claude Code）专业营销直觉的技能包。它能让研发助理在编码的同时，从 SEO（搜索引擎优化）、CRO（转化率优化）、文案说服力和增长黑客工程的角度对项目提出重构意见。
* **主要技术栈和实现方式**：主要基于 **JavaScript**。其架构通过精心设计的 prompt 指令集、行业经典转化公式和分析 API，将营销领域的最佳实践与代码生成层深度缝合。
* **适用的应用场景**：适合独立开发者（Indie Hackers）、初创团队、以及致力于提高落地页转化率和产品营销指标的增长技术团队（Growth Engineering）。

### JuliusBrussee/caveman
* **核心功能与技术特点**：Caveman 是一个主打极致极简主义的 Claude Code 效率技能。它通过驱使 AI 模仿“原始人（Caveman）”简短、无礼貌词、单刀直入的沟通风格（例如：“字少，事成”），在不损耗编码质量的前提下强行削减了 65% 的 Token 交互。
* **主要技术栈和实现方式**：该技能使用 **JavaScript** 编写。它拦截了 Claude Code 的输出规约提示词，通过高强度的正则及语义模板，将常规 LLM 的冗长套话直接过滤为极简格式。
* **适用的应用场景**：极度适合在命令行高频编码、饱受 LLM 啰嗦之苦，并且极度希望节省 API 账单和提升网络推断响应速度的硬核工程师。

### CoplayDev/unity-mcp
* **核心功能与技术特点**：unity-mcp 是一个利用 C# 编写的 Unity 编辑器深度集成桥梁。它严格遵循了最新的 **Model Context Protocol (模型上下文协议)**，将 Unity 编辑器的内部控制权向 LLM（大语言模型）完全暴露。
* **主要技术栈和实现方式**：采用 **C#** 开发，内置了 MCP 协议的服务端。AI 助手可以借此直接遍历 Unity 场景树、对 3D 资产进行重命名、自动编写并绑定 C# 游戏脚本，或者在编辑器中自动执行构建流程。
* **适用的应用场景**：非常适合游戏制作人、技术美术（TA）以及试图通过自然语言交互实现游戏关卡自动化搭建和剧本自动化的游戏工作室。

### facebook/astryx
* **核心功能与技术特点**：Astryx 是 Meta（Facebook）开源的一套完全可定制、专门面向 “AI Agent 友好（Agent-Ready）”设计的现代化 UI 设计系统。它不仅向人类开发者提供高质量的 UI 组件，更为 AI 自动生成界面和操控交互提供了完美支撑。
* **主要技术栈和实现方式**：基于 **TypeScript** 开发。它在标准的 React 组件上封装了高精度的 AI 可读元数据、语义化标记和无障碍访问标签，使得大模型在解析 DOM 以及用自然语言操控组件时绝不出错。
* **适用的应用场景**：适合正在构建 AI 辅助低代码/无代码开发平台（Low-Code）、需要生成多变的前端应用、或高度依赖 GUI Agent 执行自动操作的企业级研发团队。

### immich-app/immich
* **核心功能与技术特点**：Immich 是一款在自托管领域无可争议的、高性能开源照片与视频管理解决方案。它不仅功能上完美平替 Google Photos（支持手机端自动备份、多用户管理），在隐私保护上也做到了极致。
* **主要技术栈和实现方式**：项目使用 **TypeScript**（NestJS + Svelte）开发。其底层集成了先进的本地化 AI 模型，在本地即可快速完成高精度的面部识别、物品分类以及图像语义检索。
* **适用的应用场景**：广泛适用于有海量家庭照片存储需求、不愿承受云端高昂订阅费且对隐私安全要求极高的 HomeLab 用户与极客。

### ruvnet/RuView
* **核心功能与技术特点**：RuView 是一个极具颠覆性的边缘物理世界感知项目。它能够在没有任何摄像头或图像传感器介入的前提下，将普通的商品化 WiFi 路由信号转化为实时的空间智能，实现无摄像头的人员定位、多目标追踪、甚至是对胸腔起伏的微弱生命体征（呼吸、心率）监测。
* **主要技术栈和实现方式**：系统完全采用 **Rust** 构建。其核心底层是数字信号处理（DSP）算法，对 WiFi 信道状态信息（CSI，Channel State Information）进行多维度的解算与机器学习模型比对，确保无死角地捕捉物理波动。
* **适用的应用场景**：非常适合注重绝对隐私的居家老人健康监护、无视觉侵入的商超客流分析以及智能家居安防系统的构建。

### gastownhall/gastown
* **核心功能与技术特点**：Gas Town 是一款基于 Go 语言的多智能体工作空间管理器。它能够在单机或集群环境下，为并行的 AI Agent 创造高度隔离、可监控、可审计的沙箱运行容器。
* **主要技术栈和实现方式**：核心采用 **Go** 语言编写，利用 Go 协程和轻量级虚拟化/容器技术，对各个 Agent 拥有的文件目录、网络端口权限进行精细化隔离与并发调度。
* **适用的应用场景**：最适用于构建高安全性要求的云端 AI 协同研发系统、多智能体协同攻防或需要大规模安全并行推断的商用 Agent PaaS 平台。

### dotnet/skills
* **核心功能与技术特点**：这是微软官方为辅助各种主流 AI 编码 Agent（如 GitHub Copilot, Cursor, Claude Code 等）高效处理 .NET 生态而发布的专属技能和指令仓库。它集成了微软官方对现代化 C# 标准和大型项目架构的最佳实践。
* **主要技术栈和实现方式**：全部基于 **C#** 编写，内置了针对 .NET CLI 的自动化封装、依赖冲突自动排查脚本和项目依赖注入（DI）优化的特化指令集。
* **适用的应用场景**：非常适合进行企业级 C# 遗留系统迁移、复杂微服务架构改造的开发团队，能显著降低 AI 在生成 C# 代码时的逻辑漏洞和冗余度。

### OthmanAdi/planning-with-files
* **核心功能与技术特点**：planning-with-files 是一款为长周期、高失败率 AI 任务设计的“防灾”规划管理工具。它借鉴了前沿 AI Agent（如 Manus）的思路，采用物理文件的方式进行任务状态的持久化记录。
* **主要技术栈和实现方式**：利用 **Python** 实现。其核心理念是在磁盘上动态维护一个具有确定性门控机制（Completion Gate）的 Markdown 文件作为多智能体的共享记忆库。即使 Agent 的内存或上下文在运行中断（如网络抖动、重启、`/clear` 命令）时完全丢失，它也能够通过读取本地文件无缝恢复并继续工作。
* **适用的应用场景**：对于开发长达数小时甚至数天、包含复杂多智能体分工的离线自动化工程流的架构师来说，该项目是提供鲁棒性（Crash-proof）的必备架构级底座。

---

## 3. 今日趋势特点总结

1. **“技能包（Skills）”生态呈大爆发态势**：
   今日的榜单最瞩目的特点是多款“AI 技能仓库（Skills）”的刷榜（如 `claude-skills`、`marketingskills`、`caveman`、`dotnet/skills`）。这标志着开发者已经不满足于简单的 Chat-based 大模型交互，而是开始围绕 **Claude Code**、**Cursor** 等 CLI 编码代理，积极构建和分享高度特化、业务导向的工具包（涵盖营销、C# 重构、甚至是 Token 压缩技术）。
2. **边缘计算与端侧隐私成为“第二主战场”**：
   诸如 `meetily`（本地会议助手）、`RuView`（WiFi 空间智能监测）以及 `immich` 等项目的持续火爆，清晰地揭示了技术界对于“全云端 AI”带来的隐私泄露、延迟高、高带宽消耗和巨额云开销等问题的焦虑。利用 Rust 等低功耗高性能语言，在本地边缘端榨干 CPU/NPU 算力进行私有化推理，正在成为重要的技术分水岭。
3. **“Agent 运行保障技术”日益成熟**：
   随着 AI 逐步迈向具有复杂自主决策能力的长任务（Long-running Agentic Tasks），系统的容错机制和并发治理正走向前台。`planning-with-files` 采用物理文件持久化状态防止上下文丢失，以及 `gastown`、`herdr` 对多智能体多路复用和沙箱隔离的管理，共同表明：**如何让多个 Agent 安全、不崩溃、有条不紊地协同工作，已成为当前最前沿的软件架构命题。**