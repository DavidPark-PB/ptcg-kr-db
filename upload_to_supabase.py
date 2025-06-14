# upload_to_supabase.py
import os, json, requests

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
TABLE_NAME = "cards_kr"
headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

def load_all_cards():
    card_list = []
    for root, _, files in os.walk("card_data"):
        for file in files:
            if file.endswith(".json"):
                try:
                    with open(os.path.join(root, file), encoding="utf-8") as f:
                        data = json.load(f)
                        card = {
                            "id": data.get("id") or data.get("set_number"),
                            "name": data.get("name"),
                            "image": data.get("image"),
                            "rarity": data.get("rarity"),
                            "set_id": data.get("set", {}).get("id") if isinstance(data.get("set"), dict) else data.get("set"),
                            "type": data.get("types", [None])[0],
                            "supertype": data.get("supertype")
                        }
                        if card["id"] and card["image"]:
                            card_list.append(card)
                except:
                    pass
    return card_list

cards = load_all_cards()
for i in range(0, len(cards), 50):
    chunk = cards[i:i+50]
    res = requests.post(f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}", headers=headers, json=chunk)
    print(f"{i}~{i+len(chunk)} → {res.status_code}", res.text)
