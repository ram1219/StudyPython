from urllib import request
from bs4 import BeautifulSoup
from flask import Flask

# 웹 서버 생성
app = Flask(__name__)
@app.route("/")                         # 경로를 지정할 수 있게 한다.

# 기상청 홈페이지에서 정보를 가져오는 함수 생성
def hello():
    target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(target, "html.parser")
    output = ""
    for item in soup.select("location"):             # location 키 값을 기준으로 자른다
        output += "<h3>{}</h3>".format(item.select_one("city").string)
        output += "<p>날씨 : {}</p>".format(item.select_one("wf").string)
        output += "최저/최고기온 : {}℃ / {}℃".format(item.select_one("tmn").string, item.select_one("tmx").string)  
        output += "<hr/>"    
    return output

app.run(host='127.0.0.1', debug=False)