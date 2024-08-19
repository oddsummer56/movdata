# movdata
### Project
영화목록 API을 통해 연도별 영화목록 추출.  
이미 다운 받은 영화목록 data 는 skip 하도록 코드 추가.

### Process
1. 영화진흥위원회 영화목록 API 연도별로 호출
2. 연도별 tot cnt 계산하여 total_page 계산
3. 'movieListResult' 딕셔너리 내부의 'movieList'라는 키에 해당하는 값에 접근
4. 연도별로 total_page 만큼 Loop 돌면서 API 호출하여 영화목록 저장 (이미 다운 받은 영화목록 data 는 skip)


