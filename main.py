import os
import time
import datetime
from google import genai

from config import TASKS
from src.utils import generate_content_with_retry, save_markdown_report

# 获取当前的北京时间日期 (配合 YAML 中设置的 Asia/Shanghai 时区)
today = datetime.date.today().strftime("%Y-%m-%d")

def run_task(client, task):
    task_name = task["name"]
    print(f"\n🚀 开始执行任务: {task_name}")
    try:
        # 1. 获取原始数据
        data = task["fetch"]()
        if not data:
            print(f"⚠️ {task_name}: 未获取到任何数据，跳过此任务。")
            return
        
        # 2. 组装 Prompt
        prompt = task["prompt"](data, today)
        
        # 3. 调用 Gemini (带重试机制)
        print(f"✨ 正在向 Gemini 提交分析请求...")
        response = generate_content_with_retry(
            client=client,
            model='gemini-3.5-flash',
            contents=prompt,
            max_retries=6,
            initial_delay=15,
            backoff_factor=2
        )
        
        # 4. 保存 Markdown 报告
        save_markdown_report(task["folder"], task["prefix"], response.text, today)
        print(f"✅ 任务 {task_name} 执行完毕！")
        
    except Exception as e:
        print(f"❌ 任务 {task_name} 运行中发生错误: {e}")
    
    # 💤 强制休眠 30 秒，确保单次 Actions 周期中不会触碰 15 RPM 的免费层频率限制
    print("⏳ 等待 30 秒以规避 API 频控上限...")
    time.sleep(30)

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("错误: 缺少 GEMINI_API_KEY 环境变量，程序退出。")
        return
    
    client = genai.Client(api_key=api_key)
    
    print(f"📅 开始执行今日多维 AI 热点分析，日期: {today}")
    for task in TASKS:
        run_task(client, task)
    print("\n🏁 所有任务执行完毕！")

if __name__ == "__main__":
    main()
