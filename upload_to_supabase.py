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
                        else:
                            print(f"❗ card 누락: {data.get('name')}")
                except Exception as e:
                    print(f"❌ JSON 오류: {file} - {e}")
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
