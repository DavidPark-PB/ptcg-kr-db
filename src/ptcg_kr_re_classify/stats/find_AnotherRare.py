# 특일 SR,HR중에 일러가 공개된것들 찾아보기
# 같은 상품내에서 SR, HR 같은카드가 따닥으로 나오면 그게 특일
import json
import os

CARD_DIR = '../../../card_data_product/'

if __name__ == "__main__":
    for root, dirs, files in os.walk(CARD_DIR):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                        
                        ASR_flag = False
                        AHR_flag = False
                        for item in data:
                            if item['rarity'] == 'HR':
                                if not AHR_flag:
                                    AHR_flag = item['name']
                                else:
                                    if item['name'] == AHR_flag:
                                        print(f"{item['name']} : {item['prodName']} : {item['cardImgURL']}")
                                        AHR_flag = False
                            

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")