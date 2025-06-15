import os
import json
import requests

# 카드 데이터 디렉토리 경로
card_data_dir = './card_data'

# 이미지 저장 디렉토리
image_save_dir = './card_images'

# 디렉토리가 없으면 생성
os.makedirs(image_save_dir, exist_ok=True)

# 카드 데이터 파일 목록
card_files = [f for f in os.listdir(card_data_dir) if f.endswith('.json')]

for card_file in card_files:
    with open(os.path.join(card_data_dir, card_file), 'r', encoding='utf-8') as f:
        card_data = json.load(f)
        card_id = card_data.get('id')
        image_url = card_data.get('image_url')

        if card_id and image_url:
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                with open(os.path.join(image_save_dir, f'{card_id}.jpg'), 'wb') as img_file:
                    img_file.write(response.content)
                print(f'✅ {card_id} 이미지 저장 완료')
            except Exception as e:
                print(f'❌ {card_id} 이미지 다운로드 실패: {e}')
        else:
            print(f'⚠️ {card_file}에 필요한 정보가 없습니다.')
