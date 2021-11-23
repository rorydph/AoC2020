cnt = 0
with open("2-input.txt") as f:
    lst = [x.strip() for x in f.readlines()]
for pwd in lst:
    pwd = pwd.split()
    char_cnt = pwd[2].count(pwd[1].replace(':', ''))
    chk_range = pwd[0].split('-')
    if int(char_cnt) in range(int(chk_range[0]), int(chk_range[1]) + 1):
        cnt += 1
print(cnt)
