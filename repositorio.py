# Simulação do banco de dados
personagens = {
    1: {
        "nome" : "Harry Potter",
        "raca" : "Humano",
        "casa" : "Grifinória",
        "altura" : 1.80,
        "nascimento" : "31/07/1980",
        "imagem" : "https://upload.wikimedia.org/wikipedia/en/d/d7/Harry_Potter_character_poster.jpg"
    },
    2: {
        "nome" : "Ron Weasley",
        "raca" : "Humano",
        "casa" : "Grifinória",
        "altura" : 1.80,
        "nascimento" : "01/03/1980",
        "imagem" : "https://upload.wikimedia.org/wikipedia/en/5/5e/Ron_Weasley_poster.jpg?20180102231238"
    },
    3: {
        "nome" : "Hermione Gringer",
        "raca" : "Humano",
        "casa" : "Grifinória",
        "altura" : 1.65,
        "nascimento" : "19/09/1979",
        "imagem" : "https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Hermione_Granger_poster.jpg/220px-Hermione_Granger_poster.jpg"
    },
    4: {
        "nome" : "Draco Malfoy",
        "raca" : "Humano",
        "casa" : "Sonserina",
        "altura" : 1.80,
        "nascimento" : "05/06/1980",
        "imagem" : "https://upload.wikimedia.org/wikipedia/en/thumb/1/16/Draco_Mal.JPG/220px-Draco_Mal.JPG"
    }
}

# Gerar ID, no bd essa função não vai existir, no nosso caso será usada na função criar personagem

def gerar_id():
    id = len(personagens) + 1
    return id

# [C]RUD
# Criar o personagem, recebe como argumento as características, escolhi não tipar

def criar_personagem(nome, raca, casa, altura, nascimento, imagem):
    personagens[gerar_id()] = {"nome":nome, "raca":raca, "casa":casa, "altura":altura, "nascimento":nascimento, "imagem":imagem}

# C[R]UD
# Função para retornar todos items no dict personagens, não recebe argumento

def retornar_personagens():
    return personagens

# C[R]UD
# Função para retornar personagem específico, recebe como argumento o id que será a chave do dict

def retornar_personagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else:
        return {}

# CR[U]D    
# Atualiza as características do personagem, recebe como argumento o id(key) e um dicionário de características para substituir as características atuais, cuidado na sintaxe do dict quando utilizar
    
def atualizar_personagem(id:int, dados_personagem:dict):
    personagens[id] = dados_personagem

#CRU[D]
# Retira do dicionário o personagem, recebe como argumento o id(key) do personagem a ser excluído

def remover_personagem(id):
    del personagens[id]
