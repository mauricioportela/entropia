Legal! Veja como fiz em Python:

"""
Entropia de Senha
-----------------
Funcao: entropia(senha)
Parametro: senha (A senha passada para o calculo.)
Retorna:

    Valor da Entropia | Categoria
    ------------------+--------------------------
     0 ate 24         | Senha Pobre
    25 ate 49         | Senha Fraca
    50 ate 74         | Senha Regular
    maior que 75      | Senha Forte
"""
import sys

def log2(n):
    v = 0
    if (n <= 0): return -1
    while (n > 1):
        n /= 2
        v += 1
    return v

def entropia(s):
    s = s.strip()
    t = len(s)
    f,a,b,n = 0,0,0,0
    for c in s:
        if c.isupper(): a += 1
        if c.islower(): b += 1
        if c.isnumeric(): n += 1
    print(f"MAIUSCULAS: {a}")
    print(f"minusculas: {b}")
    print(f"Numeros   : {n}")
    f += 26 if (a > 0) else 0
    f += 26 if (b > 0) else 0
    f += 10 if (n > 0) else 0
    return (t * log2(f * 2))

if __name__ == '__main__':
    print("PortelaINFO")
    print("OLÁ! VAMOS TESTAR A FORÇA DAS SUAS SENHAS?")
    print("-"*80)
    while True:
        r = 0
        x = input("Digite uma senha (somente ENTER=Sair): ")
        if len(x) == 0:
            sys.exit(0)
        r = entropia(x)
        if r <= 24: k = "[~~] Senha POBRE"
        elif r >= 25 and r <= 49: k = "[..] Senha FRACA"
        elif r >= 50 and r <= 74: k = "[--] Senha REGULAR"
        elif r >= 75: k = "[OK] Senha FORTE"
        else: k = "[!] error"
        print(f"VEREDITO: {k} | Entropia({r})")
