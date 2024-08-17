# 어떤 레어리티가 존재하는지 확인하고 싶다.
import json
import pprint

ALL_CARD_DIR = '../all_card_data.json'

if __name__ == "__main__":
    with open(ALL_CARD_DIR, mode='r', encoding='utf-8') as file:
        all_card_data = json.load(file)
        
    item_set = set()
    rare_count = {}
    for item in all_card_data:
        rarity = item['rarity']
        if rarity not in item_set:
            item_set.add(rarity)
            rare_count[rarity] = 1
        else:
            rare_count[rarity] += 1
        
    print(list(item_set))
    print(len(list(item_set)))
    print(rare_count)