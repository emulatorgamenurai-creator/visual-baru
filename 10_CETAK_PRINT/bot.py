import os
import shutil

# Jalur Sumber Data
JALUR_LINK_TUYUL = "../03_PROYEK_DATA/target_links/antrian_print.txt"

# Jalur Output Dua Arah
OUTPUT_PUBLIK = "print_hapus_clean.txt"
OUTPUT_ARSIP = "../01_ARSIP_PROTEKSI/print_simpan_arsip.txt"

KATA_RAHASIA = ["PASSWORD", "SECRET_KEY", "TOKEN", "API_KEY", "PRIVATE_KEY"]

def proses_dua_jalur_cetak():
    print("[Bot Cetak] Memulai pemrosesan Dua Jalur Cetak...")
    
    if not os.path.exists(JALUR_LINK_TUYUL):
        print("[Info] Antrian link kosong. Tidak ada data untuk diproses.")
        return

    with open(JALUR_LINK_TUYUL, "r") as f:
        baris_data = f.readlines()

    cetak_hapus = []   # Untuk Member / Colab / Luar (Bersih)
    cetak_simpan = []  # Untuk Arsip Internal (Lengkap)

    for baris in baris_data:
        # Jalur Simpan: Masukkan data apa adanya tanpa rekayasa untuk arsip Anda
        cetak_simpan.append(baris)
        
        # Jalur Hapus: Saring ketat sebelum dilempar ke luar
        baris_terfilter = baris
        for rahasia in KATA_RAHASIA:
            if rahasia in baris_terfilter:
                baris_terfilter = f"[SENSOR] Data rahasia internal telah dimusnahkan.\n"
        cetak_hapus.append(baris_terfilter)

    # 1. CETAK JALUR 1 (PRINT HAPUS) -> Siap kirim ke member/Colab
    with open(OUTPUT_PUBLIK, "w") as f_publik:
        f_publik.write("=== DATA RESMI INDRAMAYU CLUB (PUBLIK/MEMBER) ===\n")
        f_publik.writelines(cetak_hapus)
    print(f"[Jalur 1] SUKSES: 'Print Hapus' siap di luar -> 10_CETAK_PRINT/{OUTPUT_PUBLIK}")

    # 2. CETAK JALUR 2 (PRINT SIMPAN) -> Dikunci di folder arsip terproteksi
    os.makedirs(os.path.dirname(OUTPUT_ARSIP), exist_ok=True)
    with open(OUTPUT_ARSIP, "w") as f_arsip:
        f_arsip.write("=== ARSIP RAHASIA INTERNAL MASTER NUR (NOT FOR PUBLIC) ===\n")
        f_arsip.writelines(cetak_simpan)
    print(f"[Jalur 2] SUKSES: 'Print Simpan' terkunci di -> {OUTPUT_ARSIP}")

if __name__ == "__main__":
    proses_dua_jalur_cetak()

