#!/bin/bash

# Identitas
echo "=========================================="
echo "   COMMANDER: TUAN JAMHARI (000555)       "
echo "   UNIT: INDRAMAYU CLUB MAKRIFAT          "
echo "=========================================="

echo "1. Backup Semua Folder (Arsip/Digital/Game)"
echo "2. Push Edit ke GitHub (Website Update)"
echo "3. Cek Status Mesin (Node/Hugo)"
echo "4. Keluar"
read -p "Pilih Aksi [1-4]: " aksi

case $aksi in
    1)
        echo "Menjalankan Backup ke folder Arsip..."
        # Menghubungkan ke 5 folder Drive yang tadi
        cp -r content/ arsip/digital_kreator/
        cp -r data/ arsip/administrasi/
        echo "Backup Selesai!"
        ;;
    2)
        echo "Melakukan Push ke GitHub..."
        git add .
        git commit -m "Update otomatis dari Master Lab"
        git push origin main
        echo "Data berhasil terkirim ke Cloud!"
        ;;
    3)
        echo "Status Port Aktif:"
        netstat -tuln | grep LISTEN
        ;;
    4)
        exit
        ;;
    *)
        echo "Pilihan salah."
        ;;
esac
