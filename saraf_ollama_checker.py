import os
import requests
import json
from datetime import datetime

# Konfigurasi Saraf Ollama Lokal (Qwen 2.5 0.5B)
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:0.5b"  

# Jalur Pipeline Pabrik & Log Nur Core
PABRIK_DIR = "./05_DIGITAL_ASSETS"  
LOG_SAH_DIR = "./04_LOG_SISTEM_FOLDER"
FILE_LOG_SAH = os.path.join(LOG_SAH_DIR, "stempel_nur_core.log")

def minta_stempel_ollama(nama_file):
    """Meminta keputusan dari saraf Qwen2.5 secara lokal"""
    prompt = (
        f"Analisis file: '{nama_file}'. Jika aman dan valid untuk ekosistem "
        f"Indramayu Club Makrifat, berikan respon singkat tepat: SAH_NUR_CORE."
    )
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        # Timeout diperlebar 30 detik demi stabilitas 2500 file
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json().get("response", "").strip()
    except Exception as e:
        return f"ERROR_KONEKSI: {e}"
    return "GAGAL_VALIDASI"

def cek_pabrik_massal():
    waktu_mulai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== [UPGRADE] Saraf Ollama ({MODEL_NAME}) Aktif ===")
    
    if not os.path.exists(PABRIK_DIR):
        os.makedirs(PABRIK_DIR, exist_ok=True)

    semua_file = [f for f in os.listdir(PABRIK_DIR) if os.path.isfile(os.path.join(PABRIK_DIR, f))]
    total_file = len(semua_file)
    print(f"[PABRIK] Mendeteksi {total_file} file siap disaring oleh Nur Core.\n")

    sukses_hitung = 0
    gagal_hitung = 0
    catatan_json_log = []

    for indeks, nama_file in enumerate(semua_file, 1):
        print(f"[{indeks}/{total_file}] Memproses Saraf -> {nama_file}")
        stempel = minta_stempel_ollama(nama_file)
        
        # Penentuan status keamanan berbasis stempel
        status_keamanan = "SAH_NUR_CORE" if "SAH_NUR_CORE" in stempel else "PERINGATAN_SISTEM"
        if "ERROR_KONEKSI" in stempel:
            status_keamanan = "GAGAL_KONEKSI"
            gagal_hitung += 1
        else:
            sukses_hitung += 1

        # Struktur Log Hasil Upgrade (Format Objek JSON Terstruktur)
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "indeks": f"{indeks}/{total_file}",
            "nama_file": nama_file,
            "respon_saraf": stempel,
            "status": status_keamanan
        }
        
        # Simpan dalam format string JSON per baris
        catatan_json_log.append(json.dumps(log_entry) + "\n")

    # Tambahkan Manifes Rangkuman Akhir Pabrik (Ringkasan Eksekutif)
    waktu_selesai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    manifes_rangkuman = {
        "SINKRONISASI_MANIFES": {
            "waktu_mulai": waktu_mulai,
            "waktu_selesai": waktu_selesai,
            "total_aset_diproses": total_file,
            "total_sukses_stempel": sukses_hitung,
            "total_gagal": gagal_hitung,
            "otoritas_kontrol": "JAMHARI_DUL_KOHAR_ADMINISTRATOR"
        }
    }
    catatan_json_log.append("\n=== MANIFES RINGKASAN PABRIK ===\n" + json.dumps(manifes_rangkuman, indent=4) + "\n")

    # Amankan dan tulis ke dalam Log Sistem Folder
    with open(FILE_LOG_SAH, "a") as log_file:
        log_file.writelines(catatan_json_log)

    print(f"\n[SUKSES_UPGRADE] File log terstruktur berhasil disuntikkan ke: {FILE_LOG_SAH}")

if __name__ == "__main__":
    cek_pabrik_massal()
