import json

# Token of ur bot
Token = '5756605309:AAG7t8Rluc6Vio_n3Ybk367CBeS4vJ-hrr0'

# Get random hero list
dir_hero_lists = 'hero_list/'

# log to file
def log(id, name, text):
    with open('logs/log.json', mode='w') as log_file:
        json.dump({
        'id' : id,
        'name' : name,
        'text' : text
        },
        log_file)

# log faces
def wr_faces(faces):
    with open('logs/faces.json',mode='w') as fac:
        json.dump({'faces' : faces}, fac)