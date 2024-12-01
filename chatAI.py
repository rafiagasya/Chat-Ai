# Program Curhat dengan AI Sederhana
import time

def chatbot_response(user_input):
    # Daftar respons sederhana
    responses = {
        "sedih": "Kenapa sedih kamu padahal kan aku baik hehehe. Kalo mau curhat ke aku ajah yah",
        "senang": "Wah, kok bsia seanang cokkk gimana caranya kasih tau lahh asuuuu!",
        "marah": "Gak usah di pikiran perselingkuhan mah santai ajah yahh?",
        "bingung": "Apa yang bikin kamu bingung? Coba aku bantu ya.",
        "lelah": "Gak usah istirahat cokkk laki-laki harus kuat asuuuu.",
        "default": "Mong Ahhh,,! kamu nya kayak gitu sama aku hehehe."
    }
    
    # Mencari kata kunci untuk merespons
    for keyword in responses:
        if keyword in user_input.lower():
            return responses[keyword]
    return responses["default"]

# Program utama
print("=== Chat dengan AI ===")
print("Halo Raffi! Aku di sini untuk mendengarkan. Ceritakan apa yang kamu rasakan.")
while True:
    user_input = input("Kamu: ")
    if user_input.lower() in ["bye", "selesai", "exit", "keluar"]:
        print("AI: Baik Raffi, sampai jumpa lagi. Jangan ragu untuk curhat kapanpun ya!")
        break
    response = chatbot_response(user_input)
    print("AI:", response)
    time.sleep(1)
