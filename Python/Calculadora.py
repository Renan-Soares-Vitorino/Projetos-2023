class calculadora:
    mais = lambda x, y: x + y
    menos = lambda x,y: x - y
    dividir = lambda x,y: x / y
    vezes = lambda x,y: x * y

num0 = int(input("Digite um número: "))
num1 = int(input("Digite outro número: "))
operacao = input("Digite uma operação: ")

try:
    print(getattr(calculadora, operacao)(num0, num1))
except:
    pass