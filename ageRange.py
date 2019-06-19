#年龄测试程序

import sys

age = int(sys.argv[1])
if 0 <= age <10:
    print('you belong to kids')
elif 10 <= age < 18:
    print('you belong to teenager')
elif 18 <= age <30:
    print('you belong to adult')
elif 30 <= age <60:
    print('you belong to older')
else:
    print('you belong to oldest')

