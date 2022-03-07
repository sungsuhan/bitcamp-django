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
        res = '윤년' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else '평년'
        print(f'{year}년은 {res}')
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
        Account.main()
        '''acc = Account()
        print(acc.to_string())
        while 1:
            menu = int(input('0.종료 1.입금 2.출금'))
            if menu == 0:
                print('종료')
                break
            elif menu == 1:
                deposit = int(input('입금(원):'))
                acc.money += deposit
                print(f'{acc.name}님 잔액:{acc.money}원')
            elif menu == 2:
                withdraw = int(input('출금(원)'))
                acc.money -= withdraw
                print(f'{acc.name}님 잔액:{acc.money}원')'''
        return None

    def quiz09gugudan(self):  # 책받침구구단
        for i in range(2,10,4):
            for j in range(1,10):
                for k in range(0,3):
                    print(i+k,'X', j, '=', (i+k)*j, end='\t')
                print(i+3,'X', j, '=', (i+3)*j)
            print()
        return None

'''
은행이름은 Bitbank
입금자 이름(name)-랜덤, 계좌번호(account_number)-랜덤, 금액(money)-랜덤 속성값으로 계좌를 생성
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성 (123-12-123456)
금액은 100 ~ 999 사이 랜덤하게 입금
'''
class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = members()[myRandom(0,23)] if name == None else name
        self.account_number = self.creat_account_number() if account_number == None else account_number
        self.money = myRandom(100,999) if money == None else money

    def to_string(self):
        return f'은행:{self.BANK_NAME} ' \
               f'입금자:{self.name} ' \
               f'계좌번호:{self.account_number} ' \
               f'금액:{self.money}원'

    @staticmethod
    def creat_account_number():
        return "".join(['-' if (i==3 or i==6) else str(myRandom(0,9)) for i in range(13)])

    def del_account(self, ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌해지')
            if menu == '0':
                print('종료')
                break
            elif menu == '1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()} 계좌개설 완료')
                ls.append(acc)
            elif menu == '2':
                print("\n".join([i.to_string() for i in ls]))
            elif menu == '3':
                account_number = input('입금할 계좌번호')
                deposit = input('입금액')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        pass

            elif menu == '4':
                account_number = input('출금할 계좌번호')
                withdraw = input('출금액')

            elif menu == '5':
                account_number = input('탈퇴할 계좌번호')
            else:
                print('Wrong Number.. Try Again')
                continue







