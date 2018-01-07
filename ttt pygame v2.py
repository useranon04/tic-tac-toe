#tictactoe pygame v1

import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Tic Tac Toe by Francois Ni")

pygame.font.init()

start = pygame.font.SysFont("Garamond MS",115,True)
win_message = pygame.font.SysFont("Garamond MS",100,True)
play_again = pygame.font.SysFont("Garamond MS",50,False,True)
message_start1 = start.render("Tic",True,(0,0,255))
message_start2 = start.render("Tac",True,(0,0,255))
message_start3 = start.render("Toe",True,(0,0,255))
begin = play_again.render("Click to play",True,(255,0,0))
messageX = win_message.render("X won!",True,(0,0,255))
messageO = win_message.render("O won!",True,(255,0,0))
message_draw = win_message.render("Draw!",True,(0,0,0))
play = play_again.render("Click to play again.",True,(0,0,0))

X = True
screen.fill((255,255,255))

def start():
    screen.blit(message_start1,(20,50))
    screen.blit(message_start2,(170,150))
    screen.blit(message_start3,(320,250))
    pygame.draw.line(screen,(191,62,255),(0,415),(500,415),50)
    pygame.draw.line(screen,(0,0,0),(100,415),(400,415),50)
    pygame.draw.circle(screen,(255,127,0),[90,290],35)
    pygame.draw.line(screen,(0,205,0),(450,40),(350,140),5)
    pygame.draw.line(screen,(0,205,0),(350,40),(450,140),5)
    screen.blit(begin,(150,400))
    pygame.display.flip()
    tmp = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                tmp = True
                break
        if tmp:
            break
            print("hi")
    screen.fill((255,255,255))
    return True

def get_board():
    board = [[".",".","."],[".",".","."],[".",".","."]]
    return board

board = get_board()

def background():
    pygame.draw.line(screen,(0,0,0),[200,100],[200,400],5)
    pygame.draw.line(screen,(0,0,0),[300,100],[300,400],5)
    pygame.draw.line(screen,(0,0,0),[100,200],[400,200],5)
    pygame.draw.line(screen,(0,0,0),[100,300],[400,300],5)

def check():
    reset = False
    draw = True

    checklist = [[board[0][0],board[1][0],board[2][0]],
                 [board[0][1],board[1][1],board[2][1]],
                 [board[0][2],board[1][2],board[2][2]],
                 [board[0][2],board[1][1],board[2][0]],
                 [board[0][0],board[1][1],board[2][2]],
                  board[0],board[1],board[2]]

    for i in checklist:
        if all(x == i[0] for x in i) and not i[0] == ".":
            screen.fill((255,255,255))
            if i[0] == "X":
                screen.blit(messageX,(120,150))
            elif i[0] == "O":
                screen.blit(messageO,(120,150))
            screen.blit(play,(100,250))
            reset = True
            draw = False
            time.sleep(1)
            pygame.display.flip()
            break

    for i in board:
        for e in i:
            if e == ".":
                draw = False

    if draw:
        time.sleep(1)
        screen.fill((255,255,255))
        screen.blit(message_draw,(140,150))
        screen.blit(play,(100,250))
        pygame.display.flip()
        reset = True

    tmp = False
    if reset:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    screen.fill((255,255,255))
                    pygame.display.flip()
                    tmp = True
                    break
            if tmp:
                break
        return True
    else:
        return False

def move(X):
    while True:
        go = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                go = True
        if go:
            coords = pygame.mouse.get_pos()
            if 100 <= coords[0] <= 200 and 100 <= coords[1] <= 200:
                x1 = [110,110] ; x2 = [190,190] ; x3 = [190,110] ; x4 = [110,190]
                o = [150,150] ; pos = [0,0]
            elif 200 <= coords[0] <= 300 and 100 <= coords[1] <= 200:
                x1 = [210,110] ; x2 = [290,190] ; x3 = [290,110] ; x4 = [210,190]
                o = [250,150] ; pos = [0,1]
            elif 300 <= coords[0] <= 400 and 100 <= coords[1] <= 200:
                x1 = [310,110] ; x2 = [390,190] ; x3 = [390,110] ; x4 = [310,190]
                o = [350,150] ; pos = [0,2]
            elif 100 <= coords[0] <= 200 and 200 <= coords[1] <= 300:
                x1 = [110,210] ; x2 = [190,290] ; x3 = [190,210] ; x4 = [110,290]
                o = [150,250] ; pos = [1,0]
            elif 200 <= coords[0] <= 300 and 200 <= coords[1] <= 300:
                x1 = [210,210] ; x2 = [290,290] ; x3 = [290,210] ; x4 = [210,290]
                o = [250,250] ; pos = [1,1]
            elif 300 <= coords[0] <= 400 and 200 <= coords[1] <= 300:
                x1 = [310,210] ; x2 = [390,290] ; x3 = [390,210] ; x4 = [310,290]
                o = [350,250] ; pos = [1,2]
            elif 100 <= coords[0] <= 200 and 300 <= coords[1] <= 400:
                x1 = [110,310] ; x2 = [190,390] ; x3 = [190,310] ; x4 = [110,390]
                o = [150,350] ; pos = [2,0]
            elif 200 <= coords[0] <= 300 and 300 <= coords[1] <= 400:
                x1 = [210,310] ; x2 = [290,390] ; x3 = [290,310] ; x4 = [210,390]
                o = [250,350] ; pos = [2,1]
            elif 300 <= coords[0] <= 400 and 300 <= coords[1] <= 400:
                x1 = [310,310] ; x2 = [390,390] ; x3 = [390,310] ; x4 = [310,390]
                o = [350,350] ; pos = [2,2]
            else:
                x1,x2,x3,x4,o,pos = [0,0],[0,0],[0,0],[0,0],[0,0],[0,0]

            if X and board[pos[0]][pos[1]] == ".":
                pygame.draw.line(screen,(0,0,200),x1,x2,5)
                pygame.draw.line(screen,(0,0,200),x3,x4,5)
                board[pos[0]][pos[1]] = "X"
                break
            elif not X and board[pos[0]][pos[1]] == ".":
                pygame.draw.circle(screen,(200,0,0),o,45)
                pygame.draw.circle(screen,(255,255,255),o,40)
                board[pos[0]][pos[1]] = "O"
                break
            go = False
    X = not X
    return X

if start():
    while True:
        background()
        pygame.display.flip()
        X = move(X)
        pygame.display.flip()
        if check():
            board = get_board()
            X = True
        pygame.display.flip()
    
