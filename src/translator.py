# translator.py
# TR -> EN çeviri ve açıklama üretme modülü

translation_dict = {
    "İndirimli fiyat geç düşüyor": "Discounted price loads slowly",
    "Kargo ücreti yüklenmiyor": "Shipping fee is not loading",
    "Sepette indirim görünmüyor": "Discount not visible in cart",
    "Kart logosu görünmüyor": "Card logo is missing",
}

def translate_trigger(text):
    return translation_dict.get(text, text)

def behavior_en():
    return "User behavior: Missing or delayed information reduces trust."

def diagnosis_en():
    return "Diagnosis: Indicates a technical issue affecting user trust."

def action_en():
    return "Action: Fix issue, add fallback logic, monitor logs."
