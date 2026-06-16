import json
import datetime

def _get_default_today():
    return datetime.date.today().strftime("%Y-%m-%d")

def get_prompt_daily_papers(data, today=None):
    return f"""
    你是一个世界顶尖的 AI 研究专家。下面是今天 Hugging Face Daily Papers 的论文列表（JSON 格式）。
    请帮我阅读这些数据，并生成一份中文的 Markdown 总结。
    
    【格式要求】
    1. 首先用 3 句话总结今日的整体研究趋势。
    2. 对每篇重点论文（筛选点赞数排名前 20 篇左右的论文即可，如数据不足则有多少分析多少），输出：
       - **[论文标题（英文原名）]** (附带论文链接: https://huggingface.co/papers/{{id}})
       - **研究机构/作者** (如果有)
       - **核心痛点与创新点**：用 5-8 句话解释这篇论文解决了什么问题、怎么解决的。
       - **潜在影响力**：这篇论文对行业或后续研究有什么启发。
       
    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """

def get_prompt_trending_papers(data, today=None):
    return f"""
    你是一个世界顶尖的 AI 研究专家。下面是今天 Hugging Face Trending Papers 的论文列表（JSON 格式）。
    请帮我阅读 these 数据，并生成一份中文的 Markdown 总结。
    
    【格式要求】
    1. 首先用 3 句话总结今日的整体研究趋势。
    2. 对每篇重点论文（筛选点赞数排名前 30 篇左右的论文，如数据不足则有多少分析多少），输出：
       - **[论文标题（英文原名）]** (附带论文链接: https://huggingface.co/papers/{{id}})
       - **研究机构/作者** (如果有)
       - **核心痛点与创新点**：用 5-8 句话解释这篇论文解决了什么问题、怎么解决的。
       - **潜在影响力**：这篇论文对行业或后续研究有什么启发。
       
    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """

def get_prompt_github_trending(data, today=None):
    current_date = today or _get_default_today()
    return f"""
    ## GitHub Trending 每日自动总结任务 ({current_date})
    你是一个世界顶尖的 AI 软件架构师。请根据下方提供的 GitHub Trending Top 20 项目列表（JSON 格式），输出一份深度中文 Markdown 总结报告。

    请严格按照以下报告结构输出：
    1. **标题与日期**
    2. **Trending Top 20 表格**：含列（项目名称与链接、语言、总Star、今日新增Star、功能描述）
    3. **项目详细分析**：每个项目分别用 5-8 句话深度介绍：
       - 项目的核心功能与技术特点
       - 主要技术栈和实现方式
       - 适用的应用场景
    4. **今日趋势特点总结**（2-3 个要点）
    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """

def get_prompt_models(data, today=None):
    return f"""
    你是一个世界顶尖的 AI 模型和部署优化专家。下面是今天 Hugging Face Trending Models 的热门模型列表（JSON 格式）。
    请阅读数据并生成一份中文 Markdown 总结报告。
    
    【格式要求】
    1. 首先用 3 句话总结今日热门开源模型的设计方向（例如多模态、轻量化、特定架构等）。
    2. 对每个重点趋势模型（筛选前 20 个，如不足则有多少分析多少），输出：
       - **[模型 ID]** (链接: https://huggingface.co/{{id}})
       - **作者与提供者**
       - **标签与任务类型** (结合 tags)
       - **核心功能与技术特点分析**：用 5-8 句话详细分析该模型背后的主要技术亮点与架构特性。
       - **潜在应用前景与影响力**：该模型对下游开发、业务部署或学术研究能带来什么促进作用。
       
    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """

def get_prompt_spaces(data, today=None):
    return f"""
    你是一个世界顶尖的 AI 应用体验和交互设计师。下面是今天 Hugging Face Trending Spaces 的热门应用 Demo 列表（JSON 格式）。
    请阅读数据并生成一份中文 Markdown 总结报告。
    
    【格式要求】
    1. 首先用 3 句话总结今日开源社区中最热门的应用 Demo 形态与交互演进特点（例如文生视频、实时语音交互、自主 Agent 等）。
    2. 对每个重点 Space 应用（筛选前 15 个，如不足则有多少分析多少），输出：
       - **[Space 名称与作者]** (链接: https://huggingface.co/spaces/{{id}})
       - **核心 SDK 技术栈** (如 Gradio, Streamlit, Docker)
       - **功能亮点与底层技术解析**：用 5-8 句话详细解析该应用演示了什么功能，它可能是如何与底层大模型/算法交互实现的。
       - **复现或二次开发价值**：普通开发者或产品研究者可以从中借鉴什么思路、如何将其集成 to自己的商业流。
       
    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """
