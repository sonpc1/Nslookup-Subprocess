import subprocess
from Network.detect import *
import csv
import datetime
import os

def DT_trigger():
    with open('DOMAIN.csv', mode='r') as file:
        reader = csv.reader(file)
        with open('kq.csv', mode='w', newline='') as file_kq:
            for i in reader:
                host = i[0]
                n = 0
                IP = set()
                while n <= 20:
                    nsl = subprocess.run(['nslookup', host, '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    nsl_str = nsl.stdout.decode('utf-8').replace('8.8.8.8', '').replace('\r', '').replace('\n', '').replace('\t', '').replace('A', ' ')
                    nsl_lst = nsl_str.split(' ')
                    for i in nsl_lst:
                        if Chck_IPv4(i) == True:
                            IP.add(i)
                        if Chck_IPv6(i) == True:
                            IP.add(i)
                    n = n + 1
                k = 0
                for i in IP:
                    print(i)
                    DTv4 = i + '/32 null0 tag 5555 description ' + str(datetime.datetime.now()).split(' ')[0]
                    DTv6 = i + '/128 null0 tag 5555 description ' + str(datetime.datetime.now()).split(' ')[0]
                    writer = csv.writer(file_kq)
                    if Chck_IPv4(i) == True:
                        writer.writerow([host, i, DTv4, '', ''])
                        k = k + 1
                    else:
                        writer.writerow([host, '', '', i, DTv6])
                        k = k + 1
                if k == 0:
                    writer.writerow([host + ' khong ton tai'])
                print(' da nslookup xong host %s ' % host)













