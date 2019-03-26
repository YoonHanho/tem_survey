import pandas as pd
import sqlite3
from datetime import datetime
import os
import time

intro = """
-----------------------------------------------------------------
빅데이터팀 조직관리 초간단 다섯문항 서베이!! 익명으로 저장됩니다.
(삼성전자의 조직관리 설문 문항에서 발췌)
-----------------------------------------------------------------

"""

q1 = "[1/5] 나의 업무량은 적절하다 "
q2 = "[2/5] 나의 업무 난이도는 적절하다"
q3 = "[3/5] 나는 주도적으로 업무를 계획하고 추진한다"
q4 = "[4/5] 우리 팀원들은 서로의 업무기술과 아이디어에 대해 상호 존중해준다"
q5 = "[5/5] 나는 팀에 대해 전반적으로 만족한다"
po = "직위를 입력해주세요"

def q_and_a(question):
    print(question)    
    while True:
        try:
            answer = int(input("매우그렇다 5점, 그런편이다 4점, 보통이다 3점, 아니다 2점, 매우아니다 1점 => "))
            if answer in (1,2,3,4,5):
                print('\n')
                break
            else: 
                print("이런~ 에러 떴어요! 1에서 5사이로 입력해주세요")
        except:
            print("이런~ 에러 떴어요! 1에서 5사이로 입력해주세요")
            pass
    return answer

def q_of_position(question):
    print(question)    
    while True:
        try:
            answer = int(input("매니저 1번, 선임매니저/수석매니저 2번 => "))
            if answer in (1,2):
                print('\n')
                break
            else: 
                print("이런~ 에러 떴어요! 1이나 2를 입력해주세요")
        except:
            print("이런~ 에러 떴어요! 1이나 5를 입력해주세요")
            pass
    return answer


if __name__ == "__main__":
    
    os.system('clear')   # 윈도우에서는 os.system('cls')    
    print(intro)

    a1 = q_and_a(q1)
    a2 = q_and_a(q2)
    a3 = q_and_a(q3)
    a4 = q_and_a(q4)
    a5 = q_and_a(q5)
    p1 = q_of_position(po)

    now = datetime.now()
    
    data = {'a1':[a1], 'a2':[a2], 'a3':[a3], 'a4':[a4], 'a5':[a5], 
            'po':[p1], 
            'dt':[str(now)]}
    df = pd.DataFrame(data)

    con = sqlite3.connect("survey.db")                  # 걍 생성되네
    df.to_sql('team_survey', con, if_exists='append')   # if_exists : {‘fail’, ‘replace’, ‘append’}, default ‘fail’

    os.system('clear')
    
    print("설문이 완료되었습니다. 고맙습니다.")
    print("(◕‿◕✿) (◠﹏◠✿) ôヮô ┌( ಠ‿ಠ)┘ ｖ(⌒ｏ⌒)ｖ♪ ＼(￣▽￣)/\n\n")
    #print(pd.read_sql('select * from team_survey', con))  ### 나중에 주석처리 하자
    
    time.sleep(3)
    os.system('neofetch')     # 리눅스 로고, 스펙 출력 : https://fossbytes.com/linux-distribution-logo-ascii-art-terminal/