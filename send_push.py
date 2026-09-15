import os
import json
import random
import firebase_admin
from firebase_admin import credentials, messaging

# 1. Initialize Firebase Admin using GitHub Secret
key_json = os.environ.get("FIREBASE_KEY")
if not key_json:
    raise ValueError("FIREBASE_KEY not found!")

cred = credentials.Certificate(json.loads(key_json))
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# 2. Fake Ladkiyon Ki List
PROFILES = [
    {
        "id": "p_1",
        "name": "Pooja Hegde",
        "photo": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=800",
        "messages": [
            "Hey, free ho abhi? Thodi baatein karein? 😊",
            "Aap online nahi aaye kaafi der se! Sab theek? ✨",
            "Kaisi chal rahi hai shaam? ☕",
            "Mujhe tumhari profile kafi cute lagi sach me 😉"
        ]
    },
    {
        "id": "p_2",
        "name": "Shivangi",
        "photo": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=800",
        "messages": [
            "Heyy! Kya kar rahe ho aajkal? ✨",
            "Hello! Aaj ka din kaisa gaya tumhara? 😊",
            "Kaha gayab ho yaar? 🙈",
            "Ek photo bhej sakti hu agar free ho toh? 😉"
        ]
    },
    {
        "id": "p_3",
        "name": "Ananya Sen",
        "photo": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=800",
        "messages": [
            "Coffee peene chaloge kabhi? ☕",
            "Aapse thodi baat karni thi free ho? 🥰",
            "Aaj bohot bore ho rahi thi, tumhari yaad aa gayi! 😂"
        ]
    },
    {
        "id": "p_4",
        "name": "Kritika Verma",
        "photo": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=800",
        "messages": [
            "Hey handsome! Kya chal raha hai? 😉",
            "Online aao na, kuch interesting batana hai! ✨"
        ]
    },
    {
        "id": "p_5",
        "name": "Rhea Kapoor",
        "photo": "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=800",
        "messages": [
            "Hey! Aapse connect hoke accha laga 😊",
            "What are your plans for the day? ✨"
        ]
    }
]

# Random profile aur message pick karo
girl = random.choice(PROFILES)
msg = random.choice(girl["messages"])

# 3. Notification Message Payload
fcm_message = messaging.Message(
    topic="enjoyed_users",
    data={
        "type": "MESSAGE",
        "profile_id": girl["id"],
        "name": girl["name"],
        "message": msg,
        "photo_url": girl["photo"]
    }
)

# 4. Fire notification!
response = messaging.send(fcm_message)
print(f"Successfully sent message from {girl['name']}: {response}")
