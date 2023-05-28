class calculadora:
    mais = lambda x, y: x + y
    menos = lambda x,y: x - y
    dividir = lambda x,y: x / y
    vezes = lambda x,y: x * y

def output():
    try:
        print(getattr(calculadora, operacao)(num0, num1))
    except AttributeError:
        print("Operação não encontrada")
        inputs()

num0 = float(input("Digite um número: "))
num1 = float(input("Digite outro número: "))
def inputs():
    global operacao
    operacao = input("Digite uma operação: ")
    output()

inputs()
