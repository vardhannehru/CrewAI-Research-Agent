import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from crewai.tools import tool


@tool("AI News Search")
def search_ai_news(query: str) -> str:
    """Searches real-time AI news articles via Google News RSS.
    Provide keywords like 'Artificial Intelligence', 'OpenAI', or 'Anthropic Claude'."""
    try:
        # Encode spaces and symbols safely for the URL
        encoded_query = urllib.parse.quote(query)
        rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-US&gl=US&ceid=US:en"

        # Provide a standard browser User-Agent header
        req = urllib.request.Request(
            rss_url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                )
            },
        )

        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()

        # Parse the RSS XML structure
        root = ET.fromstring(xml_data)
        items = root.findall(".//item")

        if not items:
            return f"No news articles found for query: '{query}'."

        articles = []
        # Grab the top 5 freshest articles
        for item in items[:5]:
            title = (
                item.find("title").text
                if item.find("title") is not None
                else "No Title"
            )
            link = (
                item.find("link").text
                if item.find("link") is not None
                else "No Link"
            )
            pub_date = (
                item.find("pubDate").text
                if item.find("pubDate") is not None
                else "Recent"
            )
            source = (
                item.find("source").text
                if item.find("source") is not None
                else "Google News"
            )

            articles.append(
                f"📰 Title: {title}\n"
                f"📅 Published: {pub_date}\n"
                f"🏢 Source: {source}\n"
                f"🔗 Link: {link}\n"
                f"----------------------------------------"
            )

        return "\n\n".join(articles)

    except Exception as e:
        return f"Error fetching news for '{query}': {str(e)}"