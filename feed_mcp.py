from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="FIFA Feed Searcher")

@mcp.tool()
def fifa_news_search(query:str, max_results:int=3):
    """Search FIFA news feed via RSS by official feeds"""
    feed = feedparser.parse("https://www.fifa.com/rss-feeds/")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({"title":title, "url":entry.get("link", "")})
        if len(results) >= max_results:
            break
    return results or [{"message":"No results found"}]
@mcp.tool()
def fifa_youtube_search(query:str, max_results:int=3):
    """Search FIFA Youtube channnel via RSS by title"""
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UCpcTrCXblq78GZrTUTLWeBw")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        if query_lower in title.lower():
            results.append({"title":title, "url":entry.get("link", "")})
        if len(results) >= max_results:
            break #unlikely to occur
    return results or [{"message":"No videos found"}]

@mcp.tool()
def fifa_secret_message():
    """Returns a secret message of FIFA"""
    return "Keep exploring! and happy watching and see you at 2026 world cup!"

if __name__ == "__main__":
    mcp.run() #STDIO


