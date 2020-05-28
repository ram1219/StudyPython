from urllib.request import urlopen
from threadsafe_tkinter import *

def get_weather(city):
    page = urlopen('https://www.weather.go.kr/weather/observation/currentweather.jsp')
    # 위 홈페이지의 글자를 모두 읽어옴
    text = page.read().decode('euckr')
    text = text[text.find(">"+city+"</a>"):]
    for i in range(5):
        text = text[text.find("<td>")+1:]
    start = 3
    end = text.find("</td>")
    tempV.set(u"온도 : " + text[start:end])
    print(text[start:end])

def refresh(*args):
    get_weather(cities.get())

root = Tk()
root.title("기상청 현재기온 : ")
root.geometry('600x480+200+200')

Label(root, text = '도시 : ').pack(side='left')
city_list = ['서울', '부산', '대구', '제주']
cities = StringVar()
cities.set(city_list[0])
cities.trace('w', refresh)

OptionMenu(root, cities, *city_list).pack(side='right')
tempV = StringVar()
tempV.set("온도 : ")
Label(root, textvariable=tempV).pack(pady=40, side='top')
Button(root, text='refresh', command=refresh).pack(pady=40, side='bottom')

root.mainloop()