import requests

print("=== Pengecekan Bot Telegram ===")
token = input("Masukkan BOT API Token Anda (Copy-Paste dari BotFather): ").strip()

try:
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    
    if response.status_code == 401:
        print("\n[ERROR] Token tidak valid! Pastikan Anda meng-copy seluruh token dengan benar dari BotFather tanpa spasi tambahan.")
    elif response.status_code == 200:
        data = response.json()
        if not data.get("result"):
            print("\n[INFO] Bot valid, tetapi belum ada pesan masuk.")
            print("Harap buka Telegram, cari bot Anda, lalu ketik /start atau kirim pesan apa saja ke bot tersebut.")
            print("Setelah itu, jalankan ulang script ini.")
        else:
            print("\n[SUKSES] Pesan ditemukan! Berikut adalah daftar Chat ID yang pernah mengirim pesan ke bot Anda:")
            chat_ids = set()
            for item in data["result"]:
                if "message" in item:
                    chat_id = item["message"]["chat"]["id"]
                    first_name = item["message"]["chat"].get("first_name", "Unknown")
                    chat_ids.add((chat_id, first_name))
            
            for cid, fname in chat_ids:
                print(f"-> Nama: {fname} | Chat ID: {cid}")
            
            print("\nSilakan COPY angka Chat ID di atas dan masukkan ke kolom Chat ID di Grafana.")
    else:
        print(f"\n[ERROR] Terjadi masalah: {response.text}")

except Exception as e:
    print(f"Error sistem: {e}")

input("\nTekan Enter untuk keluar...")
