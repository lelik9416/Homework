
def dec_2_bin_or_oct(number, base):
    a1 = []
    s_ = ''
    while number > 0:
        a1.append(int(number % base))
        number = (number - number % base) / base
    str_a1 = str(a1)[1:-1][::-1].replace(',','')
    for i in str_a1.split():
        s_ += i
    return s_
 
def dec2bin(number): # возвращает str 
    return dec_2_bin_or_oct(number, 2)

def dec2oct(number): # возвращает str
    return dec_2_bin_or_oct(number, 8)

def dec2hex(number): # возвращает str
    a1 = ''
    n = [
        '0', '1', '2', '3', '4', '5', '6', '7', 
        '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
        ]
    for i in range(1, len(n)):
        while number != 0:
            a = number % 16
            number = number // 16
            a1 += n[a]
    return a1[::-1] 

def bin_or_oct_2_dec(number, q):
    a = []
    number = list(str(number))
    count = 1
    for i in number:
        a.append(int(i) * (q **(len(number) - count)))
        count += 1    
    return sum(a)

def bin2dec(number): # возвращает int
    return bin_or_oct_2_dec(number, 2)

def oct2dec(number): # возвращает int 
    return bin_or_oct_2_dec(number, 8) 

def hex2dec(number): # возвращает int
    a = []
    n = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    count = 1
    number = list(str(number.lower()))
    for i in number:
        if i in n:
            a.append(n[i] * (16 ** (len(number) - count)))
            count += 1
    return sum(a) 

#dec - десятичное 
#bin - двоичное
#oct - восьмиричное
#hex - шестнадцатиричное
