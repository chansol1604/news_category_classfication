from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['Politics', ' Economic', 'Social', 'Culture', 'World', 'IT']
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

# resp = requests.get(url, headers = headers)
#
# # print(list(resp))
# # print(type(resp))
#
# soup = BeautifulSoup(resp.text, 'html.parser')
# # print(soup)
# title_tags = soup.select('.sh_text_headline')
# print(title_tags)   # [<a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/092/0002307361?sid=100">산업부 R&amp;D 예산 삭감...방문규 "국민 세금 현실적 집행 계기 될 것"</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/437/0000362461?sid=100">K반도체 한 숨 돌렸다…삼성·하이닉스 중국 공장에 장비공급 가능</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/277/0005323965?sid=100">예술의전당 찾은 한동훈에…野 "서초강남 출마 간보나"</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/277/0005323519?sid=100">오염수 2차 방류개시…日 언론 "오염수 추가 발생 방지책 없어"</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/081/0003399244?sid=100">권한도 없으면서… 보훈부, 지자체 참전수당 ‘상향 평준화 지침’ 추진 논란</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/018/0005592308?sid=100">박진 장관 “이스라엘 교민 철수·안전대책 강구”[2023 국감]</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/001/0014250745?sid=100"> 하마스 북한제 로켓발사기 사용 정황 포착[이·팔 전쟁]</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/001/0014252023?sid=100">권성동 "文정부 추진 민주인권기념관 백지화해야…편향적 역사"</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/025/0003313221?sid=100">"서부발전, 새만금 태양광 수익 스스로 포기"...박수영 의원 "군산판 대장동"</a>, <a class="sh_text_headline nclicks(cls_pol.clsart)" href="https://n.news.naver.com/mnews/article/001/0014252018?sid=100">이스라엘 단기체류 국민 218명 항공편·육로 이용 빠져나와</a>]
# print(len(title_tags))
# print(type(title_tags[0]))
# titles = []
# for title_tag in title_tags:
#     titles.append(re.compile('[^가-힣|a-z|A-Z]').sub(' ', title_tag.text))    # 제목만 가져오기
# print(titles)   # ['산업부 R D 예산 삭감   방문규  국민 세금 현실적 집행 계기 될 것 ', 'K반도체 한 숨 돌렸다 삼성 하이닉스 중국 공장에 장비공급 가능', '예술의전당 찾은 한동훈에    서초강남 출마 간보나 ', '오염수  차 방류개시   언론  오염수 추가 발생 방지책 없어 ', '권한도 없으면서  보훈부  지자체 참전수당  상향 평준화 지침  추진 논란', '박진 장관  이스라엘 교민 철수 안전대책 강구       국감 ', ' 하마스 북한제 로켓발사기 사용 정황 포착 이 팔 전쟁 ', '권성동   정부 추진 민주인권기념관 백지화해야 편향적 역사 ', ' 서부발전  새만금 태양광 수익 스스로 포기    박수영 의원  군산판 대장동 ', '이스라엘 단기체류 국민    명 항공편 육로 이용 빠져나와']
# print(len(titles))

df_title = pd.DataFrame()
re_title = re.compile('[^가-힣|a-z|A-Z]')

for i in range(6):
    resp = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i), headers=headers)
