import chess


board = chess.Board()

board.push_san('e4')
print(f'{board}\n')
board.push_san('e5')
print(f'{board}\n')
board.push_san('Bc4')
print(f'{board}\n')
board.push_san('Nc6')
print(f'{board}\n')
board.push_san('Qh5')
print(f'{board}\n')
board.push_san('Nf6')
print(f'{board}\n')
board.push_san('Qxf7')
print(f'{board}\n')

