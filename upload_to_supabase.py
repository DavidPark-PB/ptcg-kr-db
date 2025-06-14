import os
import json
import requests

# Supabase 연결 정보
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
TABLE_NAME = "cards_kr"

# Supabase 요청 헤더
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

                        # 리스트 방어
                        if isinstance(data, list):
                            data = data[0]

                        # set_id 추출
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

                        # type 추출
                        card_type = (
                            data["types"][0]
                            if isinstance(data.get("types"), list) and data["types"]
                            else None
                        )

                        # ID 우선순위: id > set_number > 파일명
                        card_id = data.get("id") or data.get("set_number") or file.replace(".json", "")

                        # 🔥 이미지 경로 직접 생성 (GitHub raw 주소 기준)
                        card_image = f"https://raw.githubusercontent.com/DavidPark-PB/ptcg-kr-db/main/card_img/img/{file.replace('.json', '.jpg')}"

                        card = {
                            "id": card_id,
                            "name": data.get("name"),
                            "image": card_image,
                            "rarity": data.get("rarity"),
                            "set_id": set_id,
                            "type": card_type,
                            "supertype": data.get("supertype")
                        }

                        card_list.append(card)

                except Exception as e:
                    print(f"❌ JSON 오류: {file} - {e}")
    print(f"✅ 총 {len(card_list)}개의 카드 로드 완료")
    return card_list

# 카드 업로드
cards = load_all_cards()

for i in range(0, len(cards), 50):
    chunk = cards[i:i+50]
    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}",
        headers=headers,
        json=chunk
    )
    print(f"{i}~{i+len(chunk)} 업로드 결과: {res.status_code}", res.text)
