const { GoogleGenerativeAI } = require("@google/generative-ai");
const fsg = require("fs");

// Ganti dengan API Key milikmu dari Google AI Studio
const genAI = new GoogleGenerativeAI("AIzaSyCarAUGTXAENWx56ETkTykaYmZ9pmNEQzw");
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

async function buatMarkdown() {
  const prompt = "Buat struktur organisasi dan rencana kerja mingguan dalam format markdown (.md)";

  try {
    const result = await model.generateContent(prompt);
    const text = result.response.text();

    // Menyimpan hasil langsung ke file .md
    fs.writeFileSync("output_konten.md", text);
    console.log("File output_konten.md berhasil dibuat!");
  } catch (error) {
    console.error("Terjadi kesalahan:", error);
  }
}

buatMarkdown();

