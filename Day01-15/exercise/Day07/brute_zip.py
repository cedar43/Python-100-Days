''' Do it for fun'''

import os
import zipfile

# 生成4位纯数字密码
if not os.path.exists('./Day01-15/exercise/Day07/password_4.txt'):
    f = open('password_4.txt', 'w')
    for i in range(0, 10000):
        pwd = str(i).zfill(4) + '\n'
        f.write(pwd)
    f.close()


# 利用zipfile进行破解
def extract_zip(file, pwd):
    try:
        file.extractall(pwd=bytes(pwd, 'utf8'))
        print('The password for this zip file is ' + pwd)
    except:
        pass


def main():
    file = zipfile.ZipFile('./Day01-15/exercise/Day07/test.zip')
    pwdlists = open('password_4.txt')
    for line in pwdlists.readlines():
        pwd = line.strip('\n')
        extract_zip(file, pwd)


if __name__ == "__main__":
    main()
