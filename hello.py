"""
SEILA
"""

print("Hello World\n")

def ler_arquivo(arquivo):
    """
    VS
    """
    with open (arquivo) as file_new: 
        linhas = file_new.readlines
    print(linhas)

ler_arquivo("hello.py")
