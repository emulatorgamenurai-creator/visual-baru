// post_makrifat.ts
// Skrip untuk mengirim data ke Endpoint API tanpa memicu peringatan Apps Script

const targetUrl = 'https://URL_API_FIREBASE_ATAU_CLOUDFLARE_ANDA';

async function kirimPostingan() {
    const payload = {
        title: "Update Indramayu Club Makrifat",
        message: "Sistem telah dibersihkan dan disinkronkan via Termux.",
        timestamp: new Date().toISOString(),
        author: "Lead System Architect"
    };

    try {
        const response = await fetch(targetUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'User-Agent': 'Indramayu-System-Gateway/2.0' // Menyamar agar tidak diblokir
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            console.log("✅ Berhasil Posting: Jalur Makrifat Terbuka!");
        } else {
            console.log("❌ Gagal Posting:", response.statusText);
        }
    } catch (error) {
        console.error("⚠️ Error Koneksi:", error);
    }
}

kirimPostingan();

