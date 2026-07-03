"""fetch_transcript: получить транскрипт YouTube видео."""


async def run(video_url: str, language: str = "ru") -> dict:
    """Получает транскрипт.

    Args:
        video_url: URL или ID видео.
        language: Код языка.

    Returns:
        Транскрипт с таймингами.
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return {"error": "youtube-transcript-api не установлен: pip install youtube-transcript-api"}

    import re

    # Извлекаем video ID
    match = re.search(r"(?:v=|youtu\.be/)([\w-]+)", video_url)
    video_id = match.group(1) if match else video_url

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Сначала русский
        try:
            transcript = transcript_list.find_manually_created_transcript([language])
        except Exception:
            try:
                transcript = transcript_list.find_generated_transcript([language])
            except Exception:
                # Первый доступный
                transcript = next(iter(transcript_list))

        snippets = transcript.fetch()
        full_text = " ".join(s["text"] for s in snippets)
        duration_sec = snippets[-1]["start"] + snippets[-1]["duration"] if snippets else 0

        return {
            "video_id": video_id,
            "language": transcript.language_code,
            "is_generated": transcript.is_generated,
            "duration_sec": round(duration_sec, 1),
            "full_text": full_text,
            "snippets_count": len(snippets),
            "word_count": len(full_text.split()),
        }
    except Exception as e:
        return {"error": str(e), "video_id": video_id}
