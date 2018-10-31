temperatures=str(input())
split=temperatures.split()
inInt=list(map(int,split))
day1=inInt[0]
day2=inInt[1]
day3=inInt[2]

if day2<day1 and day3>day2 or day3==day2:
    print(':)')
elif day2>day1 and day3<day2 or day3==day2:
    print(':(')
elif day2>day1 and day3>day2 and (day3-day2)<(day2-day1):
    print(':(')
elif day2>day1 and day3>day2 and (day3-day2)>=(day2-day1):
    print(':)')
elif day2<day1 and day3<day2 and (day2-day3)<(day1-day2):
    print(':)')
elif day2<day1 and day3<day2 and (day2-day3)>=(day1-day2):
    print(':(')
elif day1==day2 and day3>day2:
    print(':)')
elif day1==day2 and day3<day2:
    print(':(')