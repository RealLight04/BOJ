A=int(input())
B=int(input())
C=int(input())

result = list(str(A*B*C))

for i in range(10):
    print(result.count(str(i)))
    # 문자열 함수 count(요소 값)를 통해 문자열 내 특정 요소의 개수를 찾을 수 있다.