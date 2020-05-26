from sys import argv
import csv
import sqlite3

conn = sqlite3.connect('sample.db')
c = conn.cursor()

if len(argv) < 2:
    print("Error!!")
    exit(1)
else:
    csvfile = argv[1]
    print(csvfile)
    
    # db table 생성
    c.execute('CREATE TABLE if not exists STUDENT (id INTEGER PRIMARY KEY AUTOINCREMENT,\
        name TEXT, birth DATE, gender CHAR)')
    # csv로 저장되어있는 파일 r(read)형식으로 열기, 
    # delimeier는 csv 파일의 구분자
    student = csv.reader(open(csvfile, 'r'), delimiter = ',', quotechar = '"')  

    for row in student:
        print("%s " % (row))  
        # ?, ?, ? ---> 자동 매칭
        c.execute('INSERT INTO student(name, birth, gender) VALUES (?, ?, ?)',(row[0], row[1], row[2]))
    
    conn.commit()
    conn.close()
    exit(0)