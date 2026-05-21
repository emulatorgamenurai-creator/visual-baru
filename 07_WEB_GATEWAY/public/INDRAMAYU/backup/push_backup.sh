#!/bin/bash
# Skrip Sinkronisasi Jalur Makrifat ke GitHub

MESSAGE="Update Jalur Konfigurasi Utama: $(date +'%Y-%m-%d %H:%M:%S')"

echo "🚀 Memulai sinkronisasi ke Administrasi-Piramida..."

# Menambahkan file ke staging area
git add Auto-Backup

# Melakukan commit dengan identitas Nur Makrifat
git commit -m "$MESSAGE"

# Mendorong perubahan ke GitHub menggunakan SSH Key yang sudah Tuan buat
git push origin main

echo "✅ Berhasil! Reputasi Indramayu Club Makrifat terjaga di GitHub."

