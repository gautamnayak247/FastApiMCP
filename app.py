from fastapi import FastAPI
from fastapi_mcp import FastApiMCP


fast_api = FastAPI()


@fast_api.get("/hello", operation_id="hello_world")
def get_hello_world():
    return {"message": "Hello, World!"}

mcp = FastApiMCP(
    fast_api,
    include_operations=["hello_world"],
    name="My API MCP",
    description="My API description",
    base_url="http://localhost:8001",
    )

mcp_app = FastAPI()
mcp.mount(mcp_app)

@mcp_app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    return {"schema_version": "v1", "name_for_human": "Test Plugin"}

