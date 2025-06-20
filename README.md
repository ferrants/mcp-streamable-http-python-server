# mcp-streamable-http-python-server

This is a starting place for a new streamable-http MCP Server built with python.

Streamable HTTP Transport was introduced on 2025-03-26. [See MCP Spec Changelog](https://modelcontextprotocol.io/specification/2025-03-26/changelog).

Starts with the [MCP Python SDK Quickstart Example](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#quickstart) and contains dependencies for MCP to get rolling.

Clone or fork this repo, make updates and start building your Streamable HTTP MCP Server with Python.


## Running

Set up your environment:
```bash
python3.11 -m venv my_env
. ./my_env/bin/activate
pip install -r requirements.txt
```

Run the server:
```bash
python server.py
```

With a custom port:

```bash
PORT=3002 python server.py
```

## Connect a Client

You can connect a client to your MCP Server once it's running. Configure per the client's configuration. There is the [mcp-config.json](/mcp-config.json) that has an example configuration that looks like this:
```json
{
  "mcpServers": {
    "memvid": {
      "type": "streamable-http",
      "url": "http://localhost:3000"
    }
  }
}
```

### Acknowledgements

- Obviously the modelcontextprotocol and Anthropic teams for the MCP Specification. [https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)
- [HeyFerrante](https://heyferrante.com?ref=github-memvid-mcp-server) for enabling and sponsoring this project.
