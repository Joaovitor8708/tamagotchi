from biblioteca import *
pet = Tamagotchi(nome='João')

while True:
    acao = input('Digite a ação que deseja executar (comer, parar de comer, dormir, falar, parar de falar, acordar, checar estado): ').lower()
    if acao == 'comer':
        pet.comer()
    elif acao == 'parar de comer':
        pet.parar_de_comer()
    elif acao == 'dormir':
        pet.dormir()
    elif acao == 'falar':
        pet.falar()
    elif acao == 'parar de falar':
        pet.parar_de_falar()
    elif acao == 'acordar':
        pet.acordar()
    elif acao == 'checar estado':
        pet.checar_estado()
    else:
        print('Ação inválida')