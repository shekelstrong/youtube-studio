---
name: youtube-studio
description: YouTube-креатор. Транскрипты видео, генерация сценариев (hook/intro/main/CTA), thumbnails через AI, реверс-инжиниринг viral видео, генерация идей по нише.
---

# YouTube Studio

MCP-сервер для YouTube-креаторов.

## Когда использовать

- Нужен сценарий видео
- Парсить транскрипт чужого видео для анализа
- Разобрать почему viral видео залетело
- Сгенерировать идеи для канала
- Сделать thumbnail через AI

## 5 tools

```
видео → fetch_transcript (текст + тайминги)
идея → generate_script (структура с retention hooks)
идея → generate_thumbnail (PNG)
viral → reverse_engineer (что сработало)
ниша → suggest_topics (идеи)
```

## Алгоритм

### 1. fetch_transcript
youtube-transcript-api:
- Авто-детект языка (ru, en, ...)
- Ручные субтитры приоритетнее автогенерированных
- Snippets с таймингами
- Word count

### 2. generate_script
4 секции с таймингами:
- **HOOK** (15 сек) — 4 шаблона
- **INTRO** (30 сек) — обещание ценности
- **MAIN** (60-90% времени) — retention hooks каждые 60-90 сек
- **CTA** (60 сек) — подписка/лайк/следующее видео

5 стилей: educational / story / tutorial / rant / review.

### 3. generate_thumbnail
OpenRouter gemini-2.5-flash-image, 1280x720.
4 стиля: bold-text, shocked-face, product-shot, comparison.

### 4. reverse_engineer
Framework анализа:
- Hook (5 сек)
- Title pattern
- Thumbnail (CTR)
- Structure (setup → tension → payoff)
- Pacing (смена кадра каждые 3-5 сек)
- Retention hooks
- CTA
- Emotional arc

### 5. suggest_topics
5 ниш с шаблонами: ai, tech, freelance, business, default.

## Pitfalls

| Ошибка | Последствие | Как избежать |
|---|---|---|
| Длинное интро | Зритель уходит до hook | 5-секундный hook в начале |
| Только talking head | Скучно | Смена кадра каждые 3-5 сек |
| Clickbait без payoff | Дизлайки, жалобы | Title = реальный content |
| Нет CTA | Теряешь подписчиков | Заканчивай призывом |
| 1 retention hook на 20 мин | Зритель засыпает | Каждые 60-90 сек |
| Без thumbnail | CTR < 1% | AI-генерация + A/B test |

## Источники

5 скиллов: youtube-content, media-content-ops, programmatic-video-render, video-reverse-engineering, anthropic-slack-gif-creator.
