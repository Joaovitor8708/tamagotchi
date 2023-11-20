class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.comendo = False
        self.dormindo = False
        self.falando = False
        self.acordando = False
        self.felicidade = 50
        self.energia = 100
        self.barriga_cheia = 50

    def comer(self):
        if self.comendo == True:
            print(f'{self.nome} já está comendo')
        elif self.falando == True:
            print(f'{self.nome} não pode falar enquanto come')
        elif self.dormindo == True:
            print('Não pode dormir enquanto come')
        else:
            self.comendo = True
            self.felicidade += 5
            self.barriga_cheia += 10
            self.energia -= 5
            if self.felicidade > 100:
                self.felicidade = 100
            if self.barriga_cheia > 100:
                self.barriga_cheia = 100
            if self.energia < 0:
                self.energia = 0
            if self.energia > 100:
                self.energia = 100
            print(
                f'{self.nome} foi comer e agora tem, {self.felicidade}'
                f' pontos de felicidade, {self.barriga_cheia} '
                f'pontos de barriga cheia. Sua energia agora é {self.energia}')

    def parar_de_comer(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo, portanto não pode parar')

    def dormir(self):
        if self.dormindo == True:
            print(f'{self.nome} não pode dormir por que já está dormindo')
        elif self.falando == True:
            print(f'{self.nome} não pode falar enquanto dorme')
        elif self.comendo == True:
            print(f'{self.nome} não pode comer enquanto dorme')
        else:
            self.dormindo = True
            self.felicidade -= 5
            self.barriga_cheia -= 10
            self.energia += 15
            if self.felicidade > 100:
                self.felicidade = 100
            if self.barriga_cheia > 100:
                self.barriga_cheia = 100
            if self.energia < 0:
                self.energia = 0
            if self.energia > 100:
                self.energia = 100
            print(
                f'{self.nome} foi dormir e agora tem, {self.felicidade}'
                f' pontos de felicidade, {self.barriga_cheia} '
                f'pontos de barriga cheia. Sua energia agora é {self.energia}')

    def acordar(self):
        if self.dormindo == True:
            print(f'{self.nome} acordou')
            self.dormindo = False
        else:
            print(f'{self.nome} já está acordado')

    def falar(self):
        if self.falando == True:
            print(f'{self.nome} não pode falar por que já está falando')
        elif self.dormir == True:
            print(f'{self.nome} não pode dormir enquanto fala')
        elif self.comendo == True:
            print(f'{self.nome} não pode comer enquanto fala')
        else:
            self.falando = True
            self.felicidade += 10
            self.barriga_cheia -= 5
            self.energia -= 5
            if self.felicidade > 100:
                self.felicidade = 100
            if self.barriga_cheia > 100:
                self.barriga_cheia = 100
            if self.energia < 0:
                self.energia = 0
            if self.energia > 100:
                self.energia = 100
            print(f'{self.nome} está falando e agora tem, {self.felicidade}'
            f' pontos de felicidade, {self.barriga_cheia} '
            f'pontos de barriga cheia. Sua energia agora é {self.energia}')

    def parar_de_falar(self):
        if self.falando == True:
            print(f'{self.nome} parou de falar')
            self.falando = False
        else:
            print(f'{self.nome} não está falando, portanto não pode parar')

    def checar_estado(self):
        print(
            f'{self.nome} tem {self.energia} pontos de energia, {self.barriga_cheia} pontos de fome e {self.felicidade} pontos de felicidade.')