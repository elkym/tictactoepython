# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Board(list):

    def __init__(self):
        self.append([' ', ' ', ' '])
        self.append([' ', ' ', ' '])
        self.append([' ', ' ', ' '])

    def add_piece(self, piecetype, row, col):
        self[row][col]=piecetype
a
    def print_Board(self):
        row_number = 0
        print(" 1   2   3")
        print()
        for row in self:
          col_number = 0
          for col in row:
              print(' ' + col + ' ', end='')
              if col_number <2:
                  print('|', end='')
              col_number += 1
          print()
          if row_number < 2:
              print('--- --- ---')
          row_number += 1

Board1 = Board()

Board1.add_piece("x",0,0)
Board1.print_Board()

        
def iswon(Board):  
    for row in range(3):
        for col in range(3):
            if Board[row][col]== " ":
                continue
            else:
                letter = Board[row][col]
        
                if Board[row][0] == letter \
                and Board [row][1] == letter \
                and Board [row][2] == letter:
                #check row
                    return f"Player '{letter}' Won!"

                if Board[0][col] == letter \
                and Board[1][col] == letter \
                and Board[2][col] == letter:
                #check column
                    return f"Player '{letter}' Won!"
                
                if Board[0][0] == letter \
                and Board[1][1] == letter \
                and Board[2][2] == letter:                
                #check diagonal1
                    return f"Player '{letter}' Won!"

                if Board[0][2] == letter \
                and Board[1][1] == letter \
                and Board[2][0] == letter:                
                #check diagonal2
                    return f"Player '{letter}' Won!"
      
                
    for row in Board:
        for col in row:
            if col == ' ':
                return "Next player's turn."
    return "It's a tie."

    

print(iswon(Board1))

#board1 = Board()
#board1.print_Board()
#print()
#board1.add_piece('x', 0, 0)
#board1.print_Board()

