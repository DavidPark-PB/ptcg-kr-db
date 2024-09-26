import json
import pprint

ALL_CARD_DIR = '../all_card_data.json'

if __name__ == "__main__":
    with open(ALL_CARD_DIR, mode='r', encoding='utf-8') as file:
        all_card_data = json.load(file)
        
    type_set_poke = set()
    
    for item in all_card_data:
        if item['supertype'] == '포켓몬':
            type_set_poke.add(item['type'])
                
    pprint.pprint(sorted(list(type_set_poke)))
    