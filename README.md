# youtube-studio

> MCP-сервер для YouTube-креаторов: транскрипты, сценарии, thumbnails, реверс-инжиниринг viral видео, генерация идей.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![MCP](https://img.shields.io/badge/MCP-compatible-purple.svg)](https://modelcontextprotocol.io)

## 🎯 Что это

MCP-сервер с 5 инструментами для YouTube-креаторов:

- 📝 **fetch_transcript** — получение транскрипта видео
- 🎬 **generate_script** — структура сценария (hook → intro → main → CTA)
- 🖼 **generate_thumbnail** — превью через gemini-2.5-flash-image
- 🔍 **reverse_engineer** — разбор viral видео (hook, retention, structure)
- 💡 **suggest_topics** — генерация идей по нише

## 📦 Установка

```bash
git clone https://github.com/shekelstrong/youtube-studio.git
cd youtube-studio
pip install -r requirements.txt
pip install youtube-transcript-api  # для fetch_transcript
export OPENROUTER_API_KEY=sk-or-...  # для generate_thumbnail
```

## 🛠 MCP Tools

### fetch_transcript
```python
result = await fetch_transcript.run("https://youtu.be/VIDEO_ID", "ru")
# → {full_text, duration_sec, word_count, snippets_count}
```

### generate_script
```python
result = await generate_script.run("Как выучить английский за 3 месяца", duration_min=10, style="tutorial")
# → {structure: [HOOK, INTRO, MAIN, CTA], retention_hooks, principles}
```

4 секции: hook (15 сек), intro (30 сек), main, CTA.

### generate_thumbnail
```python
result = await generate_thumbnail.run("5 AI-инструментов", "bold-text", "/tmp/yt.png")
```

Gemini-2.5-flash-image, 1280x720.

### reverse_engineer
```python
result = await reverse_engineer.run("https://youtu.be/VIRAL_VIDEO")
# → {analysis_framework, key_questions, anti_patterns_to_avoid}
```

### suggest_topics
```python
result = await suggest_topics.run("ai", count=10)
# → {ideas: [...], principles: [...]}
```

5 ниш в базе: ai, tech, freelance, business, default.

## 📁 Структура

```
youtube-studio/
├── README.md
├── LICENSE
├── SKILL.md
├── requirements.txt
├── src_mcp/
│   ├── server.py
│   └── tools/
│       ├── fetch_transcript.py
│       ├── generate_script.py
│       ├── generate_thumbnail.py
│       ├── reverse_engineer.py
│       └── suggest_topics.py
└── .github/workflows/ci.yml
```

## 🎯 Структура сценария

| Секция | Время | Цель |
|---|---|---|
| HOOK | 0:00-0:15 | Зацепить за 5 сек, иначе зритель уйдёт |
| INTRO | 0:15-0:45 | Зачем смотреть, что получит |
| MAIN | остальное | Ценность + retention hooks каждые 60-90 сек |
| CTA | последние 60 сек | Подписка, лайк, следующее видео |

## 📄 License

MIT © Vasiliy Nedopekin (shekelstrong)
