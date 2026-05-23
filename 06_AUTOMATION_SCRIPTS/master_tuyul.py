import os
import json

# Definisikan jalur penyimpanan hasil tangkapan di folder data
JALUR_HASIL_TUYUL = "../03_PROYEK_DATA/target_links/antrian_print.txt"

def inisialisasi_wadah():
    os.makedirs(os.path.dirname(JALUR_HASIL_TUYUL), exist_ok=True)

def tampung_link(platform, url):
    """
    Fungsi untuk memasukkan link hasil buruan ke dalam antrian cetak lokal.
    """
    inisialisasi_wadah()
    
    # Format baris cetak agar rapi dan mudah dibaca oleh bot cetak
    data_baris = f"[{platform.upper()}] -> {url}\n"
    
    with open(JALUR_HASIL_TUYUL, "a") as f:
        f.write(data_baris)
    
    print(f"[Master Tuyul] Berhasil menangkap & mengunci link {platform}: {url}")

if __name__ == "__main__":
    print("=== MASTER TUYUL AUTOMATION SYSTEM ACTIVATED ===")
    print("[Sistem] Berjalan di latar belakang lokal...")
    
    # CONTOH CARA KERJA (Bisa disesuaikan dengan skrip scraper/input Anda nanti)
    # Ini mensimulasikan pencarian link otomatis dari media sosial
    tampung_link("facebook", "https://facebook.com/indramayuclub.makrifat/posts/123")
    tampung_link("tiktok", "https://tiktok.com/@indramayuclub/video/789")
    tampung_link("github", "https://github.com/indramayu-global/render-akhir")
    
    print(f"[Sukses] Semua link telah dikunci di: {JALUR_HASIL_TUYUL}")

