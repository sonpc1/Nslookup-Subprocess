def Chck_IPv4(str):
    IPv4 = False
    coun = str.count('.')
    if coun == 3:
        str_lst = str.split('.')
        for i in str_lst:
            if i.isnumeric() and 0 <= int(i) <= 255:
                IPv4 = True
            else:
                IPv4 = False
                break
    return IPv4

def Chck_IPv6(str):
    IPv6 = False
    coun = str.count(':')
    if coun == 5:
        IPv6 = True
    return IPv6


