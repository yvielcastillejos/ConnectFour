import pygame
import sys
import random
import numpy as np
from play import*
from main import BoardGame


background_img = pygame.image.load("/Users/yvielcastillejos/Desktop/Logo.png")
background_img = pygame.transform.scale(background_img,(400,100))

S_WIDTH = 700
S_HEIGHT = 600
GRIDSIZE = 50
GRID_WIDTH =  S_WIDTH/GRIDSIZE
GRID_HEIGHT = S_HEIGHT / GRIDSIZE
clr1 = (16, 62, 173) 
clr2 =(42, 157, 244) 
ply1clr =  (174, 62, 83) 
ply2clr = (230, 195, 32) 
selected = (96, 108, 118) 
unselected =(183, 190, 189) 

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size = (S_WIDTH+200,S_HEIGHT+200), flags = 0)
    surface = pygame.Surface(screen.get_size())
    board = BoardGame()
    surface = surface.convert()
    #draw the background
    draw_buttons(surface,1)
    screen.blit(background_img,(0,0))
    draw_background(surface, board)
    x = 1
    myfont = pygame.font.SysFont("fontname", 30)
    while True:
        clock.tick(10)
        screen.blit(background_img,(0,0))
        draw_background(surface, board)
        draw_buttons(surface, x)
        pos_t,x = event(surface,x)
        if x == 5:
            draw_buttons(surface, x)
            x = 1
            board = BoardGame()
        if pos_t != 1:
            board = playwithAI(pos_t[0], board, x)
            draw_background(surface, board)
        screen.blit(surface, (0,0))
        text1 = myfont.render("L1", 1, (0,0,0))
        screen.blit(text1, (65,365))
        text1 = myfont.render("L2", 1, (0,0,0))
        screen.blit(text1, (65,465))
        text1 = myfont.render("L3", 1, (0,0,0))
        screen.blit(text1, (65,565))
        text1 = myfont.render("Reset", 1, (0,0,0))
        screen.blit(text1, (49,650))
        if state(board) == 1:
                text2 = myfont.render("PLAYER 1 WON!", 1, (255,255,0))
                screen.blit(text2, (500,50))
        elif state(board) == 2:
                text2 = myfont.render("PLAYER 2 WON!", 1, (255,255,0))
                screen.blit(text2, (500,50))
        elif state(board) == 0:
                text2 = myfont.render("DRAW!", 1, (255,255,0))
                screen.blit(text2, (500,50))
        pygame.display.update()
    return


def event(surface,x):
    for event in pygame.event.get():
        pos = 5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if (pos[0] >50 and pos[0] <100) and (pos[1]>350 and pos[1]<400):
                x = 1
            elif (pos[0] >50 and pos[0] <100) and (pos[1]>450 and pos[1]<500):
                x= 3
            elif (pos[0] >50 and pos[0] <100) and (pos[1]>550 and pos[1]<600):
                x = 4
            elif (pos[0] >40 and pos[0] <125) and (pos[1]>650 and pos[1]<665):
                x = 5
            else:
                return pos,x
            return 1,x
        if event.type == pygame.MOUSEMOTION:
            posx = event.pos
            if posx[0] >150 and posx[0] <825:
                 pygame.draw.circle(surface, ply1clr, (posx[0], 150),30)
                 pygame.draw.circle(surface, (190,34,45), (posx[0], 150),30,5)
#                 pygame.display.update()
    return 1,x

def draw_background(surface, board):
    pygame.draw.rect(surface, (30,30,30), ((0,0),(S_HEIGHT+300, S_WIDTH+300)))
    surface.blit(background_img,(0,0))
    for y in range(0,int(GRID_HEIGHT)):
        for x in range(0,int(GRID_WIDTH)):
            r = pygame.Rect((GRIDSIZE*x+150, GRIDSIZE*y+200),(GRIDSIZE, GRIDSIZE))
            r1 = pygame.Rect((150, 200),(S_HEIGHT+100, S_WIDTH+100))
            pygame.draw.rect(surface, clr1, r)
            pygame.draw.rect(surface, clr2, r1,5)
    for y in range(0,int(GRID_HEIGHT),2):
        for x in range(0,int(GRID_WIDTH),2):
            pygame.draw.circle(surface, clr2, (GRIDSIZE*x+200, GRIDSIZE*y+250), 30)
    for x in range(0,len(board),1):
        for y in range(0,len(board[0]),1):
            if board[x][y] == 1:
                 pygame.draw.circle(surface, ply1clr, ((y*100+200), (x*100+250)), 30)
            if board[x][y] == 2:
                 pygame.draw.circle(surface, ply2clr, ((y*100+200), (x*100+250)), 30) 
    return

def draw_buttons(surface,x):
   myfont = pygame.font.SysFont("fontname", 20)
   r = pygame.Rect((50,350),(GRIDSIZE, GRIDSIZE))
   pygame.draw.rect(surface, unselected, r)
   pygame.draw.rect(surface, (205,205,205), r,5)
   r1 = pygame.Rect((50,450),(GRIDSIZE, GRIDSIZE))
   pygame.draw.rect(surface, unselected, r1)
   pygame.draw.rect(surface, (205,205,205), r1,5)
   r2 = pygame.Rect((50,550),(GRIDSIZE, GRIDSIZE))
   pygame.draw.rect(surface, unselected, r2)
   pygame.draw.rect(surface, (205,205,205) , r2,5)
   r3 = pygame.Rect((40,650),(GRIDSIZE+25, GRIDSIZE-25))
   pygame.draw.rect(surface, unselected, r3)
   pygame.draw.rect(surface, (205,205,205) , r3,5)
   if x == 1:
          pygame.draw.rect(surface, selected, r)
   if x == 3:
          pygame.draw.rect(surface, selected, r1)
   if x == 4:
          pygame.draw.rect(surface, selected, r2)
   if x == 5:
          pygame.draw.rect(surface, selected, r3)
          #pygame.draw.rect(surface, (205,205,205) , r3,5)
   return 
main()
