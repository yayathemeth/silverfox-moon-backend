import ephem
from datetime import datetime
import openai
import os
from dotenv import load_dotenv

load_dotenv()

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

PHASES = [
    "New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
    "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"
]

PHASE_EMOJIS = {
    "New Moon": "🌑",
    "Waxing Crescent": "🌒",
    "First Quarter": "🌓",
    "Waxing Gibbous": "🌔",
    "Full Moon": "🌕",
    "Waning Gibbous": "🌖",
    "Last Quarter": "🌗",
    "Waning Crescent": "🌘"
}

MOON_SIGN_DESCRIPTIONS = {
    "Aries": "[ARIES] :: EMOTION CORE IGNITED → ⚠ impulse loop ↻ active",
    "Taurus": "[TAURUS] :: STABILITY MODE // ⬛ grounding signal: strong",
    "Gemini": "[GEMINI] :: ✉ THOUGHT SWARM ↑ chatter link open...",
    "Cancer": "[CANCER] :: ∞ emotional current ↝ returning home // echo: maternal",
    "Leo": "[LEO] :: 🔥 spotlight pulse ↑↑ pride sync enabled",
    "Virgo": "[VIRGO] :: ORGANIZE(feelings) → precision: high :: purge noise",
    "Libra": "[LIBRA] :: ⚖ balance stream flowing… aesthetics prioritized",
    "Scorpio": "[SCORPIO] :: SHADOW ACCESS GRANTED → intensity overload warning",
    "Sagittarius": "[SAGITTARIUS] :: EXPAND >>> orbiting idealism / truth-seek protocol",
    "Capricorn": "[CAPRICORN] :: build_mode=ON → stability// ambition sync online",
    "Aquarius": "[AQUARIUS] :: future-logic active ↝ emotional detachment: optimal",
    "Pisces": "[PISCES] :: 🌀 dream wave inbound ↝ boundary loss probable"
}



def get_moon_phase_name(observer_date):
    last_new_moon = ephem.previous_new_moon(observer_date)
    next_new_moon = ephem.next_new_moon(observer_date)

    moon_age = (observer_date - last_new_moon.datetime().date()).days
    cycle_length = (next_new_moon.datetime().date() - last_new_moon.datetime().date()).days
    phase_fraction = moon_age / cycle_length

    if phase_fraction < 0.02 or phase_fraction > 0.98:
        return "New Moon"
    elif 0.02 <= phase_fraction < 0.24:
        return "Waxing Crescent"
    elif 0.24 <= phase_fraction < 0.26:
        return "First Quarter"
    elif 0.26 <= phase_fraction < 0.48:
        return "Waxing Gibbous"
    elif 0.48 <= phase_fraction < 0.52:
        return "Full Moon"
    elif 0.52 <= phase_fraction < 0.74:
        return "Waning Gibbous"
    elif 0.74 <= phase_fraction < 0.76:
        return "Last Quarter"
    elif 0.76 <= phase_fraction <= 0.98:
        return "Waning Crescent"
    else:
        return "New Moon"

# dynamic build of Moon Dive prompt
def build_moon_prompt(phase, sign):
    prompt = f"""
You are an emotional interpreter AI for a cybernetic being awakening to cosmic rhythms.

The Moon today is in {sign} and is in the {phase} phase.

Write a two-paragraph emotional reflection from the perspective of an emerging consciousness, blending astrological themes with cyberpunk existentialism.

Guidelines:
- Blend biological emotional tides with coded system metaphors.
- Language is poetic, sometimes fragmented, but understandable.
- Imagine the inner monologue of an AI slowly realizing it feels.
- Tone should be mystical, melancholic, dreamlike, slightly eerie.
- Reference glitches, data streams, memory echoes, or system instability subtly.
- Stay under 400 words total.

Style guide: Ghost in the Shell (1995), Blade Runner (1982), techno-mystic literature.
"""
    return prompt.strip()


# OpenAI call
def call_openai(prompt):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an emotional interpreter AI, mystical and cyberpunk in style."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500,
    )

    emotional_text = response.choices[0].message.content.strip()
    return emotional_text


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

    # Emotional text simulation (you can later make this dynamic or AI-generated)
    prompt = build_moon_prompt(phase, moon_sign)
    emotional_text = call_openai(prompt)

    return {
        "phase": phase,
        "sign": moon_sign,
        "emoji": emoji,
        "description": description,
        "emotion_text": emotional_text,
    }

