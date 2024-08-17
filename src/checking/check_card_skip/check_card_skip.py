# 카드팩이나 덱의 데이터를 보면 원래는 165/100 이 마지막 카드인데
# 121/100 까지밖에 없거나 하는 경우가 있다.
# 우선, 모든 상품에 대해 가장 마지막카드의 상품번호가 어떤 형태인지 확인하자
# 시리즈, 상품명, 마지막번호, 카드종류 이렇게 csv로 출력해서 읽어보자
# 덱은 볼필요 없음

import os
import json
import csv

def get_series(name):
    if 'BW' in name:
        return 'BW'
    elif 'XY' in name:
        return 'XY'
    elif '썬&문' in name:
        return 'SM'
    elif '소드&실드' in name:
        return 'S'
    elif '스칼렛&바이올렛' in name:
        return 'SV'
    elif 'M' in name:
        return 'XY'
    else:
        return 'x'

TARGET_DIR = '../../../card_data_product/pack/'
CSV_PATH = './result.csv'

if __name__ == '__main__':
    csv_data = []
    
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                print(file_path)
                try:
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                        num_set = set()
                        prodNum_set = set()
                        
                        for item in data:
                            num_set.add(int(item['number']))
                            prodNum_set.add(int(item['prodNumber']))
                            
                        csv_item = []
                        csv_item.append(get_series(data[0]['prodName']))
                        csv_item.append(data[0]['prodName'])
                        csv_item.append(max(num_set))
                        csv_item.append(max(prodNum_set))
                        if max(num_set) <= max(prodNum_set):
                            csv_item.append('check')
                        else:
                            csv_item.append('okay')
                            
                        csv_data.append(csv_item)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    
    with open(CSV_PATH, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for item in csv_data:
            writer.writerow(item)