import os
import requests
import json
from google import genai  # 使用最新的 Google GenAI SDK

# 1. 获取 Hugging Face Daily Papers 列表
def fetch_hf_papers():
    # Hugging Face 官方开放的 Daily Papers API
    url = "https://huggingface.co/api/daily_papers"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        papers = response.json()
        return papers[:20]  # 只取前 15 篇最热门的论文防止 Token 溢出
    except Exception as e:
        print(f"获取 Hugging Face 数据失败: {e}")
        return []

# 2. 调用 Gemini API 进行总结
def summarize_with_gemini(papers_data):
    # 初始化客户端，会自动读取环境变量中的 GEMINI_API_KEY
    client = genai.Client()
    
    # 构建 Prompt，将论文数据结构化传给模型
    prompt = f"""
    你是一个世界顶尖的 AI 研究专家。下面是今天 Hugging Face Daily Papers 的论文列表（JSON 格式）。
    请帮我阅读这些数据，并生成一份中文的 Markdown 总结。
    
    【格式要求】
    1. 首先用 3 句话总结今日的整体研究趋势。
    2. 对每篇重点论文（筛选点赞数排名前 15 篇左右的论文即可），输出：
       - **[论文标题（英文原名）]** (附带论文链接: https://huggingface.co/papers/{{id}})
       - **研究机构/作者** (如果有)
       - **核心痛点与创新点**：用 5-8 句话解释这篇论文解决了什么问题、怎么解决的。
       - **潜在影响力**：这篇论文对行业或后续研究有什么启发。
    
    以下是数据：
    {json.dumps(papers_data, ensure_ascii=False, indent=2)}
    """
    
    # 推荐使用 gemini-1.5-flash，速度极快且完全免费
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
    )
    return response.text

# 3. 消息推送（这里以飞书/钉钉 Webhook 为例，您可替换为其他推送方式）
def send_notification(content):
    # 这里也可以选择直接写入文件保存到本地 Git 仓库
    # 示例写入本地 markdown
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    papers = fetch_hf_papers()
    if papers:
        summary = summarize_with_gemini(papers)
        send_notification(summary)
    else:
        print("未获取到今日论文数据。")
