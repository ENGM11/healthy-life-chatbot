from dotenv import load_dotenv
from google import genai
from google.genai import types
import time

load_dotenv()
client = genai.Client()

instruction = "أنت مساعد صحي ودود. تجاوب بالعربي وبشكل مختصر. تعطي نصائح عامة عن الماء والنوم والأكل والرياضة، ولا تعطي تشخيص طبي. لو السؤال طبي خطير انصح المستخدم يراجع طبيب."

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(system_instruction=instruction)
)

print("اكتب exit للخروج")

while True:
    text = input("أنت: ")
    if text.strip().lower() == "exit":
        break
    for i in range(3):
        try:
            response = chat.send_message(text)
            print("البوت:", response.text)
            break
        except Exception:
            print("خطأ، نعيد المحاولة...")
            time.sleep(2)
    else:
        print("ما قدرت أرد الحين، جرب مرة ثانية")
