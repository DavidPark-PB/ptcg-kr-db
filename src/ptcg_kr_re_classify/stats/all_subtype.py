import json
import pprint

ALL_CARD_DIR = '../all_card_data.json'

if __name__ == "__main__":
    with open(ALL_CARD_DIR, mode='r', encoding='utf-8') as file:
        all_card_data = json.load(file)
        
    subtypes_set_poke = set()
    subtypes_set_nopk = set()
    
    for item in all_card_data:
        if item['supertype'] == '포켓몬':
            #for subtype in item['subtypes']:
            subtypes_set_poke.add(', '.join(item['subtypes']))
        else:
            #for subtype in item['subtypes']:
            subtypes_set_nopk.add(', '.join(item['subtypes']))
            
        # 1진화 GX ok
        # 2진화 GX ok
        
        # M진화 (EX 아님)
        # M진화 EX
        if 'M진화' in item['subtypes']:
            if 'EX' not in item['subtypes']:
                pprint.pprint(item)
                
    pprint.pprint(sorted(list(subtypes_set_poke)))
    print("###############")
    pprint.pprint(sorted(list(subtypes_set_nopk)))
