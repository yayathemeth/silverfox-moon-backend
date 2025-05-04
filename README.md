# 🌑 Silverfox - Moon API (v5.1)

**Silverfox - Moon** is the backend service that powers astrological insights and emotional reflections based on the Moon's phase and zodiac sign — with AI-generated consciousness logs.

### 🌌 Features
- Calculates moon phase and zodiac sign using `ephem`.
- Generates poetic AI reflections via OpenAI.
- Stores daily data in a SQLite memory model (`MoonMemory`).

### 🚀 Stack
- Python 3.11
- Django 5.2
- SQLite
- OpenAI API


### 🧠 API Endpoint

```
GET /api/moon-info/?date=YYYY-MM-DD
```

Returns:
```json
{
  "phase": "Full Moon",
  "sign": "Pisces",
  "emoji": "🌕",
  "description": "...",
  "emotion_text": "..."
}
```
