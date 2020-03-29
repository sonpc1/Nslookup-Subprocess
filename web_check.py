import requests
import csv
import os
status = set()
with open('web.csv', mode='r') as file:
    reader = csv.reader(file)
    with open('web_check.csv', mode='w', newline='') as file_check:
        writer = csv.writer(file_check)
        count_ok = 0
        count_not = 0
        for row in reader:
            print('checking %s' % row[0])
            url = 'http://' + row[0]
            print(url)
            try:
                res = requests.get(url)
                status.add(res.status_code)
                print(status)
                a = res.content.decode('utf-8')
                if int(res.status_code) >= 400 and int(res.status_code) != 500:
                    print('access')
                    writer.writerow([row[0], 'access', res.status_code])
                    count_ok = count_ok + 1
                elif int(res.status_code) == 200 and '404 Page' not in a:
                    print('access')
                    writer.writerow([row[0], 'access', res.status_code])
                    count_ok = count_ok + 1
                else:
                    writer.writerow([row[0], 'Can not access', res.status_code])
                    print('dont')
                    count_not = count_not + 1
            except:
                print('Not OK')
                writer.writerow([row[0], 'Can not access', 'Not response in script'])
                count_not = count_not + 1

#os.system('web_check.csv')
print(count_ok, count_not)