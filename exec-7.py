 7. Pinheiro  - Implemente um programa que desenhe um "pinheiro" na tela, similar ao abaixo.
#        X
#       XXX
#      XXXXX
#     XXXXXXX
#    XXXXXXXXX
#   XXXXXXXXXXX
#  XXXXXXXXXXXXX
# XXXXXXXXXXXXXXX
#        XX
#        XX
#       XXXX

altura = 8

for i in range(altura):
    espacos = ' ' * (altura - i - 1)
    folhas = 'X' * (2 * i + 1)
    print(espacos + folhas)

tronco_altura = 2
tronco_largura = 2

for j in range(tronco_altura):
    espacos = ' ' * (altura - 1)
    tronco = 'X' * tronco_largura
    print(espacos + tronco)
    
espacos = ' ' * (altura - 2)
tronco = 'X' * (tronco_largura * 2)
print(espacos + tronco)