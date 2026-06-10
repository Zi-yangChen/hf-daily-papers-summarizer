import os
import time
import random

def save_markdown_report(folder, prefix, content, today):
    os.makedirs(folder, exist_ok=True)
    filename = f"{prefix}-{today}.md"
    filepath = os.path.join(folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"成功保存报告到: {filepath}")

def generate_content_with_retry(client, model, contents, max_retries=6, initial_delay=15, backoff_factor=2):
    """
    带重试机制的 API 请求封装函数。
    支持指数退避和随机抖动，主要针对 503 (高负载) 和 429 (频率超限) 错误。
    """
    delay = initial_delay
    for attempt in range(1, max_retries + 1):
        try:
            response = client.models.generate_content(
                model=model,
                contents=contents,
            )
            return response
        except Exception as e:
            err_msg = str(e)
            print(f"⚠️ API 调用失败 (尝试 {attempt}/{max_retries}): {err_msg}")
            
            if attempt == max_retries:
                raise e
            
            jitter = random.uniform(0.8, 1.2)
            sleep_time = delay * jitter
            print(f"⏳ 服务忙/受限，等待 {sleep_time:.1f} 秒后重试...")
            time.sleep(sleep_time)
            
            delay *= backoff_factor
