import string
import random
import pandas as pd
from icecream import ic
import numpy as np
from hello.domains import members
from context.models import Model


class Quiz30:
    '''
        데이터프레임 문제 Q02.
        ic| df:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12
    '''
    def quiz30_df_4_by_3(self) -> object:
        '''
        df = pd.DataFrame([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9],
                          [10, 11, 12]], index=range(1, 5), columns=['A', 'B', 'C'])
        ic(df)
        '''
        # 위 식을 리스트 결합 형태로 분해해서 조립하시오
        dt = {'1': range(1, 4), '2': range(4, 7), '3': range(7, 10), '4': range(10, 13)}
        df = pd.DataFrame.from_dict(dt, orient='index', columns=['A', 'B', 'C'])
        ic(df)
        return None

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:    0   1   2
                0  97  57  52
                1  56  83  80
    '''
    def quiz31_rand_2_by_3(self) -> object:
        df = pd.DataFrame(np.random.randint(10, 100, size=(2, 3)))
        ic(df)
        return None

    '''
        데이터프레임 문제 Q04.
        국어, 영어, 수학, 사회 4과목을 시험 치른 10명의 학생들의 성적표 작성.
        단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
        ic| df4:        국어  영어  수학  사회
                lDZid    57   90   55    24
                Rnvtg    12   66   43    11
                ljfJt    80   33   89    10
                ZJaje    31   28   37    34
                OnhcI    15   28   89    19
                claDN    69   41   66    74
                LYawb    65   16   13    20
                QDBCw    44   32    8    29
                PZOTP    94   78   79    96
                GOJKU    62   17   75    49
    '''
    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(5)])

    def quiz32_df_grade(self) -> object:
        data = np.random.randint(0, 100, (10, 4))
        idx = [self.id(chr_size=5) for i in range(10)]
        columns = ['국어', '영어', '수학', '사회']
        df1 = pd.DataFrame(data, index=idx, columns=columns)
        dt = {i: j for i, j in zip(idx, data)}
        df2 = pd.DataFrame.from_dict(dt, orient='index', columns=columns)
        ic(df1)
        ic(df2)
        return None

    def quiz33_df_loc(self) -> object:
        subjects = ['JAVA', 'Python', 'Java Script', 'SQL']
        students = members()
        scores = np.random.randint(0, 100, (24, 4))
        students_scores = {student: score for student, score in zip(students, scores)}
        students_scores_df = pd.DataFrame.from_dict(students_scores, orient='index', columns=subjects)
        # ic(students_scores_df)
        # students_scores_.to_csv('./save/grade.csv', sep=',', na_rep='NaN')
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        # grade.csv
        model = Model()
        # model.save_model(fname='grade.csv', dframe=students_scores_df)
        grade_df = model.new_model(fname='grade.csv')
        ic(grade_df)

        print('Q1. 파이썬의 점수만 출력하시오')
        python_scores = grade_df.loc[:, 'Python']
        ic(python_scores)
        ic(type(python_scores))

        print('Q2. 조현국의 점수만 출력하시오')
        cho_scores = grade_df.loc['조현국']
        ic(cho_scores)
        ic(type(cho_scores))

        print('Q3. 조현국의 과목별 점수를 출력하시오')
        cho_subjects_scores = grade_df.loc[['조현국']]
        ic(cho_subjects_scores)
        ic(type(cho_subjects_scores))
        return None

    @staticmethod
    def createDF(keys, vals, len):
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(len)])

    def quiz34_df_iloc(self) -> object:
        df = self.createDF(keys=['a', 'b', 'c', 'd'], vals=np.random.randint(0, 100, 4), len=3)
        ic(df)
        # ic(df.iloc[0])
        '''
        ic| df.iloc[0]: a    94
                        b     8
                        c     6
                        d    78
                        Name: 0, dtype: int32
        '''
        # ic(df.iloc[[0]])
        '''
        ic| df.iloc[[0]]:     a   b   c   d
                           0  55  12  60  16
        '''
        # ic(df.iloc[[0, 1]])
        '''
        ic| df.iloc[[0, 1]]:    a  b   c   d
                             0  6  3  46  36
                             1  6  3  46  36
        '''
        # ic(df.iloc[:3])
        '''
        ic| df.iloc[:3]:     a   b   c   d
                          0  32  53  18  15
                          1  32  53  18  15
                          2  32  53  18  15
        '''
        # ic(df.iloc[[True, False, True]])
        '''
        ic| df.iloc[[True, False, True]]:     a   b   c   d
                                           0  15  28  89  48
                                           2  15  28  89  48

        '''
        # ic(df.iloc[lambda x: x.index % 2 == 0])
        '''
        ic| df.iloc[lambda x: x.index % 2 == 0]:     a   b   c   d
                                                  0  86  11  99  37
                                                  2  86  11  99  37
        '''
        # ic(df.iloc[0, 1])
        '''
        ic| df.iloc[0, 1]: 59
        '''
        # ic(df.iloc[[0, 2], [1, 3]])
        '''
        ic| df.iloc[[0, 2], [1, 3]]:     b   d
                                      0  52  26
                                      2  52  26
        '''
        # ic(df.iloc[1:3, 0:3])
        '''
        ic| df.iloc[1:3, 0:3]:     a   b   c
                                1  32  29  99
                                2  32  29  99
        '''
        # ic(df.iloc[:, [True, False, True, False]])
        '''
        ic| df.iloc[:, [True, False, True, False]]:     a   c
                                                     0  53  17
                                                     1  53  17
                                                     2  53  17
        '''
        # ic(df.iloc[:, lambda df: [0, 2]])
        '''
        ic| df.iloc[:, lambda df: [0, 2]]:     a   c
                                            0  51  58
                                            1  51  58
                                            2  51  58
        '''
        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None




