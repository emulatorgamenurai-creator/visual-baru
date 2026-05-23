import os

# Target eksekusi di folder saat ini (NUR_MASTER_BARU)
TARGET_DIR = "."

# Pemetaan urutan folder sesuai daftar Anda (Format: "Nama_Folder_Baru": "Catatan_Gmail")
STRUKTUR_BARU = [
    ("01_INDRAMAYU_CLUB", "indramayuclubmakrifat@gmail.com"),
    ("02_DISKUSI", "dkohar011@gmail.com"),
    ("03_ADMINISTRASI", "imahazzah51@gmail.com"),
    ("04_KREATOR_DIGITAL", "kurnadibewok3311@gmail.com"),
    ("05_GAME_ARISAN", "motherainur8@gmail.com"),
    ("06_BANK_GAME", "banggamenurai@gmail.com"),
    ("07_GAME_INDRAMAYU", "emulatorgamenurai@gmail.com"),
    ("08_KOMUNIKASI", "aimininurindramayu@gmail.com"),
    ("09_BACKUP", "nurindramayuaimini@gmail.com"),
    ("10_ALWI_INDRAMAYU_CLUB", "alwi.indramayuclub@gmail.com")
]

def proses_struktur():
    print("=== Memulai Manajemen Folder Lokal NUR_MASTER_BARU ===")
    
    # Ambil daftar folder yang saat ini ada di direktori
    item_saat_ini = os.listdir(TARGET_DIR)
    
    for urutan, (nama_folder, gmail) in enumerate(STRUKTUR_BARU, 1):
        # Cari versi folder lama tanpa nomor (misal: "INDRAMAYU_CLUB")
        nama_lama_tanpa_nomor = nama_folder.split("_", 1)[1] if "_" in nama_folder else nama_folder
        
        jalur_lama = os.path.join(TARGET_DIR, nama_lama_tanpa_nomor)
        jalur_baru = os.path.join(TARGET_DIR, nama_folder)
        
        # 1. Jika folder lama tanpa nomor ditemukan, ubah namanya jadi berurutan
        if nama_lama_tanpa_nomor in item_saat_ini and os.path.isdir(jalur_lama):
            try:
                os.rename(jalur_lama, jalur_baru)
                print(f"[RENAME] {nama_lama_tanpa_nomor} -> {nama_folder} ({gmail})")
            except Exception as e:
                print(f"[GAGAL RENAME] {nama_lama_tanpa_nomor}: {e}")
                
        # 2. Jika folder dengan nomor sudah ada, biarkan saja (sudah konsisten)
        elif nama_folder in item_saat_ini and os.path.isdir(jalur_baru):
            print(f"[KONSISTEN] Folder {nama_folder} sudah siap.")
            
        # 3. Jika belum ada sama sekali, buat folder baru sesuai urutan
        else:
            try:
                os.makedirs(jalur_baru, exist_ok=True)
                print(f"[BUAT BARU] Berhasil membuat: {nama_folder} ({gmail})")
            except Exception as e:
                print(f"[GAGAL BUAT] {nama_folder}: {e}")

    print("=== Proses Sinkronisasi Selesai ===")

if __name__ == "__main__":
    proses_struktur()

