table = 2
while table <= 12:
    num = 1
    print("[", table, "]")
    while num <= 12:
        print(table, " * ", num, " : ", table * num)
        num += 1
    print("-------------")
    table += 1
