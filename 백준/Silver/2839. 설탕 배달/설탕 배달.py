def min_sugar_bags(N: int) -> int:
    """
    설탕 N킬로그램을 3kg, 5kg 봉지로 정확히 옮길 때
    최소 봉지 개수를 반환합니다. 불가능하면 -1을 반환.
    """
    # 1) 5kg 봉지를 최대한 많이 쓴다고 가정하고 시작
    max_five = N // 5

    # 2) 5kg 봉지 개수를 줄여가며 확인
    for five_count in range(max_five, -1, -1):
        remain = N - 5 * five_count
        # 남은 무게가 3kg 봉지로 딱 맞으면
        if remain % 3 == 0:
            three_count = remain // 3
            return five_count + three_count

    # 3) 아무 조합도 맞지 않으면 -1
    return -1


if __name__ == "__main__":
    N = int(input().strip())          # 배달해야 할 설탕 무게 입력
    print(min_sugar_bags(N))          # 정답 출력
