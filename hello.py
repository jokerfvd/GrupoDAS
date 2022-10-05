"""
SEILA
"""

print("Hello World\n")

def ler_arquivo(arquivo):
    with open (arquivo) as f: 
        linhas = f.readlines
    print(linhas)

ler_arquivo("hello.py")


