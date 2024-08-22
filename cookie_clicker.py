#IMPORTANDO BIBLIOTECA URSINA
from ursina import *

#INICIALIZA O AMBIENTE GRAFICO
app = Ursina()

#O NUMERO DE BATATAS COMEÇA EM 0
potatos = 0
#STATUS DE POSSE DAS FABRICAS
industry1_buyed = False
industry2_buyed = False
#DEFINE/COMFIGURA O FUNDO DO APLICATIVO
background = Entity(model='quad', texture='Background.png', scale=(20,10))
#DEFINE O CONTADOR DE BATATAS
counter = Text(text='0', y=0.25, scale=2, origin=(0, -1), background=True)
#CONFIGURA A BATATA (IMG) COMO UM BOTÃO
button = Button(texture='Potato.png', scale=0.3, color=color.white)
#CONFIGURA AS FABRICAS (IMG) COMO UM BOTÃO
industry1 = Button(cost=10, x=0.7, y=-0.06, scale=0.2, texture='Indústria1.png', disabled=True)
industry2 = Button(cost=100, x=-0.65,scale=0.3, texture='Indústria2.png', disabled=True)
#CONFIGURA A DESCRIÇÃO DAS FABRICAS
industry1.tooltip = Tooltip(f'<gold>Potato Factory\n<default>Earn 1 potato every second.\nCosts {industry1.cost} potatos.')
industry2.tooltip = Tooltip(f'<gold>Potato Factory\n<default>Earn 10 potato every second.\nCosts {industry2.cost} potatos.')

#FUNÇÃO GERADOR MANUAL DE BATATAS
def button_click():
    global potatos
    potatos += 1
    button.animate_scale(0.3 * 0.9)
    button.animate_scale(0.3, delay=0.1)
    counter.text= str(potatos)
    counter.background= True

#EXECUTA A FUNÇÃO AO CLICAR COM O MOUSE NA BATATA
button.on_click = button_click

#FUNÇÃO PARA COMPRAR A INDÚSTRIA 1
def buy_industry1():
    global potatos
    global industry1_buyed
    if potatos >= industry1.cost and industry1_buyed == False:
        potatos -= industry1.cost
        industry1_buyed = True
        counter.text = str(potatos)
        invoke(generate_gold_industry1, 1, 1)

#EXECUTA A FUNÇÃO AO CLICAR COM O MOUSE NA INDUSTRIA 1 
industry1.on_click = buy_industry1

#FUNÇÃO GERADORA DE INDUSTRIA 1
def generate_gold_industry1(value=1, interval=1):
    global potatos
    potatos += 1
    industry1.animate_scale(0.2 * 1.1)
    industry1.animate_scale(0.2, delay=0.1)
    counter.text= str(potatos)
    counter.background= True
    invoke(generate_gold_industry1, value, delay=interval)

#FUNÇÃO DE COMPRA DA INDÚSTRIA 2
def buy_industry2():
    global potatos
    global industry2_buyed
    if potatos >= industry2.cost and industry2_buyed == False:
        potatos -= industry2.cost
        industry2_buyed = True
        counter.text = str(potatos)
        invoke(generate_gold_industry2, 1, 1)

#EXECUTA A FUNÇÃO AO CLICAR COM O MOUSE NA INDUSTRIA 2
industry2.on_click = buy_industry2

#FUNÇÃO GERADORA DA INDUSTRIA 2
def generate_gold_industry2(value=1, interval=1):
    global potatos
    potatos += 10
    industry2.animate_scale(0.3 * 1.1)
    industry2.animate_scale(0.3, delay=0.1)
    counter.text= str(potatos)
    counter.background= True
    invoke(generate_gold_industry2, value, delay=interval)

#FUNÇÃO DE ATUALIZAÇÃO DE DADOS
def update():
    global potatos
    global industry1
    global industry2
    for b in (industry1, ):
        if potatos >= b.cost:
            b.color = color.white
    for b in (industry2, ):
        if potatos >= b.cost:
            b.color = color.white
    
#EXECUTAR O CODIGO
app.run()