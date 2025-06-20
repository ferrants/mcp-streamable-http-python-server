import os
from mcp.server.fastmcp import FastMCP

PORT = os.getenv("PORT", "3000")
HOST = os.getenv("HOST")
kwargs = {}
if HOST is not None:
    kwargs['host'] = HOST

# Create an MCP server
mcp = FastMCP("Demo", port=PORT, debug=True, log_level="DEBUG", **kwargs)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(f"Running on port {PORT}")
    mcp.run(transport="streamable-http")
