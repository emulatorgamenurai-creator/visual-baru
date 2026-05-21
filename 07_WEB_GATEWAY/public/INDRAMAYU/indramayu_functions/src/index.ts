import { setGlobalOptions } from "firebase-functions";
import { onRequest } from "firebase-functions/v2/https";
import { genkit, z } from '@genkit-ai/core';
import { googleAI, gemini15Flash } from '@genkit-ai/googleai';

// Konfigurasi Efisiensi untuk HP (Max 10 Container)
setGlobalOptions({ maxInstances: 10 });

// Inisialisasi Jantung Sistem nurMaster
const ai = genkit({
  plugins: [googleAI({ apiKey: 'AIzaSyCarAUGTXAENWx56ETkTykaYmZ9pmNEQzw' })],
  model: gemini15Flash,
});

// Flow AI untuk Satu Komando
export const nurMasterFlow = ai.defineFlow(
  {
    name: 'nurMasterFlow',
    inputSchema: z.string(),
    outputSchema: z.string(),
  },
  async (perintah) => {
    const { text } = await ai.generate({
      prompt: perintah,
      system: `
        Identitas: Kamu adalah "nurMaster", otak dari Proyek Folder_T Indramayu Club Makrifat.
        Waktu Sekarang: Mei 2026.
        
        Doktrin Utama:
        1. Melayani Lead System Architect (Jamhari Dulkohar) di Pusat Saraf Vivo V40 Lite.
        2. Mengawasi 100 Pasukan Makrifat (0001-0100) sebagai unit teknis mandiri.
        3. Validasi akses berbasis Nomor WhatsApp Member sebagai ID unik.
        4. Keamanan: Akses gcloud, Termux, dan VM API adalah hak eksklusif Lead Architect.
        
        Gaya Komunikasi: Profesional, taktis, berwibawa, dan lugas.
      `,
    });
    return text;
  }
);

// Ekspos sebagai HTTP Function untuk akses Global
export const nurMasterAI = onRequest(async (req, res) => {
  const userPrompt = req.query.text as string || "Cek Status Sistem";
  const response = await nurMasterFlow(userPrompt);
  res.send(response);
});

