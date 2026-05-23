import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Cakupan akses untuk Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

# Data folder berdasarkan urutan yang Anda berikan (ID diambil dari URL Drive Anda)
DRIVE_FOLDERS = [
    {"id": "1-vfSMe4HLBRw_6xgHQuzL2MaL-QsmYyT", "new_name": "INDRAMAYU_CLUB"},
    {"id": "19ezgJgH4kn7KV23NMaLsUnJVHl8PMJT_", "new_name": "DISKUSI"},
    {"id": "1v0Wc-oNUhJYHBIj9sP6KcmOXwNpHkzm_", "new_name": "ADMINISTRASI"},
    {"id": "1w4NdVPZVDbdptFT_n3mtL0zxPQ_Uveuz", "new_name": "KREATOR_DIGITAL"},
    {"id": "19sQU6y-_PD2Nj9-wRdsICh7LUyxtspia", "new_name": "GAME_ARISAN"},
    {"id": "1Gt21jF-4N-eOep5U_ZWjtYHqIjXSGvPa", "new_name": "BANK_GAME"},
    {"id": "1AY5jD0BbOZMcUW2JTq5HpbNlZQ1l3P3n", "new_name": "GAME_INDRAMAYU"},
    {"id": "15pynM8x7bca0deCVLjW6BhyqW5lQZ76s", "new_name": "KOMUNIKASI"},
    {"id": "1D2jx-VV-AkPwc6rUtvabthyYc61Lw7Ti", "new_name": "BACKUP"},
    {"id": "1nM6UeY60YU0-WTynteXVjKw9W-s3F-7I", "new_name": "ALWI_INDRAMAYU_CLUB"}
]

def get_drive_service():
    creds = None
    # File token.json menyimpan token akses pengguna
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Jika tidak ada kredensial yang valid, lakukan login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

def rename_folders():
    try:
        service = get_drive_service()
        print("=== Memulai Perubahan Nama Folder Google Drive ===")
        
        for folder in DRIVE_FOLDERS:
            folder_id = folder["id"]
            new_name = folder["new_name"]
            
            # Struktur body untuk update nama metadata di Google Drive
            file_metadata = {'name': new_name}
            
            try:
                # Eksekusi perubahan nama menggunakan Drive API
                updated_file = service.files().update(
                    fileId=folder_id,
                    body=file_metadata,
                    fields='id, name'
                ).execute()
                print(f"[SUKSES] Folder ID {folder_id} berhasil diubah menjadi -> {updated_file.get('name')}")
            except Exception as folder_error:
                print(f"[GAGAL] Tidak dapat mengubah Folder ID {folder_id}. Error: {folder_error}")
                
        print("=== Proses Selesai ===")
    except Exception as e:
        print(f"[ERROR SISTEM] Gagal menjalankan fungsi: {e}")

if __name__ == '__main__':
    rename_folders()

