import datetime

# 한 줄 입력
x, y = map(int, input().split())

# 날짜 객체 생성
date = datetime.date(2007, x, y)

# 요일 리스트
weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# 결과 출력
print(weekdays[date.weekday()])
