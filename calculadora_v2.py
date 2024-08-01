def adicao(a, b):
    return a + b

resultado = adicao(5, 3)
print(resultado)



def subracao(a, b):
    return a - b

resultado = subracao(10, 4)
print(resultado)


def multiplicacao(a, b):
    return a * b

resultado = multiplicacao(4, 5)
print(resultado)



def divisao(dividendo, divisor):
    if divisor == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return dividendo / divisor

resultado1 = divisao(10, 2)
print(resultado1) 

resultado2 = divisao(10, 0)
print(resultado2)


def calculadora(num1, num2, operacao):
    if operacao in ('+', 'adição', 'soma'):
        return num1 + num2
    elif operacao in ('-', 'subtração', 'subtração'):
        return num1 - num2
    elif operacao in ('*', 'multiplicação', 'produto'):
        return num1 * num2
    elif operacao in ('/', 'divisão', 'quociente'):
        if num2 == 0:
            return "Não foi possível realizar a divisão por 0"
        return num1 / num2
    else:
        return "Operação inválida"

resultado1 = calculadora(10, 5, '+')
print(resultado1)  

resultado2 = calculadora(10, 5, 'subtração')
print(resultado2)  

resultado3 = calculadora(10, 0, '/')
print(resultado3)  

resultado4 = calculadora(10, 5, 'multiplicação')
print(resultado4) 


def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    resultado = None
    
    if operacao in ('+', 'adição', 'soma'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtração', 'subtração'):
        resultado = subtracao(num1, num2)
    elif operacao in ('*', 'multiplicação', 'produto'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisão', 'quociente'):
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    
    return resultado

resultado1 = calculadora(10, 5, '+')
print(resultado1) 

resultado2 = calculadora(10, 5, 'subtração')
print(resultado2)  

resultado3 = calculadora(10, 0, '/')
print(resultado3)  

resultado4 = calculadora(10, 5, 'multiplicação')
print(resultado4) 

resultado5 = calculadora(10, 5, 'desconhecida')
print(resultado5)  

def solicitar_saida():
    while True:
        
        saida = input("Digite 'n' para sair ou qualquer outra tecla para continuar: ").strip().lower()
        def adicao(a, b):
         return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    resultado = None
    
    if operacao in ('+', 'adição', 'soma'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtração', 'subtração'):
        resultado = subtracao(num1, num2)
    elif operacao in ('*', 'multiplicação', 'produto'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisão', 'quociente'):
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    
    return resultado

def main():
    while True:
        
        try:
            num1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            continue
        
        
        try:
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            continue
        
        
        operacao = input("Digite a operação desejada (+, -, *, /, adição, subtração, multiplicação, divisão): ").strip().lower()
        
        
        resultado = calculadora(num1, num2, operacao)
        
       
        print(f"Resultado da operação: {resultado}")
        
        
        saida = input("Digite 'n' para sair ou qualquer outra tecla para continuar: ").strip().lower()
        
        if saida == 'n':
            print("Saindo do programa.")
            break


main()