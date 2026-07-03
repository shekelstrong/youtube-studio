"""generate_thumbnail: генерация превью через OpenRouter."""


async def run(title: str, style: str = "bold-text", output_path: str = "thumbnail.png") -> dict:
    """Генерирует превью.

    Args:
        title: Текст на превью.
        style: bold-text / shocked-face / product-shot / comparison.
        output_path: Куда сохранить.

    Returns:
        Словарь с путём и промптом.
    """
    import os
    import base64
    import httpx

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return {"error": "OPENROUTER_API_KEY не задан"}

    prompt = (
        f"YouTube thumbnail 1280x720, eye-catching. "
        f"Style: {style}. "
        f"Title: '{title}'. "
        f"Bold readable text, high contrast, saturated colors. "
        f"No logos, no watermarks."
    )

    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.post(
            "https://openrouter.ai/api/v1/images",
            json={"model": "google/gemini-2.5-flash-image", "prompt": prompt},
            headers={"Authorization": f"Bearer {api_key}"},
        )

    if resp.status_code != 200:
        return {"error": f"OpenRouter {resp.status_code}: {resp.text[:200]}"}

    data = resp.json()
    b64 = data.get("data", [{}])[0].get("b64_json")
    if not b64:
        return {"error": "No image in response"}

    from pathlib import Path
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_bytes(base64.b64decode(b64))

    return {
        "output_path": output_path,
        "size_bytes": os.path.getsize(output_path),
        "prompt": prompt,
    }
