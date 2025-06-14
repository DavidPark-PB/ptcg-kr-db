import os
import json
import requests

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

                        # ✅ 리스트 형태 JSON 방어
                        if isinstance(data, list):
                            data = data[0]

                        # set 필드 처리
                        set_id = None
                        set_value = data.get("set")
                        if isinstance(set_value, list):
                            if set_value and isinstance(set_value[0], dict):
                                set_id = set_value[0].get("id")
                            elif set_value and isinstance(set_value[0], str):
                                set_id = set_value[0]
                        elif isinstance(set_value, dict):
                            set_id = set_value.get("id")
                        elif isinstance(set_value, str):
                            set_id = set_value

                        # type 필드 처리
                        card_type = (
                            data["types"][0]
                            if isinstance(data.get("types"), list) and data["types"]
                            else None
                        )

                        card = {
                            "id": data.get("id") or data.get("set_number"),
                            "name": data.get("name"),
                            "image": data.get("image"),
                            "rarity": data.get("rarity"),
                            "set_id": set_id,
                            "type": card_type,
                            "supertype": data.get("supertype")
                        }

                        if card["id"] and card["image"]:
                            card_list.append(card)
                        else:
                            print(f"❗ card 누락: {data.get('name')}")
                except Exception as e:
                    print(f"❌ JSON 오류: {file} - {e}")
                    print(f"↪️ 원본 타입: {type(data)}")
    print(f"✅ 총 {len(card_list)}개의 카드 로드 완료")
    return card_list

cards = load_all_cards()

for i in range(0, len(cards), 50):
    chunk = cards[i:i+50]
    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}",
        headers=headers,
        json=chunk
    )
    print(f"{i}~{i+len(chunk)} 업로드 결과: {res.status_code}", res.text)
