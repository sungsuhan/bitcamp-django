from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz04AutoGrade, Quiz05Dice, Quiz07RandomChoice, \
    Quiz08Rps, Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, Quiz14Gugudan

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기(+,-,*,/) 2.BMI 3.성적표 4.자동 성적표 5.주사위 6.미정 7.랜덤 학생 8.가위바위보 9.소수 판별기' )
        if menu == '0':
            print('종료')
            break
        elif menu == '1': #계산기
            # 객체생성
            q1 = Quiz01Calculator(int(input('첫번째 수')),input('연산자'), int(input('두번째 수')))
            print('*'*30)
            print(f'{q1.num1} {q1.opcode} {q1.num2} = {q1.calc()}')
        elif menu == '2': #BMI
            member = Member()
            q2 = Quiz02Bmi()
            member.name = input('이름 입력')
            member.height = float(input('키 입력(cm)'))
            member.weight = float(input('몸무게 입력(kg)'))
            res = q2.bmi(member)
            print('*'*30)
            print(f'{member.name}님의 BMI 결과는 {res}입니다')
        elif menu == '3': #Grade
            q3 = Quiz03Grade(input('이름 입력'), int(input('국어 점수')), int(input('영어 점수')), int(input('수학 점수')))
            print('*'*15 + '성적표' + '*'*15 + '\n' +
                f' 이름: {q3.name}\n' +
                f'> 국어: {q3.kor}점 \n' +
                f'> 영어: {q3.eng}점 \n' +
                f'> 수학: {q3.math}점\n' +
                f' 총점: {q3.total()}점 \n' +
                f' 평균: {q3.avg()}점\n' +
                f' 합격여부: {q3.chkPass()}\n' +
                '*'*35)
        elif menu == '4':
            name = input('이름 입력')
            kor = int(input('국어 점수'))
            eng = int(input('영어 점수'))
            math = int(input('수학 점수'))
            q4 = Quiz04AutoGrade(name, kor, eng, math)
            print('*' * 15 + '성적표' + '*' * 15 + '\n' +
                  f' 이름: {q4.name}\n' +
                  f'> 국어: {q4.kor}점 \n' +
                  f'> 영어: {q4.eng}점 \n' +
                  f'> 수학: {q4.math}점\n' +
                  f' 총점: {q4.total()}점 \n' +
                  f' 평균: {q4.avg()}점\n' +
                  f' 합격여부: {q4.chkPass()}\n' +
                  '*' * 35)
        elif menu == '5':
            print(Quiz05Dice.dice())
        elif menu == '6':
            q6 = None
        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())
        elif menu == '8':
            q8 = Quiz08Rps(int(input('1:가위 2:바위 3:보')))
            print('*'*30)
            print(q8.game())
        elif menu == '9':
            q9 = Quiz09GetPrime(int(input('숫자 입력')))
            print('*'*30)
            print(q9.getPrime())
        elif menu == '10':
            q10 = Quiz10LeapYear()
        elif menu == '11':
            q11 = Quiz11NumberGolf()
        elif menu == '12':
            q12 = Quiz12Lotto()
        elif menu == '13':
            q13 = Quiz13Bank()
        elif menu == '14':
            q14 = Quiz14Gugudan()
        else:
            print('0~14 입력')
