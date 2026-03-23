def triangulo(n1, n2, n3):
    if n1 == n2 and n2 == n3:
        return 1
    elif n1 >= n2 + n3 or n2 >= n1 + n3 or n3 >= n1 + n2:
        return 3
    elif n1 == n2 or n1 == n3:
        return 0
    else:
        return 2
