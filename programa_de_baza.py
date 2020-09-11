n = 6
a = range(n + 1)


# max_range = ultimul numar din sir, valoarea maxima a sirului, k = numarul de putere la care va fi ridicat sirul
# total,total1 sunt variabele ce vor tine in ele suma, scrise in functie pentru a le defini valoarea de 0


def algebra(max_range, k, total,total1):
    row = []  #definim lista
    for num in max_range:
        row.append(num) #adaugam valorile din range() in lista
    for pare in row: #pentru fiecare numar din lista
        if row[-1] > 20: #daca ...
            print("sirul este mai mare decat  20")
        elif pare % 2 == 0:  #altfel
            ec1 = pare ** k
            total = ec1 + total
            print("suma la moment = ", total)
    print("suma numerelor pare in lista la puterea", k," = ", total)

    for impare in row:  #pentru fiecare numar din lista
        if impare % 2 == 1: #daca...
            ec2 = impare ** k
            total1 = ec2 + total1
            print("suma la moment = ", total1)
    print("suma numerelor impare in lista la puterea", k," = ", total1)

algebra(a, 2, 0, 0)
