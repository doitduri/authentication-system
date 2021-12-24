### assignment

- [x] 인증서버 API 구현

- [x] RDBMS 사용 (Mysql)

- [x] Password Encryption
- [ ] Front-end
- [ ] E-mail 인증
- [ ] 비밀번호 찾기
- [ ] 캐시



### 시스템 아키텍처 

![image](https://user-images.githubusercontent.com/26545623/146738522-7cc7fd60-899a-4856-a2a9-388cc38b786b.png)



### Moblie

![image](https://user-images.githubusercontent.com/26545623/147306801-a5d54c59-7bfb-4691-acea-f925f8bc6bbc.png)

각 도메인(또는 기능) 단위로 아래 파일이 생성된다.

- View : present 부분
- ViewModel : 화면의 데이터를 서비스로직에 맞게 처리하는 부분 // RxSwift, input(이벤트)+output(서비스로직의 결과)
- Coordinator : 화면 전환 // RxFlow로 도입 고민 중
- Service : 네트워크 통신 등을 통해 서버 모델을 가지고 로직에서 사용하는 모델로 바꾸는 부분
- Model : entity 
- Network : header, HTTP method 등 정의



