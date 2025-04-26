from .astronomy import get_moon_phase_name, SIGNS, PHASE_EMOJIS, MOON_SIGN_DESCRIPTIONS
from .ai_prompt import build_moon_prompt
from .openai_client import call_openai
import ephem

def get_moon_info(date):
    observer = ephem.Observer()
    observer.date = f"{date.isoformat()} 12:00:00"

    moon = ephem.Moon(observer)
    moon.compute(observer)

    # Moon phase calculation
    phase = get_moon_phase_name(date)
    emoji = PHASE_EMOJIS.get(phase, "🌑")

    # Moon sign calculation
    moon_lon_deg = float(ephem.Ecliptic(moon).lon) * (180 / ephem.pi)
    sign_index = int((moon_lon_deg + 1e-6) // 30) % 12
    moon_sign = SIGNS[sign_index]

    # Moon sign description
    description = MOON_SIGN_DESCRIPTIONS.get(moon_sign, "The moon travels through unknown realms.")

    # Emotional text generation
    prompt = build_moon_prompt(phase, moon_sign)
    emotional_text = call_openai(prompt)

    return {
        "phase": phase,
        "sign": moon_sign,
        "emoji": emoji,
        "description": description,
        "emotion_text": emotional_text,
    }
