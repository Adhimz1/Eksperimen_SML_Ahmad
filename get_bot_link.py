import requests
token = "8364586877:AAEHG39jYW83XHU8QVP9P_0L8B65HYrxT9o"
try:
    res = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()
    if res.get("ok"):
        username = res["result"]["username"]
        print(f"BOT_LINK: https://t.me/{username}")
    else:
        print("Invalid token")
except Exception as e:
    print(str(e))
