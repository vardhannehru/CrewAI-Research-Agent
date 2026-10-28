import os
import sys  # <--- Make sure sys is imported
import webbrowser
from dotenv import load_dotenv
import markdown
from crew import news_crew

# Force Python on Windows to support emojis and international characters
sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()


def save_html_newsletter(content_markdown: str):
    # Convert markdown text to HTML tags
    html_body = markdown.markdown(content_markdown)

    # Wrap the converted body with clean, modern CSS styling
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Daily AI Newsletter</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #f4f7f6;
            color: #2d3748;
            margin: 0;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: #ffffff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }}
        h1 {{
            color: #1a202c;
            border-bottom: 3px solid #3182ce;
            padding-bottom: 12px;
        }}
        h2 {{
            color: #2b6cb0;
            margin-top: 30px;
        }}
        a {{
            color: #3182ce;
            text-decoration: none;
            font-weight: 600;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        p, li {{
            line-height: 1.7;
            font-size: 16px;
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_body}
    </div>
</body>
</html>"""

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    file_path = os.path.join("output", "newsletter.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"\n✨ Newsletter successfully saved to: {file_path}")
    return os.path.abspath(file_path)


def run():
    print("\n==========================================")
    print("🚀 Starting AI Daily Newsletter Crew...")
    print("==========================================\n")

    result = news_crew.kickoff()

    print("\n==========================================")
    print("✅ Crew Execution Finished!")
    print("==========================================\n")

    # Save to HTML and open in browser
    full_path = save_html_newsletter(str(result))
    webbrowser.open(f"file://{full_path}")


if __name__ == "__main__":
    run()