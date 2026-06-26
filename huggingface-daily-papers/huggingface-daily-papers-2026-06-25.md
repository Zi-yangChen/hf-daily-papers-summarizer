您好！我是 AI 研究专家。以下是针对 2026 年 6 月 25 日 Hugging Face Daily Papers 论文列表中点赞数靠前的重点论文进行的专业解读和中文总结：

---

### 今日整体研究趋势总结
1. **智能体（Agent）系统的深度审视与重构**：今天的多篇高赞论文聚焦于智能体底层系统，从世界模型环境模拟、原子化记忆评估，到防止自演进陷入“自我确认陷阱”的机制，均体现了业界正从简单的“提示词工程”向更稳健的系统工程与认知架构演进。
2. **多模态与流式实时交互的崛起**：端到端流式基础模型（如 Wan-Streamer）的出现打破了传统 ASR-LLM-TTS 的模块拼接，将多模态实时低延迟交互推向了全新高度。
3. **更具挑战性与可复现性的评估基准**：研究人员开始对现有的单一评估基准（如 DiT 领域的 ImageNet 刷榜）提出质疑，并推出了涉及多模态代码智能、科学文献复现、真实手机 GUI 交互以及精神科医学诊断等垂直、高门槛的综合性新基准。

---

### 重点论文深入剖析

#### 1. **Qwen-AgentWorld: Language World Models for General Agents**
*   **论文链接**: [https://huggingface.co/papers/2606.24597](https://huggingface.co/papers/2606.24597)
*   **研究机构/作者**: Qwen 团队 (An Yang, Dayiheng Liu, Jingren Zhou, Ning Ding 等)
*   **核心痛点与创新点**：传统的智能体训练和强化学习通常极度依赖真实的物理环境或高昂的手工规则模拟器，不仅难以泛化，也无法实现规模化扩展。这篇论文研究了如何使用大语言模型构建通用智能体环境模拟的“语言世界模型”。作者推出了 Qwen-AgentWorld（35B和397B），这是首个能通过长思维链推理模拟 7 个领域智能体环境的语言世界模型。它利用超过 1000 万条真实交互轨迹，通过持续预训练（CPT）注入状态转换动力学，通过监督微调（SFT）激活下一步预测推理，并利用强化学习（RL）通过混合细则与规则奖励提高模拟保真度。该模型既能作为解耦的模拟器支持数千个环境的规模化强化学习，其世界模型训练还可以作为非常有效的预热（warm-up）手段，提升下游 Agent 的泛化能力。
*   **潜在影响力**：为实现不依赖高成本实体或特定软件环境的“模拟器内强化学习（RL in Sim）”提供了一条可行道路，证明了用大语言模型模拟世界的深度，将推动通用 Agent 的无实体协同演进。

#### 2. **NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?**
*   **论文链接**: [https://huggingface.co/papers/2606.24530](https://huggingface.co/papers/2606.24530)
*   **研究机构/作者**: Frontis AI / 清华大学等 (Yuru Wang, Ning Ding, Bowen Zhou, Kaiyan Zhang 等)
*   **核心痛点与创新点**：现有的智能体科学研究基准通常局限于简单的代码复制，且面临严重的“环境碎片化”问题，难以准确评估 Agent 在面对真实、未知科学问题时的自主发现能力。为此，本文推出了 NatureBench，一个包含 90 个跨学科科学任务的挑战性基准，所有任务均提炼自同行评审的《自然》（Nature）子刊论文。同时，开发了自动流水线 NatureGym，从源论文直接构建标准化的容器环境，保障了评测的复现可信度。在严格禁止联网检索的协议下，评估发现目前最强的 Agent 配置也仅能在 17.8% 的任务中超越人类 SOTA。分析表明，目前的 Agent 主要通过将复杂的科学问题转译为熟悉的“监督预测任务”来取得进展，而非进行真正的科学发现。
*   **潜在影响力**：提出了一个具有极高门槛和环境信度的科学智能体评估基准，为 Agent 迈向“AI 科学家”提供了精准的定量诊断，有助于引导未来的科学智能体设计。

#### 3. **DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation**
*   **论文链接**: [https://huggingface.co/papers/2606.26058](https://huggingface.co/papers/2606.26058)
*   **研究机构/作者**: 香港科技大学 C4G 团队 (Nan Chen, Yiyang Cai, Rongchang Xie, Junwen Pan 等)
*   **核心痛点与创新点**：开放域主体驱动的文本生成视频（S2V）在“保持参考主体特征不变”（域内场景）与“允许主体无关属性跟随提示词灵活变化”（跨域场景）之间存在难以调和的矛盾。现有方法大多过度关注域内特征复现，导致模型在跨域编辑（如新风格、特殊动作）时的灵活性严重受限。本文提出 DomainShuttle 框架，旨在使视频 personalization 能够在这两个场景之间自如穿梭。其核心设计包括 Domain-MoT 机制（解耦视频与参考特征，引入领域感知的 AdaLN 对参考图像进行特定建模）和 Video-Reference DualRoPE 方案（将参考图像 Token 和视频 Token 放置在独立的旋转位置编码空间中）。此外，引入跨对一致性损失（Cross-Pair Consistent Loss），用以提取不受无关环境特征干扰的本征主体特征。
*   **潜在影响力**：拓宽了视频个性化生成的应用边界，使高保真主体特征与高自由度艺术风格、场景、动作编辑能够共存，将促进数字人创意生成和广告营销等领域的落地。

#### 4. **Are We Ready For An Agent-Native Memory System?**
*   **论文链接**: [https://huggingface.co/papers/2606.24775](https://huggingface.co/papers/2606.24775)
*   **研究机构/作者**: 上海交通大学 (Wei Zhou, Xuanhe Zhou, Shaokun Han, Guoliang Li 等)
*   **核心痛点与创新点**：大语言模型智能体的记忆系统已从简单的检索增强进化为复杂的“非结构化数据管理系统”，支持存储、检索、更新和长期整合。然而，现有的评估通常只通过端到端任务成功率（如 F1、BLEU）来粗放衡量，使得底层的记忆系统被当作一个不可拆解的黑盒。对此，本文从数据管理的视角对智能体记忆进行了系统性实验研究。作者提出了一个分析框架，将智能体记忆拆解为：表示与存储、提取、检索与路由、以及维护四大核心模块。在该框架下，评估了 12 个代表性开源记忆系统及 2 个基线在 5 个工作负载、11 个数据集上的表现。研究发现没有单一架构能在所有场景称霸，效果高度依赖于记忆结构与工作负载瓶颈的契合度。
*   **潜在影响力**：规范了智能体记忆系统的模块化设计与评估准则，揭示了性能与运行成本之间的权衡，为构建真正“智能体原生”的高效数据管理系统指明了发展方向。

#### 5. **MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical Feedback-Guided Policy Optimization**
*   **论文链接**: [https://huggingface.co/papers/2606.19930](https://huggingface.co/papers/2606.19930)
*   **研究机构/作者**: 快手 AI 团队 (Guangyi Liu, Pengxiang Zhao, Gao Wu, Yiwen Yin, Mading Li 等)
*   **核心痛点与创新点**：将多模态大模型适配到真实且海量的手机 App 时，面临巨大的人工标注成本，因为移动应用种类繁多且更新频繁，人工难以覆盖所有场景。已有的免标注 GUI 学习法缺乏一个能将目标应用探索、课程挖掘、轨迹执行和反馈整合的统一框架，且粗粒度轨迹奖励无法提供精准的策略优化梯度。本文提出了 MobileForge，一个免标注的移动 GUI 智能体适应系统。它包含在真实应用交互中进行任务生成和评估的 MobileGym，以及分层反馈引导策略优化（HiFPO）。HiFPO 将轨迹结果、步骤级过程反馈和纠错提示转化为提示上下文相关的步骤级 GRPO（群体相对策略优化）更新，大幅提升了模型的学习效率。
*   **潜在影响力**：极大降低了手机 GUI 智能体对人工标注数据的依赖，其自动化在线进化机制和精细的过程反馈设计，为智能体自动适配多变软件环境铺平了道路。

#### 6. **MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management**
*   **论文链接**: [https://huggingface.co/papers/2606.19926](https://huggingface.co/papers/2606.19926)
*   **研究机构/作者**: 快手 AI 团队 (Guangyi Liu, Gao Wu, Congxiao Liu, Pengxiang Zhao 等)
*   **核心痛点与创新点**：现有的移动端多模态 GUI 智能体通常使用 ReAct 风格的提示，被动地累积每一步的历史交互记录。在需要跨 App 导航的长程任务中，这种方式会导致提示词长度发生“爆炸”，并且会稀释或丢失关键的中间事实。为解决这一瓶颈，本文引入了具有主动上下文管理能力的端到端手机 GUI 智能体 MemGUI-Agent。该方法的核心是“上下文即动作”（Context-as-Action, ConAct）机制，将上下文管理作为策略输出的首类动作，与 UI 操作动作并列输出。ConAct 会主动维护、折叠并精简三个结构化上下文区域（折叠动作历史、折叠 UI 状态和最近步骤记录），确保在上下文极简的前提下留存核心交互事实。
*   **潜在影响力**：为长文本、长推理链的多模态交互式任务提供了一种精细化的上下文修剪与主动记忆维持范式，有效减少了长程推理中的计算和存储开销。

#### 7. **OpenThoughts-Agent: Data Recipes for Agentic Models**
*   **论文链接**: [https://huggingface.co/papers/2606.24855](https://huggingface.co/papers/2606.24855)
*   **研究机构/作者**: OpenThoughts 团队 (Negin Raoof, Richard Zhuang, Marianna Nezhurina, Benjamin Feuer, Ludwig Schmidt 等)
*   **核心痛点与创新点**：智能体大语言模型极大地扩展了 AI 应用，但目前学术界和工业界对如何策划训练数据以培养通用、跨领域的智能体依然知之甚少。现有的一些开源努力往往仅针对单一基准或任务进行优化。为此，OpenThoughts-Agent（OT-Agent）项目推出了一套完全开源的数据策划流水线。作者进行了 100 多项控制消融实验，系统性地探究了任务来源、多样性在训练每个阶段对泛化能力的影响。他们据此组装了一个包含 10 万条高质量样本的训练集，并对 Qwen3-32B 进行微调。该模型在 7 个不同的智能体基准上取得了 44.8% 的平均准确率，相较于先前最强的同尺寸开源模型提升了 3.9 个百分点。
*   **潜在影响力**：填补了通用智能体微调阶段高质量“数据配方”的开源空白，其表现出极强的扩展律（Scaling Law）特征，将显著规范并加速开源社区在 Agent 领域的对齐与预训练。

#### 8. **Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models**
*   **论文链接**: [https://huggingface.co/papers/2606.25041](https://huggingface.co/papers/2606.25041)
*   **研究机构/作者**: Wan-AI 团队 (Lianghua Huang, Zhifan Wu, Baole Ai, Chen Liang 等)
*   **核心痛点与创新点**：传统多模态交互系统多采用级联架构，将语音活动检测（VAD）、语音识别（ASR）、语言模型、语音合成（TTS）以及视频生成等多个独立模块拼接在一起。这种做法由于跨模块传递，不仅累积了极大的系统延迟，还容易发生模态间误差放大与音视频同步失真。本文推出了 Wan-Streamer，一个原生支持流式输入输出的端到端交互基础模型。它在单个统一的 Transformer 内将文本、音频和视频无缝建模为交错的 Token 流，并使用块因果注意力（block-causal attention）进行增量式的流式计算。感知、推理、表达、语速管理和多模态同步均在此模型内联合学习，彻底摆脱了对外部任何级联模块的依赖，并设计了低延迟多模态 Token 调度，使流式单元缩短至 160ms，模型端响应延迟低至 200ms。
*   **潜在影响力**：为真正自然、低延迟的人机协作开辟了端到端流式基础模型的新方向，展示了如何大幅降低复杂多模态实时交互系统的延迟壁垒。

#### 9. **ShutterMuse: Capture-Time Photography Guidance with MLLMs**
*   **论文链接**: [https://huggingface.co/papers/2606.25763](https://huggingface.co/papers/2606.25763)
*   **研究机构/作者**: 华中科技大学等 (Jiayu Li, Yixiao Fang, Tianyu Hu, Xingjun Ma 等)
*   **核心痛点与创新点**：现实世界中的人像和风景摄影通常需要“拍摄时”对相机取景（构图）和被摄主体动作（姿态）进行实时交互引导。然而，现有的美学裁剪基准侧重于“拍摄后”的后期剪裁预测，忽视了对主体动作姿态的推荐，也使得多模态大语言模型（MLLMs）在拍摄前期的实时辅助能力未得到探索。为此，本文推出了 CaptureGuide-Bench 评估基准，覆盖摄影师端的构图决策与细化定位，以及主体端的场景自适应姿态推荐。基于此，构建了包含 13 万高质量样本（带有文本合理解释和结构化视觉标注）的 CaptureGuide-Dataset，并基于监督微调和强化学习微调训练了摄影助手模型 ShutterMuse，支持提供精准裁剪框、构图决策以及具操作性的姿态建议。
*   **潜在影响力**：将多模态大模型从“后置”的图像编辑和分析，推向了“前置”的交互式拍摄辅助，为智能相机、创意人像摄影等消费级硬件与应用开辟了新赛道。

#### 10. **AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction**
*   **论文链接**: [https://huggingface.co/papers/2606.23449](https://huggingface.co/papers/2606.23449)
*   **研究机构/作者**: 清华大学 AIR 团队等 (Shanhui Zhao, Jiacheng Liu, Yuanchun Li, Ya-Qin Zhang 等)
*   **核心痛点与创新点**：现有的绝大多数终端操作系统均是围绕“应用中心”而非“智能体中心”设计的，缺乏对 AI Agent 的底层支持。这种错配导致 Agent 在传统系统上运行时，往往面临巨大的执行开销、安全策略冲突以及权限溢出等隐患。为了向学术界提供一个智能体原生操作系统机制探索的开源试验床，作者推出了 AOHP（Android Open Harness Project）。AOHP 基于 AOSP（安卓开源项目）构建，将 Agent 视为操作系统的“一等公民”，使其能够深度介入自适应用户界面和智能体运行环境。该框架在保留安卓软硬件生态的前提下，引入了个性化服务组合、高效智能体系统接口及安全信息流保障机制。实验表明，AOHP 在复杂任务上大幅提升了任务完成率（+21.12%），节省了 51.55% 的 Token 开销，并显著提高了安全合规性。
*   **潜在影响力**：为迈向“智能体原生操作系统（Agent-OS）”迈出了坚实的开源一步，为未来人机协同交互和移动平台安全架构提供了重要参考。

#### 11. **Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence**
*   **论文链接**: [https://huggingface.co/papers/2606.15932](https://huggingface.co/papers/2606.15932)
*   **研究机构/作者**: 武汉大学、浙江大学等 (Xuanle Zhao, Qiushi Sun, Jingyu Xiao, Zhixiong Zeng 等)
*   **核心痛点与创新点**：尽管大语言模型提升了文本到代码的生成（NL2Code）能力，但在真实的编程任务中，开发者往往通过截图、草图、流程图或交互视频等视觉元素表达意图。多模态代码智能（Multimodal Code Intelligence）应运而生，它要求模型建立视觉感知与可执行程序之间的连接。本文对这一新兴领域进行了系统而深入的调研。作者根据代码在任务中扮演的角色对该领域进行了重新表述，区分了代码作为渲染工件、可编辑符号结构、科学表示、中间推理痕迹或可执行策略/工具接口的不同功能。论文将基准和方法分门别类整理成四大块：图形用户界面、科学可视化、结构化图形和前沿任务，同时深入探讨了当前研究由于仅靠“单次输出模仿”带来的局限，并提出了四种以“验证（verification）为中心”的未来发展方向。
*   **潜在影响力**：这是一篇奠定领域理论框架的综述，理清了多模态代码生成的任务脉络，为之后更注重执行验证、多状态回溯的多模态AI编码系统开发指明了路线。

#### 12. **LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis**
*   **论文链接**: [https://huggingface.co/papers/2602.09379](https://huggingface.co/papers/2602.09379)
*   **研究机构/作者**: Lyncia 团队等 (Shihao Xu, Tiancheng Zhou, Yafeng Deng 等)
*   **核心痛点与创新点**：精神障碍的诊疗因缺乏主观访谈标准和精神科医生严重短缺而面临巨大壁垒。现有的医疗AI评估缺乏真实的患者模拟、临床验证的诊断标签，且无法支持动态的多轮 consultation 交互。为了解决这一痛点，本文提出了中文精神医学问诊与诊断大模型多智能体基准框架 LingxiDiagBench。该框架的核心是 LingxiDiag-16K，包含16,000个与真实病历（EMR）一致的合成问诊对话，复现了12种 ICD-10 精神疾病类别的临床与人口学分布。实验发现：（1) 尽管大模型在抑郁/焦虑二分类上表现优异（达92.3%），但在抑郁-焦虑共病识别和12类鉴别诊断中的表现急剧下降；（2）动态交互问诊的效果往往差于静态评估，说明大模型因缺乏有效的信息搜集策略而严重损害了其下游诊断推理能力。
*   **潜在影响力**：规范了AI在高度敏感和复杂的精神医学场景下的评估方法，强调了“边问边诊”的动态探索能力建设，对未来精神科辅助诊疗系统的开发具有里程碑意义。

#### 13. **Critique of Agent Model**
*   **论文链接**: [https://huggingface.co/papers/2606.23991](https://huggingface.co/papers/2606.23991)
*   **研究机构/作者**: SAILING Lab (CMU & MBZUAI - Eric Xing, Mingkai Deng, Jinyu Hou)
*   **核心痛点与创新点**：随着智能体在市场上的大行其道，明确“自动化”的终点与“能动性（agency）”的起点成为当务之急，这对安全防范和高能系统开发都十分关键。本文对AI智能体（Agent）和能动性进行了深刻的哲学和架构层面的审视。作者将智能体架构解剖为五个维度：目标、身份、决策、自我调节和学习。他们提出一个核心论点：真正的能动性（Agency）要求这些系统结构内生于系统内部，而非通过外部的硬编码或工作流脚手架（scaffolding）进行拼凑。这就将 competence 源自工程工作流的“agentic”系统与 capabilities 自发涌现的真正自治“agentive”系统区分开来。在此基础上，作者提出了面向通用智能体模型的 GIC（目标-身份-配置器）架构，整合了层级目标拆解、身份演进、基于独立训练世界模型的模拟推理，以及自我调节和自导向学习。
*   **潜在影响力**：为智能体理论研究注入了坚实的框架和哲学底蕴，清晰定义了“工程智能体”与“真正自治智能体”的区别，为高阶可控性、安全审计提供了底层支撑。

#### 14. **Semantic Browsing: Controllable Diversity for Image Generation**
*   **论文链接**: [https://huggingface.co/papers/2606.23679](https://huggingface.co/papers/2606.23679)
*   **研究机构/作者**: 希伯来大学等 (Sara Dorfman, Maya Vishnevsky, Daniel Cohen-Or 等)
*   **核心痛点与创新点**：现代文本生成图像模型在生成保真度和提示词遵循上表现卓越，但严苛的遵循限制了生成结果的多样性，导致输出往往坍缩到单一的视觉解释。现有的多样性生成方法主要依赖无规律的随机扰动（如改变噪声种子），无法提供符合用户设计直觉、结构化的变体选项。本文引入了“语义浏览”（Semantic Browsing）的概念，即允许用户通过系统化地穿越有意义、可解释的变异轴线来浏览结构化画廊。为了达成这种语义控制，作者利用了现代图像生成模型在精细化文本（elaborated captions）上训练的特点，将语义决策与像素生成解耦，在“文本级别”直接引入多样性。他们利用大语言/多模态模型操作全局场景上下文，并借助专门的智能体工作流，针对原始提示词强制输出具有结构化语义差异的多种描述语，再输入生成模型中。
*   **潜在影响力**：改变了单纯依赖随机种子的图像生成多样性控制方式，赋予用户在精细、可预测的设计空间中进行交互探索的能力，对创意设计和艺术创作工具的开发有极佳的实用参考价值。

#### 15. **FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation**
*   **论文链接**: [https://huggingface.co/papers/2606.24876](https://huggingface.co/papers/2606.24876)
*   **研究机构/作者**: Google 团队 (Orest Kupyn, Goutam Bhat, Christian Rupprecht, Federico Tombari 等)
*   **核心痛点与创新点**：尽管视频扩散模型可以在潜在空间内隐式编码多视角的几何结构，但现有的前向潜空间三维解码器通常只生成体素化的三维高斯点云，缺乏定义良好的三维表面，这限制了它们在仿真或标准图形管线中的进一步应用。为了直接解码出更贴近显式几何资产的表面对齐图元，本文首次提出了 FLAT 框架，展示了直接从视频扩散模型的隐变量中解码出三角形亮片（triangle splats）的可行性。预测扁平的三角形图元需要面对方向敏感、梯度流差等痛点。FLAT 采用了两个核心设计：（1）一种以射线为中心的三角形回归旋转参数化方法，（2）一种新颖的乘积窗口函数，用于提高可微分三角形渲染过程中的梯度流。通过将预测的“三角形汤（triangle soup）”进行轻量级测试时细化，可转化为游戏引擎可直接读取的全不透明渲染资源。
*   **潜在影响力**：填补了前向多视角扩散模型与工业级三角网格（Mesh）渲染管线之间的鸿沟，为快速、几何上高度精准的3D场景合成提供了一条崭新的通路。

#### 16. **IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation**
*   **论文链接**: [https://huggingface.co/papers/2606.24849](https://huggingface.co/papers/2606.24849)
*   **研究机构/作者**: 蚂蚁集团等 (Zixuan Li, Haokun Lin, Zhiwei Li, Zhenan Sun 等)
*   **核心痛点与创新点**：尽管统一的多模态大模型能产生极高质量的图像，但在需要细致对齐的结构感知任务（如指定物体的精确数量、复杂的空间关系、特定的属性绑定以及粗糙布局控制）上依然容易出错。作者将此限制归因于图像生成的“结构规划”和“外观渲染”在一个单一的条件流中过于纠缠。为此，论文提出了隐式视觉思维链（IV-CoT），一个用于查询条件图像生成的潜在空间视觉推理框架。IV-CoT 将视觉条件查询解耦为“结构到语义”的级联过程，由结构查询首先在潜在空间绘制视觉规划，再由语义查询在该规划指引下渲染外观细节。为了引导结构查询，模型引入了“仅训练阶段使用”的简笔画草图（sketch）监督，使其在推理阶段无需草图输入或中间解码即可捕获物理结构，只需一次前向传播便可隐式完成视觉CoT推理。
*   **潜在影响力**：提供了一种轻量且高效的层次化生成控制策略，无需在推理时增加额外的提示或复杂的二阶段解码结构，有效改善了多模态模型在复杂图像生成时的可控性。

#### 17. **DiffusionBench: On Holistic Evaluation of Diffusion Transformers**
*   **论文链接**: [https://huggingface.co/papers/2606.24888](https://huggingface.co/papers/2606.24888)
*   **研究机构/作者**: 澳大利亚国立大学等 (Xingjian Leng, Jaskirat Singh, Liang Zheng 等)
*   **核心痛点与创新点**：目前针对扩散变形器（DiT）的研究过度偏向一个非常局限的评估设置，即 ImageNet 上的类别条件图像生成。这种在单一闭环上的优化无法保证方法能在更为实用的文本生成图像（T2I）任务中带来等量提升，但传统的 T2I 评估往往因训练和评测成本过高而被忽视。本文推出了 NanoGen，一个统一的 DiT 训练与评估框架，能用极简的代码在 ImageNet 分类生成和 T2I 任务之间自如切换，且训练算力成本控制在相近量级。通过在同一框架下系统训练21个潜空间扩散模型，作者观察到一个惊人的现象：方法在 ImageNet 条件生成与在 T2I 上的表现排名并不具有正相关性，皮尔逊相关系数处于 -0.377 至 -0.580 之间，表明只看 ImageNet 指标往往会产生误导。基于此，作者整合并推出了 DiffusionBench，一个同时覆盖 ImageNet 与 T2I 生成的多视角DiT评估基准。
*   **潜在影响力**：纠正了DiT学术界盲目在 ImageNet 单一榜单刷榜的系统偏见，为更真实、更具实用参考价值的图像生成算法评测提供了一套全面而标准化的衡量工具。

#### 18. **FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs**
*   **论文链接**: [https://huggingface.co/papers/2606.22875](https://huggingface.co/papers/2606.22875)
*   **研究机构/作者**: 浙江大学 (Wenlong Cheng, Yuan Gan, Yunqiu Xu, Jiaxu Miao)
*   **核心痛点与创新点**：在联邦学习中训练潜空间扩散模型（LDM）极富隐私保障，但因为全局模型需要共享给多个参与客户端，面临着恶意客户非法分发或转售模型的版权威胁。现有的 LDM 水印技术在联邦场景下存在两个根本痛点：首先，现有方法能验证所有权却无法追踪具体是哪一个客户端发生了泄漏；其次，基于 VAE 解码器的水印非常脆弱，恶意攻击者只需更换一个未受污染的全新 VAE 解码器即可洗掉水印。为了克服上述挑战，本文提出了第一个针对联邦 LDM 拥有权验证和泄漏追踪的框架 FedOT。FedOT 设计了分块水印系统，将水印的第一部分用于确认拥有权，第二部分包含特异性编码以识别特定客户端。同时，引入潜向量变换（LVT）机制来强化 VAE 和 U-Net 潜在空间之间的耦合，通过人为调校 VAE 潜在分布，任何通过“替换 VAE 规避水印”的尝试都会导致生成质量崩溃，让模型彻底失效。
*   **潜在影响力**：为分布式/联邦大模型生态中的数字版权保护提供了高鲁棒性、可溯源的物理防护机制，解决了长期以来水印极易被下游解码器替换攻击消解的重大安全漏洞。

#### 19. **EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies**
*   **论文链接**: [https://huggingface.co/papers/2606.18239](https://huggingface.co/papers/2606.18239)
*   **研究机构/作者**: InternRobotics / 上海人工智能实验室等 (Hanqing Wang, Jiangmiao Pang, Chunhua Shen 等)
*   **核心痛点与创新点**：评估通用移动操作（Mobile Manipulation）策略以往多依靠单一成功率数值，难以深入诊断模型在具体细分维度上的表现和短板，导致研究人员无法精准地迭代策略。为此，本文推出了 EBench，一个在仿真环境中诊断通用移动操作策略的多维度评估基准。EBench 包含了 26 个具有挑战性且多样的操作任务，涵盖 5 个基础能力维度和 4 个泛化能力维度。作者对包括 $\pi_0$、$\pi_{0.5}$、XVLA 和 InternVLA-A1 在内的先进通用模型进行了评测。评估揭示了虽然各模型在最终成功率上很相近，但它们展现了截然不同的能力特质：$\pi_{0.5}$ 具有最高的泛化测试成功率和最好的保留能力；InternVLA-A1 称霸于大范围移动操作，但在精细灵巧操作上会发生崩溃；而 XVLA 则在与其他模型完全互补的原子技能上表现优异。
*   **潜在影响力**：打破了以往具身智能策略评价中“以成败论英雄”的黑盒视角，提供了一种更精细、像“雷达图”一样的能力诊断工具，能显著指导未来多模态动作模型在灵巧和移动操作技能上的平衡训练。

#### 20. **Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning**
*   **论文链接**: [https://huggingface.co/papers/2606.24428](https://huggingface.co/papers/2606.24428)
*   **研究机构/作者**: 浙江大学 (Shiding Zhu, Yajie Wang, Kai Zhang 等)
*   **核心痛点与创新点**：经验驱动的自进化对 AI Agent 持续提高开放域表现至关重要，但当前的自学习方法大多在一个单智能体的闭环中运行（执行、总结、存入记忆都由同一个智能体处理）。这使得 Agent 极其容易陷入“自我确认陷阱（Self-Confirmation Trap）”：当智能体生成了虽然错误但自圆其说的交互轨迹时，会误认为这是成功经验并将其固化为记忆，进而在未来的检索和使用中造成错误累积。为解决这一痛点，本文提出了 EDV，一个专为构建可靠经验自进化而设计的“执行-蒸馏-验证”框架。在“执行”阶段，多个异构执行智能体并行探索相同任务，生成多样的候选轨迹；在“蒸馏”阶段，由一个独立的第三方智能体对比分析各轨迹，生成候选经验包以减少执行者自身的总结偏差；在“验证”阶段，执行组通过共识机制核实经验，只有经过合议批准的干净经验才会被写入共享或私有记忆。
*   **潜在影响力**：极大地提高了 Agent 自我反馈学习机制的安全边界与抗噪能力，避免了传统 RL/自反思模型中常见的“认知偏误”与“错误经验闭环”，对构建长期稳健演进的 AI 系统有深刻启发。
