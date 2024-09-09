#!/usr/bin/env python
# coding: utf-8

# In[57]:


#criando uma função para cada operação

def adicao (x, y):
    return x + y 

def subtracao (x, y):
    return x - y

def multiplicacao (x, y):
    return x * y

def divisao (x, y):
    return x / y

print("Escolha uma opção de cálculo (digite somente o número da opção): ")
print("1 - adição")
print("2 - subtração")
print("3 - multiplicacao")
print("4 - divisao\n")

opcao=input().strip()

x=float(input("\nInforme o primeiro número: "))
y=float(input("Informe o segundo número: "))

def escolher_opcao(opcao, x, y):
    if opcao == '1':
        return adicao(x, y)
    elif opcao == '2':
        return subtracao(x, y)
    elif opcao == '3':
        return multiplicacao(x, y)
    elif opcao == '4':
        return divisao(x, y)
    else:
        return "Opção inválida"

resultado = escolher_opcao(opcao, x, y)
print(f"O resultado é: {resultado}")


# In[ ]:




