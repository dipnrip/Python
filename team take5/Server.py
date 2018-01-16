'''Run Server.py first , then run player1.py'''
import sys
import socket
def main_menu():
    moves = 0
    choices = []
    for x in range(0,9):
       choices.append(str(x+1))
    HOST, PORT = "Localhost", 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print( 'Connection by:', addr)
    print('You are Player 2: X')
    printBoard(choices)
    try:
        while True:
            data = conn.recv(1024).decode()
            moves = moves+1
            choices[int(data)-1] = 'O'
            printBoard(choices)
            print('Player 1:', data)
            if(checkWon(choices)==True):
                print('Player 1 has won!')
                sys.exit(0)
            elif(data == 'q' or data == ''):
                print('The other player has left.')
                break
            elif(moves == 9):
                print('The game has been tied.')
                break
            data = safe_input(choices)
            choices[int(data)-1] = 'X'
            printBoard(choices)
            conn.sendall(data.encode('utf-8'))
            moves = moves+1
            if(checkWon(choices)==True):
                print('Player 2 has won!')
                break
            elif(moves == 9):
                print('The game has been tied.')
                break
    except ConnectionAbortedError:
        print('Player 1 has left')
    conn.close()
def safe_input(choices):
    for x in range(0,9):
        choices.append(str(x+1))
    data = ""
    while True:
        try:
            data = input('Player 2: ')
            if(data == 'q'):
                print('You have chosen to quit the program.')
                break
            elif(choices[int(data)-1] == 'X' or choices[int(data)-1] == 'O'):
                raise Exception()
            else:
                break
        except Exception():
            print('Invalid choice! Try again.')
    if(data == 'q'):
        sys.exit(0)
    return data
def checkWon(choices):
    winner = False
    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True

        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
    return winner
def printBoard(choices) :
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')
    
if __name__ == '__main__':
    main_menu()
