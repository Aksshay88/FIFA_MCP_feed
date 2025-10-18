# RSS Feed Server MCP

A Model Context Protocol (MCP) server built with FastMCP that provides RSS feed aggregation and search capabilities for FIFA news and YouTube content.

## 🎯 Overview

This MCP server enables AI assistants to search and retrieve content from FIFA's official RSS feeds, including news articles and YouTube videos. Built using FastMCP and feedparser, it provides three specialized tools for content discovery.

## ✨ Features

- **FIFA News Search**: Query FIFA's official news RSS feed
- **FIFA YouTube Search**: Search FIFA's YouTube channel content via RSS
- **Secret Message Tool**: Easter egg feature for fun interactions
- Real-time RSS feed parsing and filtering
- Configurable result limits

## 📋 Technical Stack

- **FastMCP** (v2.12.5): Framework for building MCP servers
- **feedparser** (v6.0.12): RSS/Atom feed parsing
- **Python** (3.13+): Core runtime
- **MCP Protocol** (v1.16.0): Model Context Protocol implementation

## 🔧 Installation

### Prerequisites

- Python 3.13 or higher
- pip package manager
- Virtual environment support (venv)

### Step 1: Clone the Repository

```bash
cd ~/Desktop/Projects
git clone <your-repo-url> rss-server
cd rss-server
```

### Step 2: Create Virtual Environment (Linux)

```bash
# Create a new virtual environment
python3 -m venv meraenv

# Activate the virtual environment
source meraenv/bin/activate

# Your prompt should now show (meraenv) prefix
```

### Step 3: Install Dependencies

```bash
# Ensure pip is up to date
pip install --upgrade pip

# Install required packages
pip install fastmcp feedparser

# Verify installation
pip list | grep -E "fastmcp|feedparser|mcp"
```

Expected output:
```
fastapi-mcp               0.4.0
fastmcp                   2.12.5
feedparser                6.0.12
mcp                       1.16.0
```

## 🚀 Usage

### Running the Server

#### Method 1: Direct Execution

```bash
# Activate virtual environment
source meraenv/bin/activate

# Run the MCP server
python feed_mcp.py
```

The server will start in STDIO mode and wait for MCP protocol messages.

#### Method 2: With MCP Client

```bash
# Using with an MCP client application
mcp run python feed_mcp.py
```

### Deactivating Virtual Environment

```bash
deactivate
```

## 🔍 Available Tools

### 1. fifa_news_search

Search FIFA's official news feed for articles matching your query.

**Parameters:**
- `query` (string, required): Search term to filter news articles
- `max_results` (int, optional): Maximum results to return (default: 3)

**Example Response:**
```json
[
  {
    "title": "FIFA World Cup 2026 Updates",
    "url": "https://www.fifa.com/..."
  }
]
```

### 2. fifa_youtube_search

Search FIFA's YouTube channel for videos matching your query.

**Parameters:**
- `query` (string, required): Search term to filter video titles
- `max_results` (int, optional): Maximum results to return (default: 3)

**Example Response:**
```json
[
  {
    "title": "Best Goals of the Tournament",
    "url": "https://www.youtube.com/watch?v=..."
  }
]
```

### 3. fifa_secret_message

Returns a motivational message about FIFA.

**Parameters:** None

**Example Response:**
```
"Keep exploring! and happy watching and see you at 2026 world cup!"
```

## 🧪 Testing with MCP Inspector

The MCP Inspector is a valuable tool for testing and debugging your MCP server.

### Installing MCP Inspector

```bash
# Install Node.js if not already installed (required for inspector)
# Ubuntu/Debian:
sudo apt update
sudo apt install nodejs npm

# Install MCP Inspector globally
npm install -g @modelcontextprotocol/inspector

# Verify installation
npx @modelcontextprotocol/inspector --version
```

### Using MCP Inspector

1. **Start the Inspector:**

```bash
# Activate your virtual environment first
source meraenv/bin/activate

# Launch inspector with your MCP server
npx @modelcontextprotocol/inspector python feed_mcp.py
```

2. **The Inspector Web Interface:**

The inspector will start a web server (typically at `http://localhost:5173`) and open it in your browser.

3. **Testing Your Tools:**

In the Inspector UI:
- **View Available Tools**: See all three tools (fifa_news_search, fifa_youtube_search, fifa_secret_message)
- **Test Tool Calls**: Click on any tool to test it with parameters
- **Inspect Responses**: View formatted JSON responses
- **Debug Protocol**: Monitor MCP protocol messages in real-time

4. **Example Test Cases:**

**Test FIFA News Search:**
```json
{
  "query": "world cup",
  "max_results": 3
}
```

**Test YouTube Search:**
```json
{
  "query": "highlights",
  "max_results": 5
}
```

**Test Secret Message:**
```json
{}
```

### Inspector Features

- **Real-time Protocol Monitoring**: See all MCP messages exchanged
- **Tool Testing Interface**: Interactive tool invocation with parameter forms
- **Response Visualization**: Pretty-printed JSON responses
- **Error Debugging**: Clear error messages and stack traces
- **Schema Validation**: Automatic validation of tool parameters

## 🏗️ Technical Architecture

### Code Structure

```
rss-server/
├── feed_mcp.py          # Main MCP server implementation
├── meraenv/             # Python virtual environment
└── README.md            # This file
```

### How It Works

1. **FastMCP Framework**: Provides decorator-based tool registration and STDIO transport
2. **feedparser Library**: Parses RSS/Atom feeds from URLs
3. **Tool Functions**: Python functions decorated with `@mcp.tool()` become MCP tools
4. **Query Filtering**: Case-insensitive string matching in titles and descriptions
5. **Result Limiting**: Configurable maximum results to prevent overwhelming responses

### RSS Feed Sources

- **FIFA News**: `https://www.fifa.com/rss-feeds/`
- **FIFA YouTube**: `https://www.youtube.com/feeds/videos.xml?channel_id=UCpcTrCXblq78GZrTUTLWeBw`

## 🛠️ Development

### Adding New Tools

To add a new RSS feed source:

```python
@mcp.tool()
def your_new_search(query: str, max_results: int = 3):
    """Description of your tool"""
    feed = feedparser.parse("YOUR_RSS_FEED_URL")
    results = []
    query_lower = query.lower()
    
    for entry in feed.entries:
        title = entry.get("title", "")
        if query_lower in title.lower():
            results.append({
                "title": title,
                "url": entry.get("link", "")
            })
        if len(results) >= max_results:
            break
    
    return results or [{"message": "No results found"}]
```

### Testing Changes

```bash
# Activate environment
source meraenv/bin/activate

# Run with inspector for interactive testing
npx @modelcontextprotocol/inspector python feed_mcp.py

# Or test directly
python feed_mcp.py
```

## 🐛 Troubleshooting

### Virtual Environment Issues

**Problem**: `source: command not found`
```bash
# Use dot instead of source
. meraenv/bin/activate
```

**Problem**: Permission denied
```bash
chmod +x meraenv/bin/activate
source meraenv/bin/activate
```

### Package Installation Issues

**Problem**: `pip: command not found`
```bash
# Install pip
sudo apt install python3-pip

# Or use python module
python3 -m pip install fastmcp feedparser
```

### MCP Inspector Issues

**Problem**: Inspector won't start
```bash
# Check Node.js version (should be 18+)
node --version

# Reinstall inspector
npm uninstall -g @modelcontextprotocol/inspector
npm install -g @modelcontextprotocol/inspector
```

**Problem**: Port already in use
```bash
# Kill process on port 5173
lsof -ti:5173 | xargs kill -9

# Or specify different port
npx @modelcontextprotocol/inspector --port 5174 python feed_mcp.py
```

### RSS Feed Issues

**Problem**: No results returned
- Check internet connectivity
- Verify RSS feed URLs are accessible
- Test feeds directly: `curl https://www.fifa.com/rss-feeds/`

**Problem**: Parse errors
- Ensure feedparser is installed: `pip show feedparser`
- Check feed format with: `python -c "import feedparser; print(feedparser.parse('URL'))"`

## 📝 Requirements File

Create `requirements.txt` for easier installation:

```txt
fastmcp==2.12.5
feedparser==6.0.12
mcp==1.16.0
fastapi-mcp==0.4.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 🔒 Security Considerations

- RSS feeds are parsed from official FIFA sources only
- No authentication or API keys required
- STDIO transport ensures local-only communication
- No data persistence or logging implemented

## 📚 Additional Resources

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [feedparser Documentation](https://feedparser.readthedocs.io/)
- [MCP Inspector GitHub](https://github.com/modelcontextprotocol/inspector)

## 🤝 Contributing

To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with MCP Inspector
5. Submit a pull request


## 🎉 Acknowledgments

- FastMCP framework by Jeremiah Lowin
- Model Context Protocol by Anthropic
- feedparser library maintainers
- FIFA for providing public RSS feeds

---

**Happy RSS Feeding! See you at the 2026 World Cup! ⚽**
