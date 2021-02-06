table = 2
while table <= 12:
    num = 1
    print("[", table, "]")
    while num <= 12:
        print(table, " * ", num, " : ", table * num)  # พิมพ์สูตรคูณ
        num += 1
    print("-------------")
    table += 1
