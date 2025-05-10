
import requests
import time

# توکن ربات شما
TOKEN = "267075:babf48ab-fea6-4d00-8bfa-6f5d1b154e57"
URL = f"https://eitaayar.ir/bot{TOKEN}/"

# تابع ارسال پیام
def send_message(chat_id, text):
    data = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(URL + "sendMessage", data=data)

# دریافت آپدیت‌ها
def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    response = requests.get(URL + "getUpdates", params=params)
    return response.json()

# پیام دعوت
invite_link = "https://eitaa.com/karimeahle_beit"
message = f"""سلام! برای عضویت در کانال، روی لینک زیر کلیک کن:
{invite_link}"""

# اجرای اصلی ربات
def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if "result" in updates:
            for update in updates["result"]:
                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    send_message(chat_id, message)
                    last_update_id = update["update_id"] + 1
        time.sleep(1)

if __name__ == "__main__":
    main()
