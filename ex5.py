def torre_de_hanoi(n, origem, destino, auxiliar):
    """
    Resolve o problema da Torre de Hanoi para n discos.

    :param n: Número de discos
    :param origem: Haste de origem
    :param destino: Haste de destino
    :param auxiliar: Haste auxiliar
    """
    if n == 1:
        # Caso base: apenas um disco
        print(f"Move o disco 1 da {origem} para a {destino}")
    else:
        # Passo recursivo:
        # 1. Move n-1 discos da origem para a auxiliar usando o destino como auxiliar
        torre_de_hanoi(n - 1, origem, auxiliar, destino)
        
        # 2. Move o disco n da origem para o destino
        print(f"Move o disco {n} da {origem} para a {destino}")
        
        # 3. Move n-1 discos da auxiliar para o destino usando a origem como auxiliar
        torre_de_hanoi(n - 1, auxiliar, destino, origem)
def main():

    n = int(input("Digite o número de discos: "))
# Exemplo de uso:
    torre_de_hanoi(n, 'A', 'C', 'B')
main()
