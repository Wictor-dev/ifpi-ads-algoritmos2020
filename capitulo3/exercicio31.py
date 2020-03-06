def right_justify(s):
    tamanho =  len(s)
    tamanho_funct = 70 - tamanho
    print (" " * tamanho_funct + s)

right_justify("monty")
