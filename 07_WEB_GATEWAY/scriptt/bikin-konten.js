const { GoogleGenerativeAI } = require("@google/generative-ai");
const fs = require("fs");

// Ganti dengan API Key milikmu
const genAI = new GoogleGenerativeAI("AIzaSyCarAUGTXAENWx56ETkTykaYmZ9pmNEQzw");

async function generateMarkdown() {
  console.log("Sedang memproses konten... Mohon tunggu.");

  try {
    // Kita coba gunakan gemini-1.5-flash jika Pro sedang limit atau tidak ditemukan
    // Flash sangat cepat untuk membuat konten Markdown
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

    const prompt = "Buatlah struktur laporan manajemen digital untuk komunitas dalam format Markdown (.md).";

    const result = await model.generateContent(prompt);
    const text = result.response.text();

    fs.writeFileSync("hasil_konten.md", text);

    console.log("-----------------------------------------");
    console.log("Berhasil! File 'hasil_konten.md' telah dibuat.");
    console.log("-----------------------------------------");
  } catch (error) {
    console.error("Detail Error:", error.message);
    console.log("\nTips: Pastikan API Key sudah benar dan kuota project di Google AI Studio aktif.");
  }
}

generateMarkdown();

