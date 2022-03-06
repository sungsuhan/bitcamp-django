from hello import Member
from hello.domains import my100, myRandom, members



class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        o = ['+','-','*','/','%']
        op = o[myRandom(0,4)]

        if op == '+':
            res = self.add(a,b)
        elif op == '-':
            res = self.sub(a,b)
        elif op == '*':
            res = self.mul(a,b)
        elif op == '/':
            res = self.div(a,b)
        elif op == '%':
            res = self.mod(a,b)
        print(f'{a} {op} {b} = {res}')
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(member):
        this = Member()
        this.name = members()[myRandom(0,23)]
        this.height = myRandom(150,190)
        this.weight = myRandom(40,100)
        bmi = this.weight / (this.height * this.height) * 10000
        if bmi >= 30:
            res = '고도비만'
        elif bmi > 25:
            res = '비만'
        elif bmi > 23:
            res = '과체중'
        elif bmi > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(f'{this.name} 키:{this.height}cm 몸무게:{this.weight}kg BMI결과:{res}')
        return None

    def quiz02dice(self):
        print(myRandom(1, 6))
        return None

    def quiz03rps(self):
        c = myRandom(1,3)
        p = myRandom(1,3)
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        print(' ----------- 1 ------------')
        if p == 1:
            if c == 1:
                res = '무승부'
            elif c == 2:
                res = '패배'
            elif c == '3':
                res = '승리'
        elif p == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        elif p == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        print(f'플레이어는 {rps[p - 1]} 컴퓨터는 {rps[c - 1]} 결과는 {res}')
        print(' ----------- 2 ------------')
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        print(res)
        return None

    def quiz04leap(self):
        year = myRandom(1,2100)
        if (year%4 == 0 and year%100 !=0) or (year%400 == 0):
            res = f'{year}년은 윤년'
        else:
            res = f'{year}년은 평년'
        print(res)
        return None

    def quiz05grade(self):
        name = members()[myRandom(0,23)]
        kor = myRandom(0,100)
        eng = myRandom(0,100)
        math = myRandom(0,100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(kor, eng, math)
        grade = self.grade(kor,eng,math)
        passChk = self.passChk(kor,eng,math)
        print(f'이름:{name} \n'
              f'국어:{kor}점 영어:{eng}점 수학:{math}점 \n'
              f'총점:{sum}점 \n'
              f'평균:{avg}점 \n'
              f'등급:{grade} \n'
              f'합/불:{passChk}')
        return None

    def sum(self,kor,eng,math):
        return kor + eng + math

    def avg(self,kor,eng,math):
        return (kor + eng + math) / 3

    def grade(self,kor,eng,math):
        if (self.avg(kor,eng,math)) >= 90:
            return 'A등급'
        elif (self.avg(kor,eng,math)) >=80:
            return 'B등급'
        elif (self.avg(kor,eng,math)) >=70:
            return 'C등급'
        elif (self.avg(kor,eng,math)) >=60:
            return 'D등급'
        else:
            return 'F등급'

    def passChk(self,kor,eng,math):  # 60점이상이면 합격
        if (self.avg(kor,eng,math)) >= 60:
            return '합격'
        else:
            return '불합격'

    def quiz06memberChoice(self):
        print(members()[myRandom(0,23)])
        return None

    def quiz07lotto(self):
        for i in range(6):
            res = myRandom(1,45)
            print(res)
        return None

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        name = members()[myRandom(0,23)]
        res = 0
        while 1:
            menu = int(input('0.종료 1.입금 2.출금'))
            if menu == 0:
                print('종료')
                break
            elif menu == 1:
                deposit = int(input('입금(원):'))
                res += deposit
                print(f'{name}님 잔액:{res}원')
            elif menu == 2:
                withdraw = int(input('출금(원)'))
                res -= withdraw
                print(f'{name}님 잔액:{res}원')
        return None

    def quiz09gugudan(self):  # 책받침구구단
        for i in range(2,10,4):
            for j in range(1,10):
                for k in range(0,3):
                    print(i+k,'X', j, '=', (i+k)*j, end='\t')
                print(i+3,'X', j, '=', (i+3)*j)
            print()
        return None