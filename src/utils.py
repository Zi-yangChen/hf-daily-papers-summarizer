import os

def save_markdown_report(folder, prefix, content, today):
    os.makedirs(folder, exist_ok=True)
    filename = f"{prefix}-{today}.md"
    filepath = os.path.join(folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"成功保存报告到: {filepath}")
