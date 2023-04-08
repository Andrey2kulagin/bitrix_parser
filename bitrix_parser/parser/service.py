import time


def my_func():

    for i in range(1000):
        f = open("my_file.txt", 'a')
        f.write(str(i)+'\n')
        time.sleep(5)
        f.close()
