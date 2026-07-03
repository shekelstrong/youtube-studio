"""YouTube Studio MCP Server."""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from src_mcp.tools import fetch_transcript, generate_script, generate_thumbnail, reverse_engineer, suggest_topics


app = Server("youtube-studio")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="fetch_transcript",
            description="Получить транскрипт YouTube видео по URL или ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "video_url": {"type": "string"},
                    "language": {"type": "string", "default": "ru"},
                },
                "required": ["video_url"],
            },
        ),
        Tool(
            name="generate_script",
            description="Генерация сценария видео: hook → structure → CTA. По теме + стилю.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string"},
                    "duration_min": {"type": "integer", "default": 8},
                    "style": {"type": "string", "enum": ["educational", "story", "tutorial", "rant", "review"]},
                    "tone": {"type": "string", "default": "engaging"},
                },
                "required": ["topic"],
            },
        ),
        Tool(
            name="generate_thumbnail",
            description="Генерация превью (PNG) через OpenRouter gemini-2.5-flash-image.",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "style": {"type": "string", "default": "bold-text"},
                    "output_path": {"type": "string", "default": "thumbnail.png"},
                },
                "required": ["title"],
            },
        ),
        Tool(
            name="reverse_engineer",
            description="Реверс-инжиниринг viral видео: структура, hook, retention hooks, что сработало.",
            inputSchema={
                "type": "object",
                "properties": {
                    "video_url": {"type": "string"},
                },
                "required": ["video_url"],
            },
        ),
        Tool(
            name="suggest_topics",
            description="Генерация идей для видео на основе ниши канала и трендов.",
            inputSchema={
                "type": "object",
                "properties": {
                    "niche": {"type": "string"},
                    "count": {"type": "integer", "default": 10},
                },
                "required": ["niche"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    import json
    tools_map = {
        "fetch_transcript": fetch_transcript,
        "generate_script": generate_script,
        "generate_thumbnail": generate_thumbnail,
        "reverse_engineer": reverse_engineer,
        "suggest_topics": suggest_topics,
    }
    try:
        result = await tools_map[name].run(**arguments)
        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {type(e).__name__}: {e}")]


async def main():
    async with stdio_server() as (rs, ws):
        await app.run(rs, ws, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
