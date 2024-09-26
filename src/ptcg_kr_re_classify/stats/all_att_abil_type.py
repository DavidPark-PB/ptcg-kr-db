import json
import pprint

ALL_CARD_DIR = '../all_card_data.json'

if __name__ == "__main__":
    with open(ALL_CARD_DIR, mode='r', encoding='utf-8') as file:
        all_card_data = json.load(file)
        
    att_type_set = set()
    abil_type_set = set()
    
    for item in all_card_data:
        if item['supertype'] == '포켓몬':
            for att in item['attacks']:
                if att.get('special',''):
                    att_type_set.add(att['special'])
                    
            for abil in item['abilities']:
                abil_type_set.add(abil['type'])
                if abil['type'] == '테라스탈':
                    pprint.pprint(item)
                
    pprint.pprint(sorted(list(att_type_set)))
    print("###############")
    pprint.pprint(sorted(list(abil_type_set)))
