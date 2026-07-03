"""reverse_engineer: реверс-инжиниринг viral видео."""


async def run(video_url: str) -> dict:
    """Анализирует viral видео.

    Args:
        video_url: URL видео.

    Returns:
        Словарь с разбором структуры.
    """
    return {
        "video_url": video_url,
        "analysis_framework": {
            "hook": "Первые 5 секунд — почему зритель остался?",
            "title_pattern": "Clickbait / curiosity gap / конкретная выгода",
            "thumbnail": "Лицо + текст + яркий фон. CTR измеряется YouTube",
            "structure": "Setup → tension → payoff. Или listicle (5 способов)",
            "pacing": "Смена кадра каждые 3-5 сек для удержания внимания",
            "retention_hooks": "Open loops, 'но это ещё не всё', 'секрет в том что...'",
            "cta": "Subscribe, like, comment. Ссылка на следующее видео",
            "emotional_arc": "Confusion → insight → relief. Или pain → solution",
        },
        "key_questions": [
            "Какой hook использовался?",
            "Сколько retention hooks в видео?",
            "Какой emotional arc?",
            "Где видео можно применить в своих?",
            "Что НЕ сработало (если знаешь retention graph)?",
        ],
        "anti_patterns_to_avoid": [
            "Длинное интро без hook (зритель уходит)",
            "Только talking head без смены визуала (скучно)",
            "Нет CTA в конце (теряешь подписчиков)",
            "Clickbait без payoff (зритель злится, дизлайки)",
        ],
    }
