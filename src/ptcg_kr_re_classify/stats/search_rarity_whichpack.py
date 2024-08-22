# 어떤 레어리티가 존재하는지 확인하고 싶다.
import json
import pprint

ALL_CARD_DIR = '../all_card_data.json'

if __name__ == "__main__":
    with open(ALL_CARD_DIR, mode='r', encoding='utf-8') as file:
        all_card_data = json.load(file)
        
    rarity_dict = {}
        
    for item in all_card_data:
        rarity = item['rarity']
        prod = item['prodName']
        if rarity not in rarity_dict:
            rarity_dict[rarity] = set([prod])
        else:
            rarity_dict[rarity].add(prod)
            
        if rarity == 'UR':
            print(item['name'])
            
    rarity_dict['C'] = set()
    rarity_dict['R'] = set()
    rarity_dict['U'] = set()
    rarity_dict['N'] = set()
    rarity_dict['RR'] = set()
    rarity_dict['SR'] = set()
    rarity_dict['RRR'] = set()



    pprint.pprint(rarity_dict)
