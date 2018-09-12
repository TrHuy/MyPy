from idlelib.idle_test.test_browser import f1

import os
os.getcwd()
f1 = open('hello.txt', 'w')
f1.write('hello guy!')
f1.close()

f2 = open('hello.txt', 'r')
data = f2.read()
print(data)
position = f2.tell()
print("con tro file hien tai", position)
position = f2.seek(0, 0)
print("con tro file hien tai", position)
#os.remove('helloGuy.txt')
