import datetime
import time

for i in range(100):
    #print("TIME : "),
    #print(datetime.datetime.now().time())
    #print("Afte : "),
    b = datetime.datetime.now()
    time.sleep(1/1000000)
    d = datetime.datetime.now() - b
    #print(datetime.datetime.now().time())
    print(d)
