from multiprocessing import Process
import datetime
import time



def t(s):
    while(True):
        time.sleep(s)

        print(datetime.datetime.now())


def main(p):
    p.start()
    for i in range(10):
        time.sleep(0.5)
        print(p.pid)
    p.terminate()
    print("fi")



if __name__ == '__main__':
    p = Process(target=t, args=(1, ))
    main(p)
