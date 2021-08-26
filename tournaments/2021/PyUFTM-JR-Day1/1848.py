lottery_result = 0
while True:
    try:
        crow = input().strip()
    except EOFError:
        break
    if crow == 'caw caw':
        print(lottery_result)
        lottery_result = 0
    else:
        lottery_result += int(crow.replace('-', '0').replace('*', '1'), 2)
