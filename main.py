import os
import time
import datetime
from google import genai

from config import TASKS
from src.utils import save_markdown_report

# 获取当前的北京时间日期 (配合 YAML 中设置的 Asia/Shanghai 时区)
today = datetime.date.today().strftime("%Y-%m-%d")

def generate_with_retry(client, prompt, max_retry=5):
    """Gemini 请求，遇到 503 自动重试"""

    for retry in range(max_retry):
        try:
            print(f"正在向 Gemini 提交分析请求（第 {retry + 1} 次）...")

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
            )

            return response

        except Exception as e:
            error = str(e)

            # 仅处理服务器繁忙
            if "503" in error or "UNAVAILABLE" in error:

                if retry == max_retry - 1:
                    raise

                wait = 30 * (2 ** retry)

                print(f" Gemini 当前繁忙，{wait} 秒后重试...")

                time.sleep(wait)

                continue

            # 其它错误直接结束
            raise


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
        
        # 3. 单次调用 Gemini (无重试机制，若失败则直接触发 Exception 逻辑)
        print(f"✨ 正在向 Gemini 提交分析请求...")
        response = generate_with_retry(client, prompt)
        
        # 4. 保存 Markdown 报告
        save_markdown_report(task["folder"], task["prefix"], response.text, today)
        print(f"✅ 任务 {task_name} 执行完毕！")
        
    except Exception as e:
        # 如果 API 提交或数据抓取失败，在此捕获，不会中断整个 main.py 循环
        print(f"❌ 任务 {task_name} 运行中发生错误: {e}")
    
    # 💤 无论成功还是失败，每个任务提交间隔 5 分钟 (300 秒)
    print("⏳ 等待 5 分钟以符合任务提交间隔要求...")
    time.sleep(300)

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
