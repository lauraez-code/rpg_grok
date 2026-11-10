import random


def calcular_dano(ataque, defesa, critico=False):

    dano = ataque - defesa

    if critico == True:
        dano = (2*ataque) - defesa

    return (dano)

def aplicar_dano(vida, dano):

    vida = vida - dano

    if vida < 0:
        vida = 0 

    return (vida)

def curar(vida, vida_max, cura=30):

    vida = vida + cura

    if vida > vida_max:
        vida = 100

    return (vida)

def barra_de_vida(vida, vida_max, tamanho=10):

    quant_hash = vida * tamanho // vida_max
    
    quant_traco = tamanho - quant_hash
    
    barra = "[" + (quant_hash * "#") + (quant_traco * "-") + "]"
    
    return (barra)

def classificar_resultado(vida, vida_max):

    if vida == 0:
        resultado = "Derrota"
    
    elif vida == vida_max:
        resultado = "Vitória perfeita"
    
    elif vida >= (vida_max / 2):
        resultado = "Vitória"
    
    else:
        resultado = " vitória apertada"
    
    return (resultado)
        
def ler_acao():
    while True:
        
        acao = input("\n 1 - Atacar   2 - Tomar poção   3 - Fugir\n\n>> Digite uma opção: ")
        
        if acao == "1" or acao == "2" or acao == "3":
            break
        
        else: 
            print("\n>> Ação inválida!")
    
    return (acao)
            
def batalha(heroi, inimigo, pocoes=3):
    """Executa a batalha e devolve um dicionário com o resultado:
       {"resultado": "vitoria" | "derrota" | "fuga", "turnos": ...,
        "vida_restante": ..., "pocoes": quantas poções sobraram}
    """
    turno = 0
    while heroi["vida"] > 0 and inimigo["vida"] > 0:
        turno = turno + 1
        print("\n----------------------------------")
        print(f"\n--- Turno {turno} ---")
        print(f"{heroi['nome']:<12} {barra_de_vida(heroi['vida'], heroi['vida_max'])}")
        print(f"{inimigo['nome']:<12} {barra_de_vida(inimigo['vida'], inimigo['vida_max'])}")

        acao = ler_acao()
        if acao == "1":
  
            critico = random.randint(1, 10) == 10
            dano = calcular_dano(heroi['ataque'], inimigo['defesa'], critico)
            
            critico = random.randint(1, 10) == 10
            
            if critico == 10:
                critico = True
                print(f"\n>> Dano crítico! Você causou {dano} de dano.")
            
            else:
                critico = False
                print(f"\n>>Você causou {dano} de dano.")
            
            inimigo['vida'] = aplicar_dano(inimigo['vida'], dano)
            
            
            if inimigo['vida'] > 0:
                print("\n----------------------------------")
                print(f"\n>> VEZ DE {inimigo['nome']} <<")
                dano = calcular_dano(inimigo['ataque'], heroi['defesa'])

                heroi['vida'] = aplicar_dano(heroi['vida'], dano)
                
                print(f"\n>> Goblin deu {dano} de dano em você.")
            
            else:
                print(f"\n>> Você matou {inimigo['nome']}!!")
                
                
        elif acao == "2":
            
            if pocoes > 0:
                pocoes = pocoes - 1
            
            else:
                print("\m>> Você não possui mais poções!")
            
            heroi['vida'] = curar(heroi['vida'], heroi['vida_max'])

        else:
            print("\n>> Você fugiu!")
            
            return({"resultado": "fuga", "turnos": turno, "vida_restante": heroi['vida'], "pocoes": pocoes})


    if heroi["vida"] > 0:
        resultado = "vitoria"
    else:
        resultado = "derrota"
    print("\n" + classificar_resultado(heroi["vida"], heroi["vida_max"]) + "!")
    
    return {"resultado": resultado, "turnos": turno,
            "vida_restante": heroi["vida"], "pocoes": pocoes}

if __name__ == "__main__":
    heroi = {"nome": "Gork", "vida": 100, "vida_max": 100, "ataque": 18, "defesa": 5}
    inimigo = {"nome": "Goblin", "vida": 60, "vida_max": 60, "ataque": 12, "defesa": 3}
    final = batalha(heroi, inimigo)
    print(final)
