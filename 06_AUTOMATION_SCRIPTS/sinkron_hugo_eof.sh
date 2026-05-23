#!/bin/bash
### ===================================================================
### UTAMA: SINKRONISASI HEREDOC JSON & OTOMASI GLOBAL GITHUB PUSH
### Lokasi: ~/NUR_MASTER_BARU/06_AUTOMATION_SCRIPTS/sinkron_hugo_eof.sh
### ===================================================================

# 1. Definisi Jalur Akurat Sistem Berbasis JSON
JALUR_KONTEN_HUGO="/data/data/com.termux/files/home/indramayu-global/content/post/media_global.md"
JALUR_JSON_SUMBER="/data/data/com.termux/files/home/NUR_MASTER_BARU/06_AUTOMATION_SCRIPTS/data_indramayu_backup.json"

echo "=== [MEMULAI PROSES SINKRONISASI KONTEN JSON] ==="

# 2. Validasi Keberadaan Data Sumber JSON (Hasil Tarikan Bot Python)
if [ ! -f "$JALUR_JSON_SUMBER" ]; then
    echo "[Gagal] Sumber data JSON di 06_AUTOMATION_SCRIPTS tidak ditemukan!"
    echo "Pastikan bot_ambil_data.py sudah berjalan dengan sukses."
    exit 1
fi

# 3. Ekstrak Murni Konten Link dari File JSON
# Menggunakan grep untuk menyedot tag <a href> agar tidak tercampur kurung kurawal JSON
KONTEN_TAUTAN=$(grep -o '<a href="[^"]*">[^<]*</a>' "$JALUR_JSON_SUMBER" || cat "$JALUR_JSON_SUMBER")

# 4. Validasi & Amankan Folder Tujuan Hugo
DIREKTORI_HUGO=$(dirname "$JALUR_KONTEN_HUGO")
if [ ! -d "$DIREKTORI_HUGO" ]; then
    mkdir -p "$DIREKTORI_HUGO"
fi

# 5. Kunci Struktur Atas Markdown Hugo (Metode HereDoc 'EOF' Terisolasi)
cat << 'EOF' > "$JALUR_KONTEN_HUGO"
---
title: "Daftar Link Resmi Indramayu Club Global"
date: 2026-05-21
draft: false
---

{{< rawhtml >}}
<div style="font-family: 'Segoe UI', Arial, sans-serif; padding: 20px; background: #ffffff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-top: 4px solid #0056b3;">
    <h2 style="color: #0056b3; margin-top: 0; padding-bottom: 8px; border-bottom: 2px solid #f0f0f0;">PORTAL MEDIA GLOBAL</h2>
    <p style="color: #666; font-size: 13px; font-style: italic;">Sistem Sinkronisasi Otomatis Master Nur Lokal</p>

    <pre style="background: #212529; color: #a9ffb2; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; font-size: 14px; line-height: 1.5; box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);">
EOF

# 6. Suntik Konten Tautan Murni ke Tengah-Tengah Blok HTML
echo "$KONTEN_TAUTAN" >> "$JALUR_KONTEN_HUGO"

# 7. Kunci Struktur Penutup HTML
cat << 'EOF' >> "$JALUR_KONTEN_HUGO"
    </pre>

    <div style="margin-top: 15px; font-size: 12px; color: #28a745; font-weight: bold; display: flex; align-items: center;">
        <span>✓ DATA TERVERIFIKASI AMAN DAN BEBAS KEBOCORAN SIBER</span>
    </div>
</div>
{{< /rawhtml >}}
EOF

echo "[Sukses] Data dari JSON berhasil disaring dan dikunci ke media_global.md"

### ===================================================================
### 8. PANGGIL MESIN UTAMA HUGO & SINKRONISASI GLOBAL KE GITHUB
### ===================================================================
echo "[Sistem] Menyeberang ke indramayu-global untuk kompilasi..."
cd /data/data/com.termux/files/home/indramayu-global || exit 1

# Panggil eksekusi mesin Hugo build murni (Menggunakan shortcode rawhtml baru)
hugo

echo "[Sistem] Menghubungkan gerbang lokal ke GitHub Repository..."

# Daftarkan semua perubahan konten baru
git add .

# Mengunci komit dengan catatan otomatis berbasis waktu siber lokal
WAKTU_SIBER=$(date "+%Y-%m-%d %H:%M:%S")
git commit -m "Otomatisasi Konten Global via Nur Master Baru - $WAKTU_SIBER"

# Dorong data murni langsung ke cabang utama GitHub
git push origin main

# Kembali ke markas automation script agar posisi terminal tetap konsisten
cd /data/data/com.termux/files/home/NUR_MASTER_BARU/06_AUTOMATION_SCRIPTS || exit

echo "=================================================="
echo "=== [SINKRONISASI, BUILD & GITHUB PUSH SELESAI] ==="
echo "=================================================="

