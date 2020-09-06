import re
import random
from random import randrange

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    over = False
    x = 'xxx'
    o = 'ooo'

    fila0 = str(self.board[0])+str(self.board[1])+str(self.board[2])
    fila1 = str(self.board[3])+str(self.board[4])+str(self.board[5])
    fila2 = str(self.board[6])+str(self.board[7])+str(self.board[8])

    col0 = str(self.board[0])+str(self.board[3])+str(self.board[6])
    col1 = str(self.board[1])+str(self.board[4])+str(self.board[7])
    col2 = str(self.board[2])+str(self.board[5])+str(self.board[8])

    diag0 = str(self.board[0])+str(self.board[4])+str(self.board[8])
    diag1 = str(self.board[2])+str(self.board[4])+str(self.board[6])

    lista = [fila0,fila1,fila2,col0,col1,col2,diag0,diag1]

    i = 0
     
    while i < len(lista):
      if lista[i] == x:
        over = True
        i = len(lista)
      elif lista[i] == o:
        over = True
        i = len(lista)
      else:
        i+=1
    
    todasCasillasMarcadas = True
    if(self.board.count(None)):
      todasCasillasMarcadas = False

   
   
    for i in lista:
      if(i!=x or i!=o) and todasCasillasMarcadas:
        over = True
        

    return over

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    seMarco = True
    i = random.randrange(0,8)
    while seMarco:
      if self.board[i] is None:
        self.board[i] = _MACHINE_SYMBOL
        seMarco = False
      else:
        i = random.randrange(0,8)

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    i=0
    while i < len(self.board):
      palito = "|"
      cadena1 = str(self.board[i])
      cadena2 = str(self.board[i+1])
      cadena3 = str(self.board[i+2])

      if cadena1 == 'None':
        cadena1 = ' '

      if cadena2 == 'None':
        cadena2 = ' '

      if cadena3 == 'None':
        cadena3 = ' '
      
      print(cadena1+'|'+cadena2+'|'+cadena3)
      i+=3

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    self.format_board()
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    ganador = 'Gano: '
    x = 'xxx'
    o = 'ooo'

    fila0 = str(self.board[0])+str(self.board[1])+str(self.board[2])
    fila1 = str(self.board[3])+str(self.board[4])+str(self.board[5])
    fila2 = str(self.board[6])+str(self.board[7])+str(self.board[8])

    col0 = str(self.board[0])+str(self.board[3])+str(self.board[6])
    col1 = str(self.board[1])+str(self.board[4])+str(self.board[7])
    col2 = str(self.board[2])+str(self.board[5])+str(self.board[8])

    diag0 = str(self.board[0])+str(self.board[4])+str(self.board[8])
    diag1 = str(self.board[2])+str(self.board[4])+str(self.board[6])

    lista = [fila0,fila1,fila2,col0,col1,col2,diag0,diag1]

    i = 0
     
    while i < len(lista):
      if lista[i] == x:
        ganador += 'el '+_PLAYER
        i = len(lista)
      elif lista[i] == o:
        ganador += 'la '+_MACHINE
        i = len(lista)
      else:
        i+=1

    if i==len(lista) and ganador=='Gano: ':
      ganador = 'Hubo un empate'
    
    print(ganador)
