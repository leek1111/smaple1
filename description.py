# -*- coding:utf-8 -*-

import streamlit as st

def run_description():

    st.markdown("## 대회목표 \n"
                "- 시계열 예측을 사용하여 에콰도르에 본사를 둔 대형 식료품 소매업체 '코퍼라시온 파보리타(Corporación Favorita)'의 데이터를 바탕으로 매장 매출을 예측 \n"
                "- 여러 Favorita 매장에서 판매되는 수천 가지 품목의 판매 단가를 더 정확하게 예측하는 모델을 구축함  \n"
                "-날짜, 매장 및 품목 정보, 프로모션, 판매 단가로 구성된 접근하기 쉬운 학습 데이터 세트를 통해 머신 러닝 기술을 연습 함")

    st.markdown("### 평가지표 \n"
                "- 평균제곱로그오차(Root Mean Squared Logarithmic Error) \n")
    st.latex(r'''
    {RMSLE} = \sqrt{\frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{n}}
    ''')

    st.markdown(" - $n$ : 총 인스턴스 수\n"
                " - $\hat{y}$ : 인스턴스 (i)에 대한 대상의 예측 값\n"
                " - $y_i$ : 인스턴스 (i)에 대한 대상의 실제 값\n"
                " - $log$ : 자연 로그\n"
               )
    st.markdown("### 데이터의 이해 \n"
                "- 2013년부터 2017년까지의 판매 데이터 \n"
                "-54개의 매장, 8개의 제품 카테고리/제품군(family)\n"
                "각 매장은 7일에 한 번씩 판매 데이터를 기록\n"
                "데이터에는 판매량(sales)과 기타 매장 정보(store_nbr, family, date 등)가 포함\n")
    st.markdown("### 문제해결 프로세스 \n")
