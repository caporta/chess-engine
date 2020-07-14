import chess
import random


board = chess.Board()

moveset = []
while not board.is_game_over():
    move = input('Your move: ')
    uci_move = board.push_san(move)
    moveset.append(uci_move)
    print(f'{board}\n')

    if not board.is_game_over():
        random_reply = random.choice(list(board.legal_moves))
        uci_move = board.push(random_reply)
        moveset.append(random_reply)
        print(f'{board}\n')

print(chess.Board().variation_san(moveset))
print(board.result())
import ipdb; ipdb.set_trace()

