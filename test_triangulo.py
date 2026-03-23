from triangulo2 import triangulo

def test1():
    assert triangulo(2, 2, 4) == 3

def test2():
    assert triangulo(2, 2, 3) == 0

def test3():
    assert triangulo(4, 4, 4) == 1

def test4():
    assert triangulo(3, 2, 4) == 2

def test5():
    assert triangulo(7, 2, 3) == 3

def test6():
    assert triangulo(3, 3, 1) == 0

def test7():
    assert triangulo(10, 10, 10) == 1

def test8():
    assert triangulo(5, 8, 10) == 2
