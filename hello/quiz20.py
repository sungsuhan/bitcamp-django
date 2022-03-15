import random
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from hello.quiz00 import Quiz00
from hello.domains import myRandom, members


class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][1])

        list3 = [1, '2', [1, 2, 3]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)

        print(2 * list4)

        list4.append(list5)
        print(list4)

        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)

        print(c[0][1])

        c[0][1] = 10
        print(c)

        a = range(10)
        print(a)

        print(sum(a))

        b = [2, 10, 0, -2]
        print(sorted(b))

        b.index(0)
        len(b)
        print(b.index(0), len(b))

        return None

    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))

        a = (1, 2)
        b = (0, (1, 4))
        print(a + b)

        return None

    def quiz22dict(self) -> str:
        a = {"class": ['deep learning', 'machine learning'], "num_studuents": [40, 20]}

        print(a)

        print(type(a))

        print(a["class"])

        a['grade'] = ['A', 'B', 'C']
        print(a)

        print(a.keys())

        print(list(a.keys()))

        print(a.values())

        print(a.items())

        print(a.get('class'))

        print("class" in a)

        return None

    def quiz23listcom(self) -> str:
        print('------- legacy -------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('------- comprehension -------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24bugs_zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml = 속도 차이
        ls1 = self.find_bugs_music(soup, 'title')
        ls2 = self.find_bugs_music(soup, 'artist')
        dt = {i: j for i, j in zip(ls1, ls2)}
        dt1 = dict(zip(ls1, ls2))
        l = [i + j for i, j in zip(ls1, ls2)]
        l1 = list(zip(ls1, ls2))
        print(dt1)
        return dt1
        # self.dict3(ls1, ls2)
        # self.dict2(ls1, ls2) # enumeration으로 출력
        # self.dict1(ls1, ls2) # range로 출력 (속도 느림)
        # self.print_music_list(soup) # 아티스트와 타이틀을 분리해서 출력
        # self.find_rank(soup) # 랭킹 보기

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    def print_bugs_list(self, soup) -> None:
        # artists = soup.find_all('p', {'class': 'artist'})
        # artists = ([i.get_text() for i in artists])
        # print(''.join(i for i in artists))
        # songs = soup.find_all('p', {'class': 'title'})
        # songs = ([i.get_text() for i in songs])
        # print(''.join(i for i in songs))
        for i, j in enumerate(['title', 'artist']):
            print(''.join(i for i in [i for i in self.find_bugs_music(soup, j)]))
            print('*'*100)

    def find_bugs_rank(self, soup) -> None:
        for i, j in enumerate(['title', 'artist']):
            for i, j in enumerate(self.find_bugs_music(soup, j)):
                print(f'{i}위 : {j}')
            print('*'*100)

    @staticmethod
    def find_bugs_music(soup, music) -> []:
        ls = soup.find_all('p', {'class': music})
        return [i.get_text() for i in ls]

    @staticmethod
    def quiz25dictcom() -> str:
        q = Quiz00
        a = set([q.quiz06memberChoice() for i in range(5)])
        while len(a) != 5:
            a.add(q.quiz06memberChoice())
        students = list(a)
        scores = [myRandom(0, 100) for i in range(5)]
        print({i: j for i, j in zip(students, scores)})
        return None

    def quiz26map(self) -> str: return None

    def quiz27melon_zip(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.find_melon_music(soup, 'ellipsis rank01')
        ls2 = self.find_melon_artist(soup, 'checkEllipsis')
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict
        # self.print_melon_list(soup) # 아티스트와 타이틀을 분리해서 출력
        # self.find_melon_rank(soup) # 랭킹 보기

    def print_melon_list(self, soup) -> None:
        for i, j in enumerate(['ellipsis rank01', 'checkEllipsis']):
            print(''.join(i for i in [i for i in self.find_melon_music(soup, j)]))
            print('*'*100)

    def find_melon_rank(self, soup) -> None:
        for i, j in enumerate(['ellipsis rank01', 'checkEllipsis']):
            for i, j in enumerate(self.find_melon_music(soup, j)):
                print(f'{i}위 : {j}')
            print('*'*100)

    @staticmethod
    def find_melon_music(soup, music) -> []:
        ls = soup.find_all('div', {'class': music})
        return [i.get_text() for i in ls]

    @staticmethod
    def find_melon_artist(soup, artist) -> []:
        ls = soup.find_all('span', {'class': artist})
        return [i.get_text() for i in ls]

    def quiz28dataframe(self) -> None:
        dt = self.quiz24bugs_zip()
        df = pd.DataFrame.from_dict(dt, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')
        return None

    '''
        데이터프레임 문제 Q01.
        ic| df:     a   b   c
                1   1   3   5
                2   2   4   6    
    '''
    def quiz29_pandas_df(self) -> object:
        d1 = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d1, index=[1, 2])
        '''
            a  b  c
         1  1  3  5
         2  2  4  6        
         '''
        d2 = {'1': [1, 3, 5], '2': [2, 4, 6]}
        df2 = pd.DataFrame.from_dict(d2)
        '''
            1  2
         0  1  2
         1  3  4
         2  5  6
        '''
        df3 = pd.DataFrame.from_dict(d2, orient="index")
        '''
           0  1  2
        1  1  3  5
        2  2  4  6
        '''
        df4 = pd.DataFrame.from_dict(d2, orient="index", columns=['A', 'B', 'C'])
        '''
           A  B  C
        1  1  3  5
        2  2  4  6
        '''
        columns = [chr(i) for i in range(97, 100)]
        odds = []
        evens = []
        [odds.append(i) if i % 2 != 0 else evens.append(i) for i in range(1, 7)]
        d3 = ['1', '2']  # TypeError: unhashable type
        d4 = [odds, evens]
        d5 = {i: j for i, j in zip(d3, d4)}
        df5 = pd.DataFrame.from_dict(d5, orient='index', columns=columns)
        print(df5)
        return None