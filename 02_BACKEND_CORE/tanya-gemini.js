const { GoogleGenAI } = require("@google/genai");

// Memasukkan API Key baru dari Google AI Studio
const API_KEY = "AQ.Ab8RN6KAzKbS7HMkm8hIugMdgxJqe_THuzKMsK4Mk2BT8mx6Ig";

// Inisialisasi kecerdasan buatan Gemini dengan key baru
const ai = new GoogleGenAI({ apiKey: API_KEY });

async function jalankanSaraf() {
    try {
        console.log("==================================================");
        console.log(" MENGHUBUNGKAN KE PUSAT SARAF INDRAMAYU CLUB... ");
        console.log("==================================================");

        const response = await
         ai.models.generateContent({
            model: "gemini-2.5-flash", // Menggunakan model standar infrastruktur Anda
            contents: "Sistem otomasi Gemini di Termux berhasil terhubung menggunakan API Key baru. Berikan konfirmasi kesiapan sistem digital Indramayu Club!",  });        
        console.log("\n[RESPONS AI GEMINI]:");
        console.log(response.text);
        console.log("==================================================");
    } catch (error) {
        console.error("\nGagal mengaktifkan saraf AI:", error.message);
    }
}

jalankanSaraf();

