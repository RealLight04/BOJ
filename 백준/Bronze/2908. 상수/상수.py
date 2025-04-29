n = list(map(str, input().split()))

# 숫자 뒤집기
a = int(n[0][::-1])
b = int(n[1][::-1])

# 큰 숫자 출력
print(max(a, b))