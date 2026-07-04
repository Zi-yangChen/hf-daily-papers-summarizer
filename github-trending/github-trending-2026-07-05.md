# GitHub Trending 每日自动总结报告 (2026-07-05)

## 1. Trending Top 18 表格

| 项目名称与链接 | 语言 | 总Star | 今日新增Star | 功能描述 |
| :--- | :--- | :--- | :--- | :--- |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | JavaScript | 24,247 | 716 | 在 Claude Code 中使用 Codex 进行代码审查或任务委派。 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | JavaScript | 83,844 | 1,089 | 通过类似“野人说话”的精简模式，为 Claude Code 削减达 65% 的 Token 消耗。 |
| [alibaba/page-agent](https://github.com/alibaba/page-agent) | TypeScript | 23,032 | 726 | 网页内嵌 GUI 智能体，允许使用自然语言控制和操作 Web 界面。 |
| [usestrix/strix](https://github.com/usestrix/strix) | Python | 35,921 | 1,910 | 开源 AI 渗透测试工具，可自动查找并修复应用程序中的漏洞。 |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TypeScript | 45,739 | 303 | 为编程智能体（Coding Agents）量身定制的 Chrome 开发者工具 MCP 服务器。 |
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Rust | 15,097 | 865 | 隐私优先的自托管 AI 会议助手，支持极速本地转录、发言人分离及本地 Ollama 总结。 |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JavaScript | 48,818 | 432 | 收集并持续更新各大主流大模型（如 Claude 5、GPT 5.5、Gemini 等）的系统提示词。 |
| [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | Python | 26,521 | 446 | 哈佛大学 Edge 实验室的《机器学习系统》（Machine Learning Systems）课程书籍仓库。 |
| [rommapp/romm](https://github.com/rommapp/romm) | Python | 10,156 | 400 | 界面美观、功能强大的自托管 ROM 游戏管理器及在线播放器。 |
| [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | Rust | 11,362 | 706 | 运行在终端环境下的 Agent 多路复用器。 |
| [dotnet/skills](https://github.com/dotnet/skills) | C# | 3,786 | 57 | 为 AI 编程智能体提供 .NET 和 C# 辅助技能的微软官方仓库。 |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | Python | 22,290 | 351 | 智能体技能（Agent Skills）的标准化规范与文档。 |
| [immich-app/immich](https://github.com/immich-app/immich) | TypeScript | 105,576 | 198 | 高性能自托管照片与视频管理解决方案。 |
| [chthollyphile/folia-major](https://github.com/chthollyphile/folia-major) | TypeScript | 975 | 319 | 专注于绚丽歌词动画效果的本地/第三方音乐播放器客户端。 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 156,482 | 1,013 | 资深工程师的高效技能集，直接提取自个人的 `.claude` 配置目录。 |
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | C# | 11,551 | 68 | 连接 AI 助手与 Unity 编辑器的 MCP 桥梁，可实现自动编辑脚本及场景控制。 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Python | 20,101 | 197 | 包含 337 个针对 Claude Code、Gemini 等编程智能体的跨领域自定义技能和插件。 |
| [crynta/terax-ai](https://github.com/crynta/terax-ai) | TypeScript | 8,024 | 44 | 体积仅 7MB 的终端原生 AI 开发工作空间。 |

---

## 2. 项目详细分析

### openai/codex-plugin-cc
* **核心功能与技术特点**：该项目是 OpenAI 官方推出的 Codex 插件，旨在无缝对接 Anthropic 的 Claude Code 终端助手。它通过桥接 Codex 的强大代码生成与 Claude Code 的自主执行能力，实现了跨生态的 AI 协同。
* **主要技术栈和实现方式**：项目基于 JavaScript 开发，通过标准化的接口调用与事件钩子，使 Claude Code 在运行过程中能够自由切换和调度后端 Codex 模型。
* **适用的应用场景**：其核心应用场景包括自动化的代码审查（Code Review）、复杂的重构任务委派以及多模型协作编程。这种强强联手的架构设计，能够有效提升生成代码的准确性并减少开发者的提示词编写负担。

### JuliusBrussee/caveman
* **核心功能与技术特点**：Caveman 是一个极具创意的 Claude Code 技能插件，其核心理念是“用最少的 Token 达到目的”。该项目通过精简的提示词工程（Prompt Engineering），指导 Claude 以“野人说话（Caveman）”的简化风格进行沟通。
* **主要技术栈和实现方式**：项目基于 JavaScript 构建，核心是一套极致压缩的信息模板。这种信息压缩技术在保证 AI 理解力和任务执行力不变的前提下，能够平均削减高达 65% 的 Token 消耗。
* **适用的应用场景**：在大模型按 Token 计费的背景下，它非常适合需要高频与 AI 交互、处理海量上下文或者预算有限的自动化开发与脚本编写场景。这不仅大幅降低了开发者的 API 使用成本，还显著提升了终端响应速度。

### alibaba/page-agent
* **核心功能与技术特点**：Page-Agent 是阿里巴巴开源的网页内 GUI 智能体（Agent），旨在让 AI 直接通过自然语言控制网页界面。它无需依赖繁重的后端视觉识别模型，直接通过 DOM 树解析和操作来实现控制。
* **主要技术栈和实现方式**：这是一个完全运行在浏览器页面内的 JavaScript/TypeScript 解决方案。它将用户的自然语言指令转化为点击、输入和滚动等具体的页面交互行为，具备高度的轻量化优势。
* **适用的应用场景**：这一技术在前端自动化测试、无障碍网页辅助访问以及复杂的网页自动化工作流中拥有广阔的应用前景。该项目为下一代“LLaMA-on-the-browser”交互模式提供了一个轻量且极具实用价值的范式。

### usestrix/strix
* **核心功能与技术特点**：Strix 是一款开源的 AI 渗透测试工具，致力于通过智能化手段自动发现并修复应用程序中的安全漏洞。它不仅能够检测已知风险，还能理解代码上下文逻辑并执行漏洞概念验证（PoC）。
* **主要技术栈和实现方式**：该系统采用 Python 语言构建，结合了先进的静态代码分析、动态执行环境测试以及大语言模型的逻辑推理能力。它能够自动生成漏洞利用 Payload 进行验证，并针对发现的安全隐患给出可直接合并的代码修复方案（Auto-remediation）。
* **适用的应用场景**：适用于 DevSecOps 流程中的自动化安全审计、企业软件发布前的合规性扫描以及红蓝对抗演练。它的出现降低了安全测试的门槛，帮助开发团队在早期阶段低成本地提升系统的整体防御力。

### ChromeDevTools/chrome-devtools-mcp
* **核心功能与技术特点**：这是一个由谷歌 Chrome DevTools 官方团队推出的模型上下文协议（MCP）服务器，专门为编程智能体（Coding Agents）设计。它允许 AI 助手通过 MCP 协议直接与 Chrome 浏览器的开发者工具进行深度的双向通信。
* **主要技术栈和实现方式**：项目使用 TypeScript 编写，利用 Chrome 调试协议（CDP）接口。通过该工具，AI 能够直接获取当前页面的控制台日志、调试网络请求、检查 DOM 元素乃至执行运行时性能分析。
* **适用的应用场景**：它是前端 AI 开发助手、自动化 UI 调试工具以及无头浏览器自动化测试方案的关键底层基础设施。它极大地拓宽了 AI 在 Web 开发生命周期中的操作边界，使智能体能够真正“看见”并“调试”网页。

### Zackriya-Solutions/meetily
* **核心功能与技术特点**：Meetily 是一款专注于隐私保护的自托管开源 AI 会议助手，支持 macOS 和 Windows 双平台。其最大特点是 100% 的本地化离线处理能力，彻底摆脱了云端服务的束缚，确保会议数据的安全与私密。
* **主要技术栈和实现方式**：该项目基于 Rust 语言构建，以确保极高的运行时性能和极低内存占用。内部集成了 Parakeet 和 Whisper 实现高精度的本地实时语音转文字，并搭载本地 Ollama 运行大模型进行会议摘要与发言人分离（Speaker Diarization）。
* **适用的应用场景**：它是政府、金融、医疗等对数据隐私要求极高的行业进行会议记录和机密讨论的理想工具。即便在完全断网的环境下依然能流畅运行，保证了极致的安全与高可靠性。

### asgeirtj/system_prompts_leaks
* **核心功能与技术特点**：该项目是一个备受瞩目的开源仓库，收集并持续更新来自各大主流商业 AI 模型的系统提示词（System Prompts）。它像是一个大模型安全防御与逻辑设定的“活化石库”。
* **主要技术栈和实现方式**：仓库主要使用 JavaScript 管理，通过逆向工程、越狱技术（Jailbreak）以及特定的提示词注入手法，提取出了包括 Claude 5、ChatGPT 5.5、Gemini 3.5 等前沿模型的内部设定。
* **适用的应用场景**：这对于提示词工程师、AI 安全研究员以及希望构建高水平 Agent 系统提示词的开发者来说，是极具参考价值的学习资源。它不仅揭示了顶级科技巨头对 AI 行为约束的黑盒内幕，也为研究 LLM 安全防护与指令遵循提供了宝贵的数据支持。

### harvard-edge/cs249r_book
* **核心功能与技术特点**：这是哈佛大学 Edge 实验室开源的《机器学习系统》（Machine Learning Systems）课程配套电子书和教学资源仓库。它重点探讨如何在资源受限的硬件和边缘端上高效运行先进的 AI 模型。
* **主要技术栈和实现方式**：该书主要采用 Python 语言进行代码示例，系统性地涵盖了模型量化、剪枝、硬件加速器适配以及大模型高效微调（PEFT）等前沿工程技术。
* **适用的应用场景**：它非常适合作为系统架构师、边缘端算法工程师以及高校研究人员深入学习 AI 系统底层工程实践的权威指南。该仓库弥补了学术界算法理论与工业界系统落地之间的鸿沟，极大地推动了边缘计算与人工智能的交叉融合。

### rommapp/romm
* **核心功能与技术特点**：RomM 是一款界面美观且功能强大的自托管复古游戏 ROM 资源管理器与在线播放器。它让复古游戏爱好者能够在一个集中的、高度可视化的 Web 平台中管理数以万计的游戏。
* **主要技术栈和实现方式**：该系统基于 Python 后端与现代化的 Web 前端技术构建，支持通过 Docker 容器化一键式快速部署。它能够自动扫描用户的 ROM 文件，匹配游戏元数据、封面海报，并集成了基于 WebGL 的浏览器内置模拟器。
* **适用的应用场景**：它适用于游戏收藏家和复古游戏爱好者，用于在 NAS（网络附加存储）或本地服务器上搭建属于自己的私有云游戏库。其多用户管理和跨平台游玩的特性，让玩家无需在多台设备上配置复杂的模拟器即可随时重温经典。

### ogulcancelik/herdr
* **核心功能与技术特点**：Herdr 是一款驻留在终端中的 Agent 多路复用器（Multiplexer），专注于提升开发者的多智能体协同效率。它允许用户将一个终端输入同时广播给多个处于本地或云端的 AI 智能体，并以直观的界面并行展示各自的输出结果。
* **主要技术栈和实现方式**：该工具采用 Rust 语言编写，具备极快的响应速度与高并发的处理能力。它通过高效的异步 I/O 架构来管理多个 LLM 的会话状态与数据流。
* **适用的应用场景**：主要适用于需要对不同 LLM（如 Claude、GPT、DeepSeek）的生成质量进行实时横向评测、或者组合多个专项 Agent 执行复杂任务的研发场景。通过 Herdr，开发者能够以极低的资源消耗在纯命令行环境中构建起强大的多智能体工作台。

### dotnet/skills
* **核心功能与技术特点**：这是微软官方推出的 .NET 技能仓库，专门用于增强 AI 编程智能体在 C# 和 .NET 生态中的开发能力。它为 AI 智能体注入了深度的平台级工程知识，使其不再仅仅依赖通用的语言常识。
* **主要技术栈和实现方式**：项目主要采用 C# 语言实现，包含了大量精心设计的可重用模块、上下文定义和 API 工具接口。这些技能模块能帮助 Copilot 或 Claude 等智能体深入理解 .NET 的设计模式、依赖注入规范以及最新的语法特性。
* **适用的应用场景**：适用于企业级 C# 项目的自动化重构、依赖项升级、代码生成以及 .NET 架构设计咨询。它为 AI 开发者树立了如何为垂直生态构建标准化 Agent Skills 的权威行业标杆。

### agentskills/agentskills
* **核心功能与技术特点**：Agent Skills 是一个开源的行业规范与文档库，旨在定义和标准化 AI 智能体所能使用的“技能（Skills）”格式。它的出现是为了解决当前各大 Agent 框架之间工具互不兼容、碎片化严重的问题。
* **主要技术栈和实现方式**：该项目主要基于 Python 开发，提供了一套通用的技能定义 Schema 和接口协议描述。通过规范化函数调用（Function Calling）和工具声明（Tool Declaration），它使不同的 AI 框架可以无缝共享和调用技能库。
* **适用的应用场景**：适用于多智能体框架的互操作性构建、企业内部私有工具库的抽象，以及开源 Agent 生态的工具集成。这一标准的推广有助于打破不同 AI 平台之间的壁垒，促进智能体应用生态走向规范化和模块化。

### immich-app/immich
* **核心功能与技术特点**：Immich 是一款极受欢迎的高性能开源自托管照片和视频管理解决方案，常被视为 Google Photos 的完美替代品。它以其惊人的更新频率和媲美一线商业产品的用户体验，在自托管社区中确立了无可替代的地位。
* **主要技术栈和实现方式**：该系统采用 TypeScript 开发，后端基于 Node.js，并融合了强大的机器学习引擎进行人脸识别、物体检测和智能多维检索。系统支持多用户隔离、手机端 App 自动后台备份以及流畅的 Web 交互界面。
* **适用的应用场景**：它是家庭 NAS 用户、个人摄影师和注重隐私的极客备份和展示数万张照片的首选方案。它能提供极其流畅的多媒体浏览体验，且数据完全掌控在用户自己手中。

### chthollyphile/folia-major
* **核心功能与技术特点**：Folia Major 是一款专注于绚丽歌词动画效果的本地及第三方网络音乐播放器。在同类自托管音频客户端中，该项目凭借其独特的视觉美学设计脱颖而出。
* **主要技术栈和实现方式**：它使用 TypeScript 开发，深度集成了 Navidrome 及第三方网易云音乐接口，支持多数据源无缝切换。其核心亮点在于利用现代 WebGL 与 CSS 动画技术，打造出了令人惊叹且流畅动感的逐字歌词视觉效果。
* **适用的应用场景**：适合音乐爱好者、极客用户以及对播放器界面美观度和歌词动效有极致追求的用户群。它将传统的音频播放提升为了听觉与视觉的双重享受。

### mattpocock/skills
* **核心功能与技术特点**：该项目是知名开发者 Matt Pocock 开源的个人 Claude 助手技能集，直接提取自其生产环境中的 `.claude` 目录。它是开发领域高度定制化、实战化的 AI 辅助工具范本。
* **主要技术栈和实现方式**：项目主要依托 Shell 脚本和高效的配置文件构建，用于在终端环境中扩展 Claude Code 的命令级功能。它包含了一系列针对现代化 TypeScript/JavaScript 工程研发、测试自动化和依赖重构的实用自动化指令。
* **适用的应用场景**：适用于追求极致效率的前端与全栈开发人员，能大幅缩短日常重复性 Git 提交、重构与测试指令的编写耗时。该项目的分享为开发者如何定制专属的本地 AI 智能体工作流提供了非常实用的、来自实战的样板。

### CoplayDev/unity-mcp
* **核心功能与技术特点**：Unity MCP 是一款连接 AI 智能体（如 Claude Code 等）与 Unity 编辑器的创新桥梁工具。该项目标志着 AI 智能体正式深入到 3D 游戏引擎的开发内部，为“AI 辅助游戏设计”开启了全新可能。
* **主要技术栈和实现方式**：基于 C# 语言实现，并遵循了最新的模型上下文协议（MCP，Model Context Protocol）。它为大语言模型赋予了操作 Unity 资产、场景控制、脚本编辑以及编辑器内任务自动化的特权。
* **适用的应用场景**：非常适合游戏开发团队进行快速原型制作、场景自动生成、自动化关卡测试以及基于 AI 的资产管道管理。它极大地降低了游戏开发的上手难度和繁琐的重复性工作量。

### alirezarezvani/claude-skills
* **核心功能与技术特点**：该项目是一个超大规模的 AI 智能体技能大礼包，集成了多达 337 个针对 Claude Code 及其他主流编程智能体的插件与指令。它是目前开源社区中覆盖面最广、实用性极强的跨领域智能体赋能工具箱之一。
* **主要技术栈和实现方式**：主要使用 Python 编写，提供了 30 多个专用角色智能体、70 多个自定义终端命令以及 330 多个预设技能模块。不仅涵盖了软件工程与代码重构，还跨界扩展到了市场营销、合规性审计、高管咨询（C-level）及日常行政工作。
* **适用的应用场景**：无论是寻找快速开发工具的程序员，还是需要多岗位 AI 虚拟助手的跨职能团队，都能从中获益。用户可以根据业务需求自定义和组合这些技能模块，以极速组建各种领域的虚拟专家团队。

### crynta/terax-ai
* **核心功能与技术特点**：Terax-AI 是一款体积极其小巧（仅约 7MB）、以终端为中心且原生支持 AI 的现代化开发工作空间。它旨在提供一个不逊于大型 IDE 的、极度专注且高效的命令行式 AI 编程环境。
* **主要技术栈和实现方式**：项目采用 TypeScript 开发，针对终端环境进行了深度剪裁与运行效率优化。它省去了繁杂的 GUI 框架，在超轻量级的身躯内无缝集成了本地智能代码补全、命令预测以及多语言编译器环境。
* **适用的应用场景**：特别适合在低配置服务器、SSH 远程开发连接、便携式单板电脑（如树莓派）等资源受限的终端场景下使用。该项目展示了如何以最极简的工程设计，让老旧硬件和命令行环境瞬间具备先进的 AI 开发体验。

---

## 3. 今日趋势特点总结

*   **智能体技能规范与 MCP 协议全面爆发**
    今日 trending 榜单中，以 `ChromeDevTools/chrome-devtools-mcp`、`dotnet/skills`、`CoplayDev/unity-mcp` 及 `agentskills` 为代表的“AI 智能体技能”及 MCP（Model Context Protocol）协议相关的项目占据了绝对的主导地位。这表明 AI 正在从单纯的“问答助手”向能够调用专业工具（如 Chrome、Unity 编译器等）、理解垂直领域语境（.NET）的“行动派智能体”加速演进，行业正合力确立统一的智能体技能接口规范。

*   **终端原生与极简化工作流备受推崇**
    以 `crynta/terax-ai` (7MB 超轻量工作区)、`ogulcancelik/herdr` (终端多路复用器) 为代表的终端 AI 交互工具迅速走红，反映了高级开发者对于重型 GUI 编辑器的审美疲劳。他们更偏爱在命令行、SSH 等极简环境中，通过高度定制化、低延迟的终端工作流与大模型交互。

*   **本地化、隐私保护与 Token 成本控制成为刚需**
    从 100% 离线运行的会议助手 `Zackriya-Solutions/meetily`，到通过“野人说话”狂砍 65% token 的 `JuliusBrussee/caveman`，开发者们正在采取务实的态度应对大模型的高昂 API 成本与潜在的数据泄露风险。如何在保护隐私的前提下，通过极致的提示词压缩或完全本地化的轻量级模型部署来实现生产力工具落地，已成为当下的核心研究方向。