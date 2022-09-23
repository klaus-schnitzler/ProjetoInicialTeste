from datetime import datetime
from time import sleep
 
def meu_decorator(funcao):
    def wrapper(valor):
        print(datetime.now().strftime("%H:%M:%S"))
        funcao(valor)
        print(datetime.now().strftime("%H:%M:%S"))
    return wrapper
 
 
@meu_decorator
def contagem(valor):
    x = 1
    while not x > valor:
        print(x)
        x += 1
        sleep(1)
 
 
 
contagem(10)