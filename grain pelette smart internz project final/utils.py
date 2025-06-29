suggestions = {
    "Arborio": "Needs moderate water. Best for creamy dishes like risotto.",
    "Basmati": "Requires well-drained soil. Ideal for dry regions with irrigation.",
    "Ipsala": "High yield in wet soils. Fertilize twice a season.",
    "Jasmine": "Thrives in warm climates. Keep soil consistently moist.",
    "Karacadag": "Hardy in cooler climates. Requires less water and rich soil."
}

def get_suggestion(label):
    return suggestions.get(label.strip(), "No suggestion available for this type.")