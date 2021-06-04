# RPA

RPA(Robotic Process Automation) : 업무자동화

- Python을 이용한 업무자동화를 위한 소스를 모아놓은 Repository 입니다.



## RPA_copytoclipboard

- 이미지파일을 읽고 클립보드에 저장하는 프로그램입니다.
- `tkinter` 인터페이스를 활용하였습니다.
  - `tkinter` : Python GUI 인터페이스
- `PyInstaller` 패키지를 이용해 exe 파일로 만들었습니다.
  - 만드는 방법은 [여기](https://tbtb7-sw.tistory.com/160)를 참고하시면 도움이 될 것입니다.

### 소스구성

- ex_tkinter.py : `tkinter` 사용을 연습하기 위한 예제 code
- copy_toclipboard.py : 경로에 있는 이미지 파일을 읽어 클립보드에 저장하는 code
- main_code.py : `tkinter` 를 활용한 copytoclipboard 프로그램 code

### 사용법

1. RPA_copytoclipboard / dist / main_code 폴더를 다운로드
2. 폴더 아래에 images 폴더 만들기
3. images 폴더에 클립보드에 저장할 이미지들 넣기
4. main_code.exe 실행
5. 이미지 파일명 입력
6. `ctrl + v` 로 원하는 곳에 붙여넣기

### UI

![RPA_copytoclipboard_UI](https://user-images.githubusercontent.com/53212228/120791047-a88fc180-c56e-11eb-9969-6da32ae080bf.JPG)



