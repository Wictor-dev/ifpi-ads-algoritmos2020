def do_twice(f):
    f()
    f()
def do_four(a):
    do_twice(a)
    do_twice(a)

def horizontal_1():
    print("+ - - - -",end=" ")
def barra_1():
    print("|        ", end=" ")
def horizontal_2():
    do_twice(horizontal_1)
    print ("+")
def barra_2():
    do_twice(barra_1)
    barra_1()
    print(" ")
def cima():
    horizontal_2()
    do_four(barra_2)
def baixo():
    do_twice(cima)
    horizontal_2()

baixo()

#1
def horizontal_1():
    print("+ - - - -",end=" ")
def barra_1():
    print("|        ", end=" ")
def horizontal_2():
    do_four(horizontal_1)
    print ("+")
def barra_2():
    do_four(barra_1)
    barra_1()
    print(" ")
def cima():
    horizontal_2()
    do_four(barra_2)
def baixo():
    do_four(cima)
    horizontal_2()

baixo()