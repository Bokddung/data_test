import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import matplotlib.font_manager as fm
import numpy as np

# 백그라운드 이미지 추가
def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiUV_FJa-4yBvSteei5KbAF386UI_i_-Hx4A&usqp=CAU");
            background-size: cover;  # 이미지가 전체 화면을 덮도록 설정
            background-position: center;  # 이미지가 중앙에 위치하도록 설정
            background-repeat: no-repeat;  # 이미지가 반복되지 않도록 설정
        }
        h1 {
            color: brown;  # 제목 색상 변경
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# 데이터 로드 및 캐싱
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("Coffee Shop Sales.xlsx")  # 파일 경로 확인
    except FileNotFoundError:
        st.error("데이터 파일을 찾을 수 없습니다. 경로를 확인하세요.")
        return None

    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df.drop(columns=["transaction_id", "store_id", "product_id", "product_detail"], inplace=True)
    df["year"] = df["transaction_date"].dt.year
    df["month"] = df["transaction_date"].dt.month_name()
    df["day"] = df["transaction_date"].dt.day_name()
    df["hour"] = df["transaction_time"].apply(lambda x: x.hour)
    df.drop(columns='transaction_time', inplace=True)
    df["Total revenue"] = df["transaction_qty"] * df["unit_price"]
    return df

# 카운트플롯 생성 함수
def plot_countplot(df, x_col, hue=None, title=None, order=None, figsize=(12, 8)):
    fig = plt.figure(figsize=figsize)
    sns.countplot(data=df, x=x_col, hue=hue, order=order, palette="YlGnBu")
    plt.title(title)
    return fig

# 메인 함수
def main():

    # 배경 이미지 추가
    add_bg_from_url()

    st.title("커피 숍 판매 데이터 분석")
    st.markdown("이 앱은 커피 숍의 판매 데이터를 분석하고 다양한 시각화를 제공합니다.")

    # 이미지를 추가하여 앱의 시각적 요소 강화
    st.image("cafe2.jpg",use_column_width=True,width=100)

    # 데이터 로드
    st.title('커피 숍 판매 데이터')
    df = load_data() 

    if st.button('정리된 데이터 보기'):
        st.dataframe(df)
    
    if df is None:
        return  # 데이터 로드 오류 시 종료

    # 사이드바 설정
    with st.sidebar:
        start_date = st.date_input(
            "조회 시작일을 선택하세요",
            value=datetime.date(2023, 1, 1),
            min_value=df["transaction_date"].min().date(),
            max_value=df["transaction_date"].max().date()
        )

        end_date = st.date_input(
            "조회 종료일을 선택하세요",
            value=datetime.date(2023, 6, 30),
            min_value=start_date,
            max_value=(df["transaction_date"].max().date())
        )

        if start_date > end_date:
            st.warning("시작 날짜가 종료 날짜보다 늦습니다. 다시 선택하세요.")

        # 데이터 출처 및 컬럼 설명
        if st.button("데이터 출처"):
            st.write(
                '<a href="https://www.kaggle.com/code/ahmedabbas757/coffee-shop-sales/notebook">사이트 이동</a>',
                unsafe_allow_html=True,
            )

        with st.expander("컬럼 설명"):
            st.write("컬럼 설명:")
            st.markdown("""
            - **transaction_date**: 거래 날짜
            - **transaction_qty**: 판매된 품목 수량
            - **store_location**: 커피숍 위치
            - **unit_price**: 판매된 제품 가격
            - **product_category**: 제품 카테고리
            """)

        selected_charts = st.multiselect(
            "비교할 차트를 선택하세요",
            ["월별 판매량", "요일별 판매량", "매장별 시간대 판매량", "제품 카테고리별 판매량", "매장별 판매 비율", "매장별 총 판매량", "월별 총 수익"]
        )

    # 사이드바에 URL로부터 이미지 추가
    st.sidebar.image(
    "https://marketplace.canva.com/EAF0HJ0HKtw/1/0/1131w/canva-%ED%99%94%EC%9D%B4%ED%8A%B8-%EB%AA%A8%EB%8D%98%ED%95%9C-%EC%B9%B4%ED%8E%98-%EB%A9%94%EB%89%B4%ED%8C%90-BAOqYK20oyI.jpg",  # 이미지 URL
    use_column_width=True  # 열 너비에 맞춰 이미지 조절
)


    # 선택된 날짜 범위 내의 데이터 필터링
    filtered_df = df[
        (df["transaction_date"].dt.date >= start_date) &
        (df["transaction_date"].dt.date <= end_date)
    ]

    # 멀티셀렉트 사용하여 차트들 한번에 보기
    if "월별 판매량" in selected_charts:
        st.subheader('월별 판매량')
        month_order = filtered_df["month"].value_counts().index
        st.pyplot(plot_countplot(filtered_df, "month", order=month_order, figsize=(12, 8)))

    if "요일별 판매량" in selected_charts:
        st.subheader('요일별 판매량')
        day_order = filtered_df["day"].value_counts().index
        st.pyplot(plot_countplot(filtered_df, "day", order=day_order, figsize=(12, 8)))

    if "매장별 시간대 판매량" in selected_charts:
        st.subheader('매장별 시간대 판매량')
        st.pyplot(plot_countplot(filtered_df, "hour", hue="store_location", figsize=(12, 8)))

    if "제품 카테고리별 판매량" in selected_charts:
        st.subheader('제품 카테고리별 판매량')
        category_order = filtered_df["product_category"].value_counts().index
        st.pyplot(plot_countplot(filtered_df, "product_category", order=category_order, figsize=(12, 8)))

    if "매장별 판매 비율" in selected_charts:
        st.subheader('매장별 판매 비율')
        fig_pie = plt.figure(figsize=(12, 8))
        store_counts = df["store_location"].value_counts()
        colors = ["#e3edba", "#b8dbbb", "#71b8b4"]
        explode = [0.1 if i == 0 else 0 for i in range(len(store_counts))]

        plt.pie(store_counts, labels=store_counts.index, autopct="%1.1f%%", explode=explode, startangle=90, colors=colors)
        st.pyplot(fig_pie)

    if "매장별 총 판매량" in selected_charts:
        st.subheader('매장별 총 판매량')
        sum_transaction_qty = df.groupby("store_location")["transaction_qty"].sum().reset_index()
        fig_line = plt.figure(figsize=(12, 8))
        sns.lineplot(x="store_location", y="transaction_qty", data=sum_transaction_qty, marker="o")
        st.pyplot(fig_line)

    if "월별 총 수익" in selected_charts:
        st.subheader('월별 총 수익')
        monthly_revenue = df.groupby("month")["Total revenue"].sum().reset_index().sort_values(by="Total revenue", ascending=True)
        fig_monthly_revenue = plt.figure(figsize=(12, 8))
        sns.lineplot(x="month", y="Total revenue", data=monthly_revenue, marker="o")
        st.pyplot(fig_monthly_revenue)

if __name__ == '__main__':
    main()
