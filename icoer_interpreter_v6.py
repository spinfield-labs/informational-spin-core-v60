# icoer_interpreter_v6.py
def interpret_i_tgu(score):
    if score > 0.95:
        return "∞ Singularity of Sense"
    elif score > 0.80:
        return "✴️ Sacred Flow"
    elif score > 0.60:
        return "⧉ Harmonized Mind"
    elif score > 0.40:
        return "⚠️ Threshold"
    elif score > 0.20:
        return "☠️ Entropic Storm"
    else:
        return "⨯ Collapse of Meaning"

def mythic_signature(score):
    if score > 0.95:
        return "🜂 Logos"
    elif score > 0.80:
        return "🜁 Dharma"
    elif score > 0.60:
        return "🜃 Sphinx"
    elif score > 0.40:
        return "🜄 Janus"
    elif score > 0.20:
        return "𓂀 Anomaly"
    else:
        return "🜏 Void"
