
# 방법들

---

과정소개

기획 : 홈카페가 취미인 저는 커피관련 데이터를 수집하여 분석및 시각화를 해보자고 생각했다.

과정 :  1. 화면 기획 ui/ux가 중요하다고 판단하여 스트림릿 앱 화면 기획(카페느낌 화면으로 기획)

        2. 데이터 수집 kaggle에 좋은 데이터들을 수집하였다

        3. 데이터가공 많은양의 데이터들 다시 분류하고 날짜중복된것들을 처리

        4. 데이터가공된것들을 모아 멀티셀렉트를 사용하여 여러 차트들을 볼수있게 만들었다

        5. 다 만들고 정상작동하는것을 확인하여 여러요소들을 추가(데이터 출처,컬럼 설명,이미지 추가)

        6. 여러요소들을 추가하니 에러 발생하여 에러를 해결하기 위해 검색 및 gpt도움
        
        7. 완성

데이터 수집 출처 : https://www.kaggle.com/code/ahmedabbas757/coffee-shop-sales/notebook

---

# 오류및 해결방안

---

오류 : title을 한글로 할려했는데 글자가 꺠짐 발생

해결 방법 : 처음에 차트안에 title을 한글로 하고싶었지만 깨짐이 발생했고 
           서브헤더를 사용했더니 글자꺠짐이 없었다

오류2 : 스트림릿 화면을 꾸미기 위해 스트림릿 테마를 사용할려했지만 충돌때문에
        사용할수 없었다.

해결 방법 : 여러 방법을 찾던중 CSS로 설정을 직접바꿔주면 변경되는것을   알아내고
            키보드에 F12를 눌러서 직접 변경한곳을 CSS로 설중해주었다.

오류3 : 스트림릿 구현중 데이터양이 많아서 로딩이 오래 걸렸다.

해결 방법 : 검색결과 데이터 캐싱이라는것을 찾았다고
           데이터 캐싱하여 시간이 좀 더 단축되었다.

오류4 : 이미지 추가 

해결 방법 : 로컬 이미지는 저장 폴더가 이상했는지? 이미지를 불러올수 없었다 그래서 
           url이미지로 해결했다.
---

# 도움이 되었던 사이트들

스트림릿 CSS 적용법 : https://blog.firstpenguine.school/105

스트림릿 widget 참고글 : https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/#google_vignette

스트림릿 chart 참고글 : https://luvris2.tistory.com/103#google_vignette

# 데이터 수집 참고했던 사이트

---

https://www.kaggle.com/

https://www.kaggle.com/datasets/sripaadsrinivasan/yelp-coffee-reviews


---



