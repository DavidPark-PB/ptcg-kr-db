# 울트라비스트 들은 subtypes에 '울트라비스트'를 추가해야한다
# 홈페이지상에는 적용되어있지 않으나, 이를 참조하는 카드가 종종 있으므로 추가하기

import json
import csv
import os
import io
import re
from collections import Counter

CARDDATA_ROOT = '../../ptcg_kr_card_data/'

def is_UB(pokemons):
    if not pokemons:
        return False
    is_ultrabeast = False
    for pokemon in pokemons:
        if (793 <= pokemon["pokedexNumber"] <= 800) or (803 <= pokemon["pokedexNumber"] <= 806):
            is_ultrabeast = True
    return is_ultrabeast

def fix_UB():
    # JSON 파일들이 저장된 디렉토리 경로
    base_directory = CARDDATA_ROOT

    # 하위 폴더를 포함하여 모든 JSON 파일에 접근
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                ub_count = 0
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    try:
                        data = json.load(json_file)
                        for item in data:
                            if is_UB(item.get('pokemons',[])):
                                item['subtypes'].append('울트라비스트')
                                ub_count += 1
                    except Exception as e:
                        print(f"Error inserting {file_path}: {e}")
                if ub_count > 0:
                    print(file_path)
                    with open(file_path,'w',encoding='utf-8') as out_file:
                        json.dump(data,out_file,ensure_ascii=False, indent =4) 

if __name__ == "__main__":
    fix_UB()