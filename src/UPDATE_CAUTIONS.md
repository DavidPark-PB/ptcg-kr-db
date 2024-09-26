# 데이터 수정시 해야할일

1. 데이터 성형 (src/checking)
   - double_pika_roto.remove_pika_roto()
   - new_cardID.fix_cardID_ver2()
   - modify_regu.basic_energy_regu()
   - modify_regu.DP_regu()
   - modify_regu.BW_regu()
2. 제품 데이터 
   - product_info.scrape_product_info.py 돌리기
   - product_info json파일 두개 갱신
3. 데이터 결합 (src/ptcg_kr_re_classify)
   - combine_all.py
   - classify_by_product.py
   - classify_by_type.py

이걸로 DB갱신은 완료