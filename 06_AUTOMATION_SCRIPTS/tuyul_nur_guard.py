import os
import shutil

# Daftar jalur yang akan dipatroli oleh Tuyul Nur
DIREKTORI_PATROLI = [
    "/data/data/com.termux/files/home/NUR_MASTER_BARU",
    "/data/data/com.termux/files/home/BANK_MAKRIFAT_INDRAMAYU",
    "/data/data/com.termux/files/home/NUR_MASTER"
]

# Ekstensi file sampah / cache yang rawan membocorkan data mentah
SAMPAH_EKSTENSI = [".pyc", ".pyo", ".pyd", ".tmp", ".log.bak"]
FOLDER_SAMPAH = ["__pycache__", ".ipynb_checkpoints", ".cache"]

def patroli_kebocoran():
    print("=== TUYUL NUR PENJAGA: MEMULAI PATROLI SIBER LOKAL ===")
    total_file_dihapus = 0
    total_folder_dihapus = 0

    for jalur_target in DIREKTORI_PATROLI:
        if not os.path.exists(jalur_target):
            continue
            
        print(f"[Patroli] Menyisir jalur: {jalur_target}...")
        
        for akar, folder, file_file in os.walk(jalur_target):
            # 1. Sikat folder cache rahasia
            for nama_folder in list(folder):
                if nama_folder in FOLDER_SAMPAH:
                    jalur_penuh_folder = os.path.join(akar, nama_folder)
                    try:
                        shutil.rmtree(jalur_penuh_folder)
                        print(f"[BERSIH] Folder Cache Dimusnahkan: {nama_folder}")
                        total_folder_dihapus += 1
                    except Exception as e:
                        pass
            
            # 2. Sikat file sampah jejak eksekusi
            for nama_file in file_file:
                if any(nama_file.endswith(ext) for ext in SAMPAH_EKSTENSI):
                    jalur_penuh_file = os.path.join(akar, nama_file)
                    try:
                        os.remove(jalur_penuh_file)
                        print(f"[KUNCI] File Jejak Dihapus: {nama_file}")
                        total_file_dihapus += 1
                    except Exception as e:
                        pass

    print("--------------------------------------------------")
    print(f"[Sukses] Tuyul Nur berhasil mengamankan sistem.")
    print(f"[Hasil] {total_folder_dihapus} Folder Cache & {total_file_dihapus} File Jejak telah dibersihkan secara permanen!")
    print("=== SISTEM AMAN DARI KEBOCORAN CACHE ===")

if __name__ == "__main__":
    patroli_kebocoran()

