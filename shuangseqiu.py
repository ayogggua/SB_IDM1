# from random import randrange, randint, sample
#
#
# def display(balls):
# 	"""
# 	输出列表中的双色球号码
# 	"""
# 	for index, ball in enumerate(balls):
# 		if index == len(balls) - 1:
# 			print('|', end=' ')
# 		print('%02d' % ball, end=' ')
# 	print()
#
#
# def random_select():
# 	"""
# 	随机选择一组号码
# 	"""
# 	red_balls = [x for x in range(1, 34)]
# 	selected_balls = []
# 	selected_balls = sample(red_balls, 6)
# 	selected_balls.sort()
# 	selected_balls.append(randint(1, 16))
# 	return selected_balls
#
#
# def main():
# 	n = int(input('机选几注: '))
# 	for _ in range(n):
# 		display(random_select())
#
#
# if __name__ == '__main__':
# 	main()
import os
import pysnooper
@pysnooper.snoop()
@pysnooper.snoop()
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()