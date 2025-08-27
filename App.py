convidados_da_festa = ["Maria",  "João", "Ana", "Carlos", "Mariana"]

status_presenca = {}

print("--- Verificação da Lista de Convidados ---")

lista_de_chegadas = ["João", "Ana", "Pedro", "Maria"]

for pessoa in lista_de_chegadas:
    if pessoa in convidados_da_festa:
        print(f"Salve, {pessoa}")
        status_presenca[pessoa] = "Confirmado"
        
    else:
        print("Desculpa ai, {pessoa}. Seu nome não esta na lista seu merda, se liga")
        status_presenca[pessoa] = "Não convidado"