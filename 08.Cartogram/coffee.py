import numpy as np
import pandas as pd
import warnings
# warnings.filterwarnings('ignore')

def get_ID(df):
    metro_list = ['서울특별시','부산광역시','대구광역시','인천광역시','대전광역시','광주광역시','울산광역시']
    si_name = [None] * len(df)
    
    for i in df.index:
        if df.시도명[i] in metro_list:
            if len(df.시군구명[i]) == 2:
                si_name[i] = df.시도명[i][:2] + ' ' + df.시군구명[i]
            else:
                si_name[i] = df.시도명[i][:2] + ' ' + df.시군구명[i][:-1]       #긴 구이름 에서 맨 뒤의 "구" 제외
        else:
            # metro_list에 없는 지역의 처리
            si_len = len(df.시군구명[i].split())
            if si_len == 1:
                if df.시군구명[i][:-1] == '고성':
                    if df.시도명[i] == '강원도':
                        si_name[i] = '고성(강원)'
                    else:
                        si_name[i] = '고성(경남)'
                elif df.시군구명[i][:2] == '세종':
                    si_name[i] = '세종'
                else:
                    print(df.시군구명[i][:-1], str(i))
                    si_name[i] = df.시군구명[i][:-1]
            else:
                # 시군구 si_len != 1
                tmp_gu_dict, admingu = df.시군구명[i].split()
                for key, values in admingu.items():
                    if admingu in values:
                        if len(admingu) == 2:
                            si_name[i] = key + ' ' + admingu
                        elif admingu in ['마산합포구', '마산회원구']:
                            si_name[i] = key + ' ' + admingu[2:-1]
                        else:
                            si_name[i] = key + ' ' + admingu[:-1]

    return si_name

starbucks = pd.DataFrame(columns=['상호명','지점명','시도명','시군구명','도로명주소'])
coffeebean = pd.DataFrame(columns=['상호명','지점명','시도명','시군구명','도로명주소'])
ediya = pd.DataFrame(columns=['상호명','지점명','시도명','시군구명','도로명주소'])
paik = pd.DataFrame(columns=['상호명','지점명','시도명','시군구명','도로명주소'])

from glob import glob

for file in glob(f'data/coffee/*.csv'):
    df = pd.read_csv(file)
    df = df[df.상권업종중분류코드 == 'Q12']
    df = df[['상호명','지점명','시도명','시군구명','도로명주소']]

    sb = df[df.상호명.str.contains('스타벅스|STARBUCKS', case=False)]
    cb = df[df.상호명.str.contains('커피빈|COFFEEBEAN', case=False)]
    ed = df[df.상호명.str.contains('이디야|EDIYA', case=False)]
    bd = df[df.상호명.str.contains('빽다방|PAIKSCOFFEE', case=False)]

    starbucks = pd.concat([starbucks, sb])
    coffeebean = pd.concat([coffeebean, cb])
    ediya = pd.concat([ediya, ed])
    paik = pd.concat([paik, bd])

starbucks.to_csv('data/result/스타벅스.csv', index=False, encoding="utf-8-sig")
coffeebean.to_csv('data/result/커피빈.csv', index=False, encoding="utf-8-sig")
ediya.to_csv('data/result/이디야.csv', index=False, encoding="utf-8-sig")
paik.to_csv('data/result/빽다방.csv', index=False, encoding="utf-8-sig")

#상호명,지점명,시도명,시군구명,도로명주소
# test01 = get_ID(paik)
# print(type(test01))
# test01.to_csv('test01.csv', index=False, encoding="utf-8-sig")