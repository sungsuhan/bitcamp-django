import random

class Quiz01Calculator:

    def __init__(self, num1, opcode, num2):
        self.num1 = num1
        self.opcode = opcode
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def calc(self):
        if self.opcode == '+':
            return self.add()
        elif self.opcode == '-':
            return self.sub()
        elif self.opcode == '*':
            return self.mul()
        elif self.opcode == '/':
            return self.div()

class Quiz02Bmi:

    @staticmethod
    def bmi(member):
        this = member
        bmiResult = this.weight / (this.height*this.height) * 10000
        if bmiResult >= 35:
            return f'고도 비만'
        elif bmiResult >= 30:
            return f'중(重)도 비만 (2단계 비만)'
        elif bmiResult >= 25:
            return f'경도 비만 (1단계 비만)'
        elif bmiResult >= 23:
            return f'과체중'
        elif bmiResult >= 18.5:
            return f'정상'
        else:
            return f'저체중'


class Quiz03Grade:

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return (self.kor + self.eng + self.math)

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def chkPass(self):
        if (self.avg()) >= 60:
            return f'합격'
        else:
            return f'불합격'

class Quiz04AutoGrade:

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return (self.kor + self.eng + self.math)

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def chkPass(self):
        if self.avg() >= 60:
            return f'합격'
        else:
            return f'불합격'

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05Dice(object):
    @staticmethod
    def dice():
        return myRandom(1,6)

class Quiz06(object):
    pass

class Quiz07RandomChoice(object):

    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        '강 민',  '최건일', '유재혁', '김아름', '장원종']

    def chooseMember(self):
        return self.members[myRandom(0,23)]

class Quiz08Rps(object):

    def __init__(self, player):
        self.player = player
        self.computer = myRandom(1,3)

    def game(self):
        c = self.computer
        p = self.player
        rps = ['가위', '바위', '보']
        '''if p == 1:
            if c == 1:
                res = f'플레이어:{rps[0]}, 컴퓨터:{rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어:{rps[0]}, 컴퓨터:{rps[1]}, 결과: 패배'
            elif c == 3:
                res = f'플레이어:{rps[0]}, 컴퓨터:{rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = f'플레이어:{rps[1]}, 컴퓨터:{rps[0]}, 결과: 승리'
            elif c == 2:
                res = f'플레이어:{rps[1]}, 컴퓨터:{rps[1]}, 결과: 무승부'
            elif c == 3:
                res = f'플레이어:{rps[1]}, 컴퓨터:{rps[2]}, 결과: 패배'
        elif p == 3:
            if c == 1:
                res = f'플레이어:{rps[2]}, 컴퓨터:{rps[0]}, 결과: 패배'
            elif c == 2:
                res = f'플레이어:{rps[2]}, 컴퓨터:{rps[1]}, 결과: 승리'
            elif c == 3:
                res = f'플레이어:{rps[2]}, 컴퓨터:{rps[2]}, 결과: 무승부'
        else:
            res = '1~3 입력'
        return res
        '''
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        return res

class Quiz09GetPrime(object):
    '''def __init__(self, num):
        self.num = num

    def getPrime(self):
        for i in range(2, self.num):
            if self.num % i == 0:
                return f'{self.num}은 소수가 아닙니다'
        return f'{self.num}은 소수가 맞습니다'
        '''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getPrime(self):
        res = ''
        for i in range(self.num1, self.num2 + 1):
            c = 0
            for k in range(1, i + 1):
                if i % k == 0:
                    c += 1
            if c <= 2:
                    res += f'{i} \t'
        return res
                
class Quiz10LeapYear(object):
    def __init__(self):
        pass
class Quiz11NumberGolf(object):
    def __init__(self):
        pass
class Quiz12Lotto(object):
    def __init__(self):
        pass
class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass


