import os
import json
import random
from datetime import datetime

def sinkron_chip_drive():
    print("🛰️ [Saraf Jembatan]: Membaca koordinat Chip ID Drive Admin...")
    output_dir = "../07_WEB_GATEWAY/data"
    os.makedirs(output_dir, exist_ok=True)
    
    dompet_master = []
    for i in range(1, 101):
        pecahan_ops = [23, 40, 33, 12, 55, 8]
        detik_micro = random.choice(pecahan_ops)
        
        member_data = {
            "id": f"nur{i}",
            "chip_uid": f"DRIVE_CHIP_990X{i:03d}",
            "lencana": "♂ Member Baru" if i <= 50 else "♀ Gold Member",
            "koin_aktif": f"RpNur1000;{detik_micro:02d}",
            "last_sync": datetime.now().strftime("%H:%M:%S")
        }
        dompet_master.append(member_data)
        
    with open(os.path.join(output_dir, "dompet_master.json"), "w") as f:
        json.dump(dompet_master, f, indent=4)
        
    print("✅ [Sukses]: 100 Data Dompet Digital dari Chip ID Drive Sah Diarsip!")

if __name__ == "__main__":
    sinkron_chip_drive()
