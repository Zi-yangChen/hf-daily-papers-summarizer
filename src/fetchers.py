import requests
from bs4 import BeautifulSoup

def fetch_hf_daily_papers():
    url = "https://huggingface.co/api/daily_papers"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        papers = []
        for item in data[:25]:
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
    url = "https://huggingface.co/api/models?sort=trendingScore&direction=-1&limit=20"
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
                "tags": item.get("tags", [])[:8]
            })
        return models
    except Exception as e:
        print(f"抓取 HF Trending Models 失败: {e}")
        return []

def fetch_hf_trending_spaces():
    url = "https://huggingface.co/api/spaces?sort=trendingScore&direction=-1&limit=20"
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
