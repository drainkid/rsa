import math
import random
from random import randint
import decimal

character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '\n', '.', ';']

def calculate_d(m):
    d = m-1
    for i in range(2,m,1):
        if (m%i ==0) and (d%i == 0):
            d-=1
            i=1

    return d

def calculate_e(d,m):
    e =10
    while(True):
        if ((e*d)% m == 1):
            break
        else:
            e+=1
    return e


def isPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def get_primes(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b

def rsa_encode(s,e,n):
    result= list()

    for i in range(0 , len(s),1):
        indexx = character.index(s[i])
        bi = indexx
        bi = pow(bi,e)
        bi = bi % n
        result.append(bi)

    return (result)

def encrypt():
   ch =  int(input("0 - Рандомная генерация, 1- Сами вводим"))

   if ch == 0:
    q = random.choice(get_primes(100))
    p = random.choice(get_primes(100))

   elif ch == 1:
       q = int(input("q= "))
       p = int(input("p= "))


   if  isPrime(q) and isPrime(p):
           with open("text.txt") as file:
            s = file.read()

            n = p * q
            m = (p - 1) * (q - 1)
            d = calculate_d(m)
            e = calculate_e(d, m)

            result = rsa_encode(s, e, n)
            f1 = open('out.txt', 'w')
            for elem in result:
                f1.write(str(elem) + "\n" )
            print('d=', d)
            print('n=', n)
   else:
       print("Числа непростые!")

def rsa_decode(input, d, n):
    result = list()
    decimal.getcontext().prec = 100
    try:
        for item in input:
            bi = int(item)
            bi = pow(bi,d)
            bi = bi % n
            ind = int(bi)
            result += str(character[ind])
    except: IndexError
    print('неверный пароль')
    return result

def decrypt():
    inputt= []
    f = open('out.txt')
    d = int(input("d= "))
    n = int(input("n= "))

    for elem in f:
        inputt.append(elem)
    f.close()
    result = rsa_decode(inputt,d,n)
    f2 = open('out2.txt', 'w')
    for elem in result:
        f2.write(str(elem))



def main():
    encrypt()
    q = int(input("Хотим расшифровать данные? Введите 0 если хотим"))
    if q == 0:
        decrypt()
        q == randint(1,10)
    else:
        print('.')


main()
