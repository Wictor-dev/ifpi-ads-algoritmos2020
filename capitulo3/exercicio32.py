#exercício 3.2
# questão de 1 a 5

def do_twice(f,valor):
    f(valor)
    f(valor)

def print_valor(valor):
    print(valor)



def print_twice(bruce):
    print(bruce)
    print(bruce)
#4º
# do_twice(print_twice,"wictor")

#5º   
def do_four(a,b):
    do_twice(a,b)
    do_twice(a,b)

do_four(print_valor,5)



    

