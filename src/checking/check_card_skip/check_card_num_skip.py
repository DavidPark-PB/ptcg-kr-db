# 중간중간에 번호가 비는게 있는데 뭔지 확인하기
import json

TARGET_PATH = '../../ptcg_kr_card_data/BS/2022/BS_2022_001_278.json'

if __name__ == "__main__":
    with open(TARGET_PATH,'r',encoding='utf-8') as f:
        data = json.load(f)
      
    num_set = set()
    for item in data:
        num_set.add(int(item['number']))
        
    num_list = sorted(list(num_set))
    list_290 = list(range(291))
    
    for num in num_list:
        list_290.remove(num)
        
    print(list_290)