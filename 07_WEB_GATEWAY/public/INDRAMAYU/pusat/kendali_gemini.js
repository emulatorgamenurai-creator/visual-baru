const fs = require('fs');

// Konfigurasi Dasar Indramayu Club Makrifat
const config = {
    project: "Indramayu_Project",
    status: "Offline Mode (Kalimantan)",
    member_prefix: "nur"
};

function cekStatusArsip() {
    console.log("=== Memulai Pengecekan Sistem Gemini ===");
    console.log("Status: " + config.status);
    
    // Cek opo file ZIP-e ono
    if (fs.existsSync('../Indramayu_Arsip_Proteksi.zip')) {
        console.log("[OK] Brankas ZIP ketemu.");
    } else {
        console.log("[WARNING] Brankas ZIP ora ketemu!");
    }

    // Cek folder public kanggo localhost
    if (fs.existsSync('../public')) {
        const files = fs.readdirSync('../public');
        console.log("[OK] Folder Public siap nggo Localhost. Isine: " + files.length + " file.");
    }
}

cekStatusArsip();
console.log("=== Gemini Standby nunggu Perintah Sabanjure ===");
