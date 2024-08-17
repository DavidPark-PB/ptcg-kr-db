# 같은 카드id에서 얼마나 중복이 있는지 가늠잡는 코드

import json
import pprint

ALL_CARD_DIR = '../all_card_data.json'

if __name__ == "__main__":
    with open(ALL_CARD_DIR, mode='r', encoding='utf-8') as file:
        all_card_data = json.load(file)
        
    dup_dict = {}
    card_count = 0
    for item in all_card_data:
        cardID = item['cardID']
        if cardID not in dup_dict:
            dup_dict[cardID] = 1
        else:
            dup_dict[cardID] += 1
        card_count += 1
        
    print(f"card_count : {card_count}")
    
    card_count_dup = 0
    for key in dup_dict:
        card_count_dup += dup_dict[key]
        
    print(f"card_count_dup : {card_count_dup}")
    print(f"number of cardId : {len(dup_dict)}")
    
    # n종류의 재록,레어수록이 있는 카드의 종류 출력
    dup_count_dict = {}
    for key in dup_dict:
        if dup_dict[key] not in dup_count_dict:
            dup_count_dict[dup_dict[key]] = [key]
        else:
            dup_count_dict[dup_dict[key]].append(key)
            
    dup_count_key_list = sorted(dup_count_dict.keys())
    for key in dup_count_key_list:
        print(f"dup {key} : {len(dup_count_dict[key])}")
        
    # 10번 이상 재록된 카드는?
    for key in dup_count_key_list:
        if key >= 10:
            print(f"dup {key} : {dup_count_dict[key]}")
    
    
    