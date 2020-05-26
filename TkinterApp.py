from tkinter import *

root = Tk()
#Label(root, text = 'hello world').pack()
root.title('Event test')
# 창 크기 'widthXheight+창위치x+창위치y'
root.geometry('640x480+50+50')

# 버튼이 클릭되어진 후 실행되는 동작
def callback():
    exit(0)

# 버튼 생성
button = Button(root, text = 'Quit', width = 20, command = callback)
# 위젯에 버튼 생성
button.pack(padx = 10, pady = 10)

root.mainloop()
