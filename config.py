from src.fetchers import (
    fetch_hf_daily_papers,
    fetch_hf_trending_papers,
    fetch_github_trending,
    fetch_hf_trending_models,
    fetch_hf_trending_spaces
)
from src.prompts import (
    get_prompt_daily_papers,
    get_prompt_trending_papers,
    get_prompt_github_trending,
    get_prompt_models,
    get_prompt_spaces
)

# 注册所有要运行的任务元数据
TASKS = [
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
