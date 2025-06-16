# 0 ≤ N ≤ 99 정수를 입력받아 사이클 길이를 계산합니다.
N = int(input().strip())  # 입력된 수
original = N              # 원래 수 저장
current = N               # 매 사이클마다 변하는 값
count = 0                 # 사이클 횟수

while True:
    # 1) 두 자리로 분리
    ten = current // 10
    one = current % 10

    # 2) 각 자리 합 계산
    s = ten + one

    # 3) 새 숫자의 일의 자리
    new_one = s % 10

    # 4) 새로운 수 생성: 이전 수의 일의 자리 * 10 + 합의 일의 자리
    current = one * 10 + new_one

    # 5) 한 사이클 완료
    count += 1

    # 6) 원래 수로 되돌아왔으면 결과 출력 후 종료
    if current == original:
        print(count)
        break
