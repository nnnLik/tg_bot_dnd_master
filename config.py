import json

# Token of ur bot
Token = '5756605309:AAG7t8Rluc6Vio_n3Ybk367CBeS4vJ-hrr0'

# Get random hero list
dir_hero_lists = 'hero_list/'
logs = 'logs/log.json'
faces = 'logs/faces.json'

# log to file
def log(id, name, text):
    with open(logs, mode='w+') as log_file:
        json.dump({
        'id' : id,
        'name' : name,
        'text' : text
        },
        log_file)

# log faces
def wr_faces(fac_of_dice):
    with open(faces, mode='w') as fac:
        json.dump({'faces' : fac_of_dice}, fac)

def rd_faces():
    with open(faces, mode='r', encoding='utf-8') as fac:
        text = json.load(fac)
        return int(text['faces'])