from hello import Member
from hello.domains import my100, myRandom, members



class Quiz00:
    def quiz00calculator(self)-> float:
        a = my100()
        b = my100()
        o = ['+','-','*','/','%']
        op = myRandom(0,4)

        if(o[op] == '+'):
            res = self.add(a,b)
        elif(o[op] == '-'):
            res = self.sub(a,b)
        elif (o[op] == '*'):
            res = self.mul(a,b)
        elif (o[op] == '/'):
            res = self.div(a,b)
        elif (o[op] == '%'):
            res = self.mod(a,b)
        print(f'{a} {o[op]} {b} = {res}')

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

    def quiz02dice(self):
        print(myRandom(1, 6))

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

    def quiz04leap(self):
        year = myRandom(1,2100)
        if (year%4 == 0 and year%100 !=0) or (year%400 == 0):
            res = f'{year}년은 윤년'
        else:
            res = f'{year}년은 평년'
        print(res)

    def quiz05grade(self):
        name = members()[myRandom(0,23)]
        kor = myRandom(0,100)
        eng = myRandom(0,100)
        math = myRandom(0,100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(kor, eng, math)
        #grade = self.grade(kor,eng,math)
        passChk = self.passChk(kor,eng,math)
        print(f'이름:{name} \n'
              f'국어:{kor}점 영어:{eng}점 수학:{math}점 \n'
              f'총점:{sum}점 \n'
              f'평균:{avg}점 \n'
              #f'등급:{grade} \n'
              f'합/불:{passChk}')

    def sum(self,kor,eng,math):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    '''def grade(self,kor,eng,math):
        if (self.avg(self.kor,self.eng,self.math)) >= 90:
            return 'A등급'
        elif (self.avg(self.kor,self.eng,self.math)) >=80:
            return 'B등급'
        elif (self.avg(self.kor,self.eng,self.math)) >=70:
            return 'C등급'
        elif (self.avg(self.kor,self.eng,self.math)) >=60:
            return 'D등급'
        else:
            return 'F등급'
            '''

    def passChk(self,kor,eng,math):  # 60점이상이면 합격
        if (self.avg(kor,eng,math)) >= 60:
            return '합격'
        else:
            return '불합격'

    def quiz06memberChoice(self):
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   '권혜민', '서성민', '조현국', '김한슬', '김진영',
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   '강  민', '최건일', '유재혁', '김아름', '장원종']
        return members[myRandom(0, 23)]

    def quiz07lotto(self):
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        pass

    def quiz09gugudan(self):  # 책받침구구단
        pass