from tkinter import *
from PIL import ImageTk
import os

def cmd_ky():
    print("command Test")
    label1.config(text="Changed Text")

root = Tk()
root.title("KY")                        # 제목
root.geometry("600x500+0+0")            # 가로x세로+x+y
root.resizable(False, False)            # 창 크기 조절 허용 안함

pjt_dir = os.path.dirname(os.path.realpath(__file__))
print(pjt_dir) #프로젝트 소스코드 파일 경로 출력
photo = ImageTk.PhotoImage(file=pjt_dir+"\\images\\img.jpg")
label1 = Label(root, text="Test")
label2 = Label(root, image=photo)
label1.pack()
label2.pack()

# 위젯(widget) : 버튼, 체크박스 등 이벤트를 통칭한 것을 의미
btn1 = Button(root, padx=10, pady=10, text="버튼1")
btn1.pack()                             # btn1 에 설정한 속성 값을 적용시켜줌
                                        # root에 text로 들어가도록

btn2 = Button(root, fg="red", bg="white", width=10, height=10, text="버튼2")
btn2.pack()

btn4 = Button(root, text="cmd btn", command=cmd_ky)
btn4.pack()



root.mainloop()
