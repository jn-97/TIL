T = int(input())

for tc in range(1, T+1):
    ymd = input()

    y = ymd[0:4]
    m = ymd[4:6]
    d = ymd[6:8]

    # m = int(m) # 개월
    d = int(d) # 일

    if m == '01' or m == '03' or m == '05' or m == '07' or m == '08' or m == '10' or m == '12':
        if d >= 1 and d <= 31:
            print('#{} '.format(tc), y,'/',m,'/',ymd[6:8], sep='')
        else:
            print('#{} '.format(tc),'-1',sep='')
    elif m == '02':
        if d >= 1 and d <= 28:
            print('#{} '.format(tc), y,'/',m,'/',ymd[6:8], sep='') 
        else:
            print('#{} '.format(tc),'-1', sep='')
    elif m == '04' or m == '06' or m == '09' or m == '11':
        if d >= 1 and d <= 30:
            print('#{} '.format(tc), y,'/',m,'/',ymd[6:8], sep='')
        else:
            print('#{} '.format(tc),'-1', sep='')
    else:
        print('#{} '.format(tc),'-1', sep='')