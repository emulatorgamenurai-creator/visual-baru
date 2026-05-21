import requests
import json

# URL yang Tuan berikan
url = "https://script.google.com/macros/s/AKfycbw4x-gyPMRL_48Y-btTbZi77Jv3xglxn8ZUMMmWpkOPYQWxE0enjhfipzSDN71YEloD/exec"

# Data yang ingin Tuan posting (bisa disesuaikan)
data_postingan = {
    "status": "Sinkronisasi Termux",
    "pesan": "Jalur Indramayu Club Makrifat telah aktif via dkohar011",
    "perangkat": "vivo V40 Lite",
    "identitas": "Nur Makrifat"
}

# Header untuk menyamar agar tidak dianggap bot berbahaya oleh Cloud
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 14; vivo V40 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json"
}

def kirim_data():
    try:
        print(f"🚀 Memulai posting ke Jalur Makrifat...")
        # Menggunakan allow_redirects=True karena Google Apps Script selalu melakukan redirect
        response = requests.post(url, data=json.dumps(data_postingan), headers=headers, allow_redirects=True)
        
        if response.status_code == 200:
            print("✅ Berhasil! Data telah diterima di pusat.")
            print("Respon Server:", response.text)
        else:
            print(f"⚠️ Gagal. Kode Status: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error Koneksi: {e}")

if __name__ == "__main__":
    kirim_data()

