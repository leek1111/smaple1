# -*- coding:utf-8 -*-

import pandas as pd

# Date Selection
def date_select(data, col):
    data[col] = pd.to_datetime(data[col])
    data['year'] = data[col].dt.year
    data['month'] = data[col].dt.month
    data['day'] = data[col].dt.day

    new_df = data.loc[data['year'].isin([2015, 2016]), :]
    return new_df

home_html="""


# 매출 분석 프로젝트

### 언어 및 작업툴, 사용 라이브러리


### 기간
-  2023.04.27 ~ 2023.05.17



### 내용

 ▼ 목표

	👉 머신러닝, 시계열 분석으로 재고 관리의 효율성 높이기

	□ 매출 데이터 수집 및 정리

	□ 매출 데이터 시각화

	□ 매출 추세 분석

	□ 판매 단가 예측 모델링

	□ 매출 향상을 위한 전략 및 제안서 작성



###  팀원별 파트소개

- 최 정 안 : 기획 및 분석, 총괄  
- 최 재 명 : 
- 권 용 석 :
- 윤 용 준 :
- 이 건 용 :
- 이 경 철 :
"""