# 아이그루스 회비 입금 확인 자동화 디스코드 봇
개발자 : <a href="https://github.com/Yun-YeoJun">윤여준</a>, <a href="https://github.com/Jimin0430">최지민</a><br>
개발 기간 : 2022-08-03 ~ 2022-08-04

## 개요
아이그루스 회비 입금자를 확인하고 디스코드 서버에서 정회원 역할을 부여해주는 디스코드 봇입니다.

정회원 역할이 부여되기 전까진 준회원 상태이며 공지 채널 외에 다른 채널에 들어갈 수 없습니다.



## 사용 효과
아이그루스는 2022년 1학기 기준 400명 이상의 대형 동아리입니다. 그래서 회비 입금 확인 후 정회원 톡방 초대 업무가 기존엔 총무, 부총무 2명이 하루에 30분씩 투자해서 총 20일이 필요한 업무였습니다. 이 프로그램을 사용하면 단 몇 초만에 업무를 끝낼 수 있게 되어 효율이 매우 높아졌습니다.


## 사용 방법 (카카오뱅크 기준)
1. 아이그루스 통장 거래내역 엑셀 파일을 다운로드 후 "deposit.xlsx"라는 이름으로 프로젝트 폴더에 저장합니다.

![image](https://user-images.githubusercontent.com/30434779/182913865-0c625b01-b23f-435e-a853-422856b65b89.png)
<br>
<br>
<br>

2. 입금 내역 확인 구글폼 결과 엑셀 파일을 "final.xlsx"라는 이름으로 프로젝트 폴더에 저장합니다.

![image](https://user-images.githubusercontent.com/30434779/182921780-42aa381a-cc9b-4006-a378-2e10c806a7d5.png)

<br>
<br>
<br>

3. 기존 회원 모집폼 결과 엑셀 파일을 "existing_member.xlsx"라는 이름으로 프로젝트 폴더에 저장합니다. 
(기존 회원 중 군휴학생의 경우 회비를 안 내기 때문에 입금 내역 관련 엑셀 파일이 아닌 기존 회원 모집 폼 엑셀 파일에서 명단 추출)
 
![image](https://user-images.githubusercontent.com/30434779/183120752-6906b3ff-d985-498d-8dcb-54e8f660cce0.png)

<br>
<br>
<br>

3. 아이그루스 디스코드 서버로 회비 입금 확인 자동화 봇을 초대합니다.

<br>
<br>
<br>

4. serverId.txt 파일과 token.txt 파일을 만들어 각각 아이그루스 디스코드 서버 ID와 회비 입금 확인 자동화 봇 Token 값을 입력하고 프로젝트 폴더에 저장합니다. (보안 때문에 token.txt 파일은 .gitignore 파일에 꼭 추가해서 깃허브에 업로드 되지 않도록 해야 합니다.)

![image](https://user-images.githubusercontent.com/30434779/182916191-94d47468-0237-4b68-9d11-0a347fd1a157.png)
![image](https://user-images.githubusercontent.com/30434779/182916557-9d1a5d2d-5230-49ad-b49e-5faa0ec3264f.png)

<br>
<br>
<br>

5. automization.py 파일을 실행시키고 다음과 같이 봇의 이름과 봇이 접속한 서버 ID가 제대로 뜨는지 확인합니다.

![image](https://user-images.githubusercontent.com/30434779/182918042-b584dda0-5d54-4c19-b728-026e3379f93a.png)

<br>
<br>
<br>

6. 채팅창에 "!정회원"이라고 명령어를 입력합니다.

![image](https://user-images.githubusercontent.com/30434779/182916848-1c117d94-e494-4efd-8ed8-77e3f5496ca5.png)

<br>
<br>
<br>

7. 봇이 pandas 라이브러리를 사용해 거래내역 엑셀 파일(deposit.xlsx)의 C,D,G열의 11번째 행부터 마지막 행까지 긁어옵니다.

![image](https://user-images.githubusercontent.com/30434779/182914947-bcb85090-312f-4bfb-82e2-0718c30e5b01.png)

<br>
<br>
<br>

8. 입금액이 2만원인지 확인하고 해당하는 사람들의 목록이 출력됩니다.

![image](https://user-images.githubusercontent.com/30434779/182918893-1c08f495-e8e0-4291-ad93-bbe1ceb24faa.png)

<br>
<br>
<br>

9. 봇이 pandas 라이브러리를 사용해 입금 내역 확인 구글폼 결과 엑셀 파일(final.xlsx)의 D,I열의 값을 전부 긁어옵니다.

![image](https://user-images.githubusercontent.com/30434779/182921195-58a2e10a-0545-4666-836f-43599f8cf14e.png)

<br>
<br>
<br>

10. 입금 내역 확인 구글폼 작성자 목록이 출력됩니다.

![image](https://user-images.githubusercontent.com/30434779/182922214-0d0cffe6-b66c-46aa-bcd0-42bb8d8e71d6.png)

<br>
<br>
<br>

11. 봇이 pandas 라이브러리를 사용해 기존 회원 모집 구글폼 결과 엑셀 파일(existing_member.xlsx)의 B,F,H열의 값을 전부 긁어오고 F열의 값이 "휴학생(군휴학)"인 행만 추출한다.

![image](https://user-images.githubusercontent.com/30434779/183122510-8575f907-1d73-4304-a4d2-dea9a2e5ad6a.png)



<br>
<br>
<br>

12. 기존 회원 중 군휴학자 명단이 출력됩니다.

![image](https://user-images.githubusercontent.com/30434779/183123123-7c9b433f-9202-4576-8382-9cfd121d1c72.png)

<br>
<br>
<br>

11. 회비 입금 내역(7번)과 입금 내역 확인 구글폼 결과 목록(10번)에 중복되는 사람들 중 현재 정회원이 아닌 사람들 또는 기존 회원이면서 군휴학생인 사람들에게 정회원 역할이 부여되고, 다음과 같이 결과가 출력됩니다.

![image](https://user-images.githubusercontent.com/30434779/182922586-45ddfe2f-5b16-4cbd-a1d3-f03df9b9e1d5.png)

<br>
<br>
<br>

12. 마지막으로 "FINISH" 라는 단어가 출력되고 "!정회원" 명령어로 인한 봇의 행동은 끝나게 됩니다.
