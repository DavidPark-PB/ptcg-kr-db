# 가장 많은 종류의 레어리티를 가지는 포켓몬은?

import json
import pprint

ALL_CARD_DIR = '../all_card_data.json'

if __name__ == "__main__":
    with open(ALL_CARD_DIR, mode='r', encoding='utf-8') as file:
        all_card_data = json.load(file)
        
    rare_dict = {}
    for item in all_card_data:
        if item['supertype'] != '포켓몬':
            continue
        else:
            for pokemon in item['pokemons']:
                if pokemon['name'] not in rare_dict.keys():
                    rare_dict[pokemon['name']] = set([item['rarity']])
                else:
                    rare_dict[pokemon['name']].add(item['rarity'])
                    
    best_poke = ''
    best_rare_num = 0
    for key in rare_dict:
        if len(rare_dict[key]) > best_rare_num:
            best_poke = key
            best_rare_num = len(rare_dict[key])
            
    for key in rare_dict:
        if len(rare_dict[key]) == best_rare_num:
            print(key)
            
    print(best_poke)
    print(best_rare_num)
    print(rare_dict[best_poke])
                
    # 가장 레어도 종류가 많은건 리자몽, 피카츄, 뮤츠, 뮤 가 12종
    # 각각이 어떤 레어도 있는지 출력
    
    print('리자몽')
    print(sorted(list(rare_dict['리자몽'])))
    print('피카츄')
    print(sorted(list(rare_dict['피카츄'])))
    print('뮤츠')
    print(sorted(list(rare_dict['뮤츠'])))
    print('뮤')
    print(sorted(list(rare_dict['뮤'])))
    
    # U 레어인 뮤 찾기
    for item in all_card_data:
        if item['supertype'] != '포켓몬':
            continue
        else:
            for pokemon in item['pokemons']:
                if pokemon['name'] == '뮤':
                    if item['rarity'] == 'U':
                        pprint.pprint(item)
                        
    
    # CSR 카운트
    csr_count = 0
    for item in all_card_data:
        if item['supertype'] != '포켓몬':
            continue
        else:
            for pokemon in item['pokemons']:
                if item['rarity'] == 'CSR':
                    csr_count += 1
                    
    print(csr_count)
                    
    

    