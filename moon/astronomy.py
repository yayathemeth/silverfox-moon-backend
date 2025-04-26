import ephem

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
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
