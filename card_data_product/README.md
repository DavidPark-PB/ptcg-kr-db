# 개요

본 디렉토리는 카드의 정보를 "발매제품" 끼리 묶어서 분류합니다.
즉, "확장팩 어쩌고" 에 포함되는 모든 카드 각각의 상세정보를 한 파일에 저장합니다.

# 디렉토리 구조 설명

이하와 같은 디렉토리 구조를 가집니다.
> ./{제품타입}/{시리즈}/{제품코드}.json

각 변수의 의미는 다음과 같습니다.
- 제품타입 : pack, deck, special, promo(엄밀히 말하면 제품은 아니나)
- 시리즈 : DP, BW, XY, SM, S, SV, none 으로 Bulbapedia 기준으로 분류합니다. none에는 분류가 어려운것들을 넣습니다.
- 제품코드 : BW-3, SV5a 같은 것을 의미합니다. 각 카드 상세정보의 "prodCode" 에 저장되어있습니다.

제품타입이 promo라면 시리즈 생략하고 {시리즈}-P.json 을 생성
