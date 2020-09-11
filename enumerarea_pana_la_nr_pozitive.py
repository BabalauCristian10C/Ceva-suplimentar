list1 = []  # denumim 1 lista
list2 = []  # denumim 2 lista
n = 0


def fuctn_creator(b, c):  # formam functia ce va crea pentru noi liste
    for num in range(b, c):
        list1.append(num)
    return list1


fuctn_creator(-3, 6) # cu ajutorul acestei comenzi, returnam list1 = [-3......6]

for number in list1:  #aceleasi operatiuni cu diferite cicluri, daca enumerarea liste ajunge pana la un numar pozitiv, enumerarea termina
    if number > 0:
        break
    elif number <= 0:
        list2.append(number)
        print(number)
print("numerele sunt negative sau egale cu 0")


while list1[n] <= 0:   #aceleasi operatiuni cu diferite cicluri, daca enumerarea liste ajunge pana la un numar pozitiv, enumerarea termina
    print(list1[n])
    n += 1
print("numerele sunt negative sau egale cu 0")
