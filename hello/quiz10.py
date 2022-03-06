from hello import Member
from hello.domains import my100, myRandom, members


class Quiz10:

    def quiz10bubble(self) -> str:
        arr = [my100(),my100(),my100(),my100(),my100()]
        init = f'처음 배열: {arr}'
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f'{init}''\n'f'거품 정렬: {arr}')
        return None

    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self) -> str:
        num1 = my100()
        num2 = myRandom(num1,100)
        print(f'{num1} ~ {num2} 사이 소수 출력')
        for i in range(num1,num2+1):
            count = 0
            for j in range(2,i+1):
                if i % j == 0:
                    count += 1
            if count == 1:
                print(i)
        return None

    def quiz18golf(self) -> str: return None

    def quiz19booking(self) -> str: return None