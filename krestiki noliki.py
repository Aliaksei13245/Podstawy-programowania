from random import randint
from time import sleep
tile = ['#','#','#','#','#','#','#','#','#',]
print(f'{tile[0]}|{tile[1]}|{tile[2]}\n'
      f'{tile[3]}|{tile[4]}|{tile[5]}\n'
      f'{tile[6]}|{tile[7]}|{tile[8]}')
while '#' in tile:
      player_do = int(input('gdzie postawisz X ?'))
      tile[player_do - 1] = 'X'
      print(f'{tile[0]}|{tile[1]}|{tile[2]}\n'
            f'{tile[3]}|{tile[4]}|{tile[5]}\n'
            f'{tile[6]}|{tile[7]}|{tile[8]}')
