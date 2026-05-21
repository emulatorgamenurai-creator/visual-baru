const { GoogleGenerativeAI } = require("@google/generative-ai");

// Ganti "API_KEY_ANDA" dengan kunci API Gemini yang valid
const genAI = new GoogleGenerativeAI("AIzaSyA4xP7WSh1jA1I7wmz3HtXVTBKClWZw-TM");
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

async function run() {
  const prompt = "Halo Gemini, perkenalkan dirimu secara singkat.";

  try {
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
  } catch (error) {
    console.error("Terjadi kesalahan:", error);
  }
}

run();

