from ursina import *

app = Ursina()

potatos = 0
industry1_buyed = False
industry2_buyed = False
background = Entity(model='quad', texture='Background.png', scale=(20,10))
counter = Text(text='0', y=0.25, scale=2, origin=(0, -1), background=True)
button = Button(texture='Potato.png', scale=0.3, color=color.white)
industry1 = Button(cost=10, x=0.7, y=-0.06, scale=0.2, texture='Indústria1.png', disabled=True)
industry2 = Button(cost=100, x=-0.65,scale=0.3, texture='Indústria2.png', disabled=True)
industry1.tooltip = Tooltip(f'<gold>Potato Factory\n<default>Earn 1 potato every second.\nCosts {industry1.cost} potatos.')
industry2.tooltip = Tooltip(f'<gold>Potato Factory\n<default>Earn 10 potato every second.\nCosts {industry2.cost} potatos.')

#GERADOR MANUAL

def button_click():
    global potatos
    potatos += 1
    button.animate_scale(0.3 * 0.9)
    button.animate_scale(0.3, delay=0.1)
    counter.text= str(potatos)
    counter.background= True

button.on_click = button_click

#INDÚSTRIA 1

def buy_industry1():
    global potatos
    global industry1_buyed
    if potatos >= industry1.cost and industry1_buyed == False:
        potatos -= industry1.cost
        industry1_buyed = True
        counter.text = str(potatos)
        invoke(generate_gold_industry1, 1, 1)

industry1.on_click = buy_industry1

def generate_gold_industry1(value=1, interval=1):
    global potatos
    potatos += 1
    industry1.animate_scale(0.2 * 1.1)
    industry1.animate_scale(0.2, delay=0.1)
    counter.text= str(potatos)
    counter.background= True
    invoke(generate_gold_industry1, value, delay=interval)

#INDÚSTRIA 2

def buy_industry2():
    global potatos
    global industry2_buyed
    if potatos >= industry2.cost and industry2_buyed == False:
        potatos -= industry2.cost
        industry2_buyed = True
        counter.text = str(potatos)
        invoke(generate_gold_industry2, 1, 1)

industry2.on_click = buy_industry2

def generate_gold_industry2(value=1, interval=1):
    global potatos
    potatos += 10
    industry2.animate_scale(0.3 * 1.1)
    industry2.animate_scale(0.3, delay=0.1)
    counter.text= str(potatos)
    counter.background= True
    invoke(generate_gold_industry2, value, delay=interval)

#ATUALIZAÇÃO

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
    

app.run()