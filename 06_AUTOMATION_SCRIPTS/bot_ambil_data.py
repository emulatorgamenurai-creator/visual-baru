import requests

# URL Web App Tuan
url = "https://script.google.com/macros/s/AKfycbw4x-gyPMRL_48Y-btTbZi77Jv3xglxn8ZUMMmWpkOPYQWxE0enjhfipzSDN71YEloD/exec"

def jalankan_bot():
    print("🤖 Bot Nur Makrifat sedang menarik data...")
    # Menggunakan identitas browser agar tidak dicurigai Google
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 14; vivo V40 Lite)"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open("data_indramayu_backup.json", "w") as f:
            f.write(response.text)
        print("✅ Semua data berhasil diambil dan disimpan di Termux!")
    else:
        print("❌ Gagal menembus jalur.")

if __name__ == "__main__":
    jalankan_bot()

