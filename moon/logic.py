import ephem
from datetime import datetime

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

    if phase_fraction < 0.0625:
        return "New Moon"
    elif phase_fraction < 0.1875:
        return "Waxing Crescent"
    elif phase_fraction < 0.3125:
        return "First Quarter"
    elif phase_fraction < 0.4375:
        return "Waxing Gibbous"
    elif phase_fraction < 0.5625:
        return "Full Moon"
    elif phase_fraction < 0.6875:
        return "Waning Gibbous"
    elif phase_fraction < 0.8125:
        return "Last Quarter"
    elif phase_fraction < 0.9375:
        return "Waning Crescent"
    else:
        return "New Moon"



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
    emotional_text = f"""
        Under the {phase.lower()} phase, the Moon drifts through the {moon_sign} skies.
        Emotional tides pull gently, asking you to reflect inward and embrace the hidden currents beneath your surface.

        Tonight, energies align around themes of {moon_sign.lower()} — inviting you to move slowly, to trust your instincts, and to surrender to the unspoken rhythms of change.
        """

    return {
        "phase": phase,
        "sign": moon_sign,
        "emoji": emoji,
        "description": description,
        "emotion_text": emotional_text.strip(),
    }

