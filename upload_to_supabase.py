import os
import json
import requests

# 환경변수로부터 Supabase 정보 가져오기
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
TABLE_NAME = "cards_kr"

# 요청 헤더 설정
headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

# 카드 데이터를 로드하는 함수
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
                            "set_id": (
