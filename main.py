import os
import time
import datetime
import json
import requests
from bs4 import BeautifulSoup
from google import genai

# 获取当前的北京时间日期 (配合 YAML 中设置的 Asia/Shanghai 时区)
today = datetime.date.today().strftime("%Y-%m-%d")

# ==================== 1. 数据抓取模块 ====================

def fetch_hf_daily_papers():
    url = "https://huggingface.co/api/daily_papers"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        papers = []
        for item in data[:25]:  # 多拿几篇备用，API 通常返回 flat 或嵌套结构
            paper_data = item.get("paper") if "paper" in item else item
            papers.append({
                "id": paper_data.get("id"),
                "title": paper_data.get("title"),
                "upvotes": paper_data.get("upvotes", 0),
                "publishedAt": paper_data.get("publishedAt", "N/A")
            })
        return papers
    except Exception as e:
        print(f"抓取 HF Daily Papers 失败: {e}")
        return []

def fetch_hf_trending_papers():
    # 抓取通用趋势论文列表
    url = "https://huggingface.co/api/papers?limit=25"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        papers = []
        raw_list = data if isinstance(data, list) else data.get("items", [])
        for item in raw_list[:25]:
            papers.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "upvotes": item.get("upvotes", 0),
                "publishedAt": item.get("publishedAt", "N/A")
            })
        return papers
    except Exception as e:
        print(f"抓取 HF Trending Papers 失败: {e}")
        return []

def fetch_github_trending():
    url = "https://github.com/trending"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        repos = []
        rows = soup.select("article.Box-row")
        for row in rows[:20]:
            title_el = row.select_one("h2.h3 a")
            if not title_el:
                continue
            href = title_el["href"]
            name = href.strip("/")
            link = f"https://github.com{href}"
            
            lang_el = row.select_one('[itemprop="programmingLanguage"]')
            lang = lang_el.text.strip() if lang_el else "N/A"
            
            stars_total = "N/A"
            stars_today = "N/A"
            
            muted_links = row.select("a.Link--muted")
            for link_el in muted_links:
                href_attr = link_el.get("href", "")
                if "stargazers" in href_attr:
                    stars_total = link_el.text.strip()
            
            today_el = row.select_one("span.d-inline-block.float-sm-right")
            if today_el:
                stars_today = today_el.text.strip().replace("stars today", "").strip()
                
            desc_el = row.select_one("p.col-9")
            desc = desc_el.text.strip() if desc_el else "No description provided."
            
            repos.append({
                "name": name,
                "link": link,
                "language": lang,
                "stars_total": stars_total,
                "stars_today": stars_today,
                "description": desc
            })
        return repos
    except Exception as e:
        print(f"抓取 GitHub Trending 失败: {e}")
        return []

def fetch_hf_trending_models():
    # 抓取前 20 趋势模型
    url = "https://huggingface.co/api/models?sort=trending&limit=20"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        models = []
        for item in data[:20]:
            models.append({
                "id": item.get("id"),
                "author": item.get("author", "N/A"),
                "likes": item.get("likes", 0),
                "downloads": item.get("downloads", 0),
                "tags": item.get("tags", [])[:8]  # 限制标签长度
            })
        return models
    except Exception as e:
        print(f"抓取 HF Trending Models 失败: {e}")
        return []

def fetch_hf_trending_spaces():
    # 抓取前 20 趋势 Space 应用
    url = "https://huggingface.co/api/spaces?sort=trending&limit=20"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        spaces = []
        for item in data[:20]:
            spaces.append({
                "id": item.get("id"),
                "author": item.get("author", "N/A"),
                "likes": item.get("likes", 0),
                "sdk": item.get("sdk", "N/A"),
                "tags": item.get("tags", [])[:5]
            })
        return spaces
    except Exception as e:
        print(f"抓取 HF Trending Spaces 失败: {e}")
        return []


# ==================== 2. Prompt 生成模块 ====================

def get_prompt_daily_papers(data):
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

def get_prompt_trending_papers(data):
    return f"""
    你是一个世界顶尖的 AI 研究专家。下面是今天 Hugging Face Trending Papers 的论文列表（JSON 格式）。
    请帮我阅读这些数据，并生成一份中文的 Markdown 总结。
    
    【格式要求】
    1. 首先用 3 句话总结今日的整体研究趋势。
    2. 对每篇重点论文（筛选点赞数排名前 15 篇左右的论文，如数据不足则有多少分析多少），输出：
       - **[论文标题（英文原名）]** (附带论文链接: https://huggingface.co/papers/{{id}})
       - **研究机构/作者** (如果有)
       - **核心痛点与创新点**：用 5-8 句话解释这篇论文解决了什么问题、怎么解决的。
       - **潜在影响力**：这篇论文对行业或后续研究有什么启发。
       
    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """

def get_prompt_github_trending(data):
    return f"""
    ## GitHub Trending 每日自动总结任务 ({today})
    你是一个世界顶尖的 AI 软件架构师。请根据下方提供的 GitHub Trending Top 20 项目列表（JSON 格式），输出一份深度中文 Markdown 总结报告。

    请严格按照以下报告结构输出：
    1. **标题与日期**
    2. **Trending Top 20 表格**：含列（项目名称与链接、语言、总Star、今日新增Star、功能描述）
    3. **AI/Agent 相关项目详细分析**：针对与 AI, Agent, LLM 等相关的项目，每个项目用 5-8 句话深度介绍：
       - 项目的核心功能与技术特点
       - 主要技术栈和实现方式
       - 适用的应用场景
    4. **AI 项目对 AI4S（AI for Science）工作者的价值**：
       - 对科研工作的帮助（如文献处理、数据分析、论文写作等）
       - 可否集成到现有工作流
       - 学习借鉴的价值
    5. **今日趋势特点总结**（2-3 个要点）
    6. **非 AI 项目的简要说明**（用 1-2 句话做一句话横向总结）

    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """

def get_prompt_models(data):
    return f"""
    你是一个世界顶尖的 AI 模型和部署优化专家。下面是今天 Hugging Face Trending Models 的热门模型列表（JSON 格式）。
    请阅读数据并生成一份中文 Markdown 总结报告。
    
    【格式要求】
    1. 首先用 3 句话总结今日热门开源模型的设计方向（例如多模态、轻量化、特定架构等）。
    2. 对每个重点趋势模型（筛选前 15 个，如不足则有多少分析多少），输出：
       - **[模型 ID]** (链接: https://huggingface.co/{{id}})
       - **作者与提供者**
       - **标签与任务类型** (结合 tags)
       - **核心功能与技术特点分析**：用 5-8 句话详细分析该模型背后的主要技术亮点与架构特性。
       - **潜在应用前景与影响力**：该模型对下游开发、业务部署或学术研究能带来什么促进作用。
       
    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """

def get_prompt_spaces(data):
    return f"""
    你是一个世界顶尖的 AI 应用体验和交互设计师。下面是今天 Hugging Face Trending Spaces 的热门应用 Demo 列表（JSON 格式）。
    请阅读数据并生成一份中文 Markdown 总结报告。
    
    【格式要求】
    1. 首先用 3 句话总结今日开源社区中最热门的应用 Demo 形态与交互演进特点（例如文生视频、实时语音交互、自主 Agent 等）。
    2. 对每个重点 Space 应用（筛选前 15 个，如不足则有多少分析多少），输出：
       - **[Space 名称与作者]** (链接: https://huggingface.co/spaces/{{id}})
       - **核心 SDK 技术栈** (如 Gradio, Streamlit, Docker)
       - **功能亮点与底层技术解析**：用 5-8 句话详细解析该应用演示了什么功能，它可能是如何与底层大模型/算法交互实现的。
       - **复现或二次开发价值**：普通开发者或产品研究者可以从中借鉴什么思路、如何将其集成到自己的商业流。
       
    以下是数据：
    {json.dumps(data, ensure_ascii=False, indent=2)}
    """


# ==================== 3. 运行控制中心 ====================

def save_markdown_report(folder, prefix, content):
    os.makedirs(folder, exist_ok=True)
    filename = f"{prefix}-{today}.md"
    filepath = os.path.join(folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"成功保存报告到: {filepath}")

def run_task(client, task_name, fetch_func, prompt_func, folder_name, file_prefix):
    print(f"\n🚀 开始执行任务: {task_name}")
    try:
        # 获取原始数据
        data = fetch_func()
        if not data:
            print(f"⚠️ {task_name}: 未获取到任何数据，跳过此任务。")
            return
        
        # 组装 Prompt
        prompt = prompt_func(data)
        
        # 调用 Gemini (Free Tier 默认限额 15 RPM，一分钟最多 15 次调用)
        print(f"✨ 正在向 Gemini 提交分析请求...")
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt,
        )
        
        # 保存 Markdown
        save_markdown_report(folder_name, file_prefix, response.text)
        print(f"✅ 任务 {task_name} 执行完毕！")
        
    except Exception as e:
        print(f"❌ 任务 {task_name} 运行中发生错误: {e}")
    
    # 💤 强制休眠 30 秒，确保单次 Actions 周期中不会触碰 15 RPM 的免费层频率限制
    print("⏳ 等待 30 秒以规避 API 频控上限...")
    time.sleep(30)

def main():
    # 从环境变量获取 API KEY，初始化官方最新 SDK
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("错误: 缺少 GEMINI_API_KEY 环境变量，程序退出。")
        return
    
    client = genai.Client(api_key=api_key)
    
    # 注册 5 个任务元数据
    tasks = [
        {
            "name": "Hugging Face Daily Papers",
            "fetch": fetch_hf_daily_papers,
            "prompt": get_prompt_daily_papers,
            "folder": "huggingface-daily-papers",
            "prefix": "huggingface-daily-papers"
        },
        {
            "name": "Hugging Face Trending Papers",
            "fetch": fetch_hf_trending_papers,
            "prompt": get_prompt_trending_papers,
            "folder": "huggingface-trending-papers",
            "prefix": "huggingface-trending-papers"
        },
        {
            "name": "GitHub Trending",
            "fetch": fetch_github_trending,
            "prompt": get_prompt_github_trending,
            "folder": "github-trending",
            "prefix": "github-trending"
        },
        {
            "name": "Hugging Face Trending Models",
            "fetch": fetch_hf_trending_models,
            "prompt": get_prompt_models,
            "folder": "huggingface-models",
            "prefix": "huggingface-models"
        },
        {
            "name": "Hugging Face Trending Spaces",
            "fetch": fetch_hf_trending_spaces,
            "prompt": get_prompt_spaces,
            "folder": "huggingface-spaces",
            "prefix": "huggingface-spaces"
        }
    ]
    
    print(f"📅 开始执行今日多维 AI 热点分析，日期: {today}")
    for task in tasks:
        run_task(
            client=client,
            task_name=task["name"],
            fetch_func=task["fetch"],
            prompt_func=task["prompt"],
            folder_name=task["folder"],
            file_prefix=task["prefix"]
        )
    print("\n🏁 所有任务执行完毕！")

if __name__ == "__main__":
    main()
