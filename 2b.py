cnt = 0
with open("2-input.txt") as f:
    lst = [x.strip() for x in f.readlines()]
for pwd in lst:
    pwd = pwd.split()
    char = pwd[1].replace(':', '')
    char_chk = pwd[0].split('-')
    if bool(pwd[2][int(char_chk[0]) - 1] == char) != bool(pwd[2][int(char_chk[1]) - 1] == char):
        cnt += 1
print(cnt)
