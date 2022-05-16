hour, minute = map(int, input("").split())
runTime = int(input(""))

hap = minute + runTime

if hap >= 60:
    minuteToHour = hap//60
    minute = hap - minuteToHour*60
    hour = hour+minuteToHour
    if hour>=24:
        print(hour-24, minute)
    else:
        print(hour, minute)
else:
    print(hour, hap)