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

1. Locate your image file in this exe file folder
2. Put image file name
3. use ctrl + v

