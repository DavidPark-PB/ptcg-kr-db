import json
import pprint

ALL_CARD_DIR = '../all_card_data.json'

if __name__ == "__main__":
    with open(ALL_CARD_DIR, mode='r', encoding='utf-8') as file:
        all_card_data = json.load(file)
        
    rule_set = set()
    subtype_set = set()
    
    for item in all_card_data:
        if item['rules']:
            for rule in item['rules']:
                if 'BREAK' in rule:
                    print(len(item['rules']))
                    for subtype in item['subtypes']:
                        subtype_set.add(subtype)
                        
                
    rule_list = sorted(list(rule_set))
    
    for item in rule_list:
        print(item)
    
    pprint.pprint(sorted(list(subtype_set)))