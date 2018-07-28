#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, math
import sys

pygame.init()

# CONSTANTES -------------------------------------------------------------------

# PALETA DE CORES
WHITE       = (255, 255, 255) #FFFFFF
NEARBLACK   = ( 19,  15,  48) #130f30
RED         = (244,  67,  54) #F44336
ORANGE      = (255, 152,   0) #FF9800
PINK        = (233,  30,  99) #E91E63

# DISPLAY
GAME_TITLE      = 'uGame - CG 2017.1'
DISPLAY_FONTE   = pygame.font.SysFont('Quicksand', 22)
DISPLAY_WIDTH   = 1280
DISPLAY_HEIGHT  = 755
DISPLAY         = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
DISPLAY_CLOCK   = pygame.time.Clock()
BG_IMAGE        = pygame.image.load('assets/images/background.png').convert()
BG_COLOR        = NEARBLACK
FPS             = 30

pygame.key.set_repeat(1, 1)
clock = pygame.time.Clock()

# OBJETOS - LIFE
LIFE_P1_TRUE_IMG    = pygame.image.load("assets/images/life_true.png")
LIFE_P2_TRUE_IMG    = pygame.image.load("assets/images/life_true.png")
LIFE_P1_FALSE_IMG   = pygame.image.load("assets/images/life_false.png")
LIFE_P2_FALSE_IMG   = pygame.image.load("assets/images/life_false.png")

# GAME CONTROLE
GAME_CONTROLLER_IMG = pygame.image.load("assets/images/game_controller.png")

# BALLETS CP
BULLET_1_CP         = pygame.image.load("assets/images/bullet_1_cp.png")
BULLET_2_CP         = pygame.image.load("assets/images/bullet_2_cp.png")
BULLET_3_CP         = pygame.image.load("assets/images/bullet_3_cp.png")

# WINS
PLAYER_1_WINS_IMG         = pygame.image.load("assets/images/p1_wins.png")
PLAYER_2_WINS_IMG         = pygame.image.load("assets/images/p2_wins.png")

# YOSHI_P1
PLAYER_1_IMG          = pygame.image.load("assets/images/p1.png")
PLAYER_1_IMG_GUN      = pygame.image.load("assets/images/gun_p1.png")
PLAYER_1_BULLET_1_IMG = pygame.image.load("assets/images/bullet_1.png")
PLAYER_1_BULLET_2_IMG = pygame.image.load("assets/images/bullet_2.png")
PLAYER_1_BULLET_3_IMG = pygame.image.load("assets/images/bullet_3.png")

# YOSHI_P2
PLAYER_2_IMG          = pygame.image.load("assets/images/p2.png")
PLAYER_2_IMG_GUN      = pygame.image.load("assets/images/gun_p2.png")
PLAYER_2_BULLET_1_IMG = pygame.image.load("assets/images/bullet_1.png")
PLAYER_2_BULLET_2_IMG = pygame.image.load("assets/images/bullet_2.png")
PLAYER_2_BULLET_3_IMG = pygame.image.load("assets/images/bullet_4.png")

# RECTS_P1
PLAYER_1_RECT          = pygame.Rect( 50, 650, 64, 64)
PLAYER_1_GUN_RECT      = pygame.Rect( 45, 680, 88, 10)
PLAYER_1_BULLET_1_RECT = pygame.Rect(125, 678, 12, 12)
PLAYER_1_BULLET_2_RECT = pygame.Rect(125, 678, 12, 12)
PLAYER_1_BULLET_3_RECT = pygame.Rect(125, 678, 64, 64)

# RECTS_P2
PLAYER_2_RECT          = pygame.Rect(1166, 650, 64, 64)
PLAYER_2_GUN_RECT      = pygame.Rect(1147, 680, 88, 10)
PLAYER_2_BULLET_1_RECT = pygame.Rect(1143, 678, 12, 12)
PLAYER_2_BULLET_2_RECT = pygame.Rect(1143, 678, 12, 12)
PLAYER_2_BULLET_3_RECT = pygame.Rect(1143, 678, 64, 64)

# VARIÁVEIS --------------------------------------------------------------------

# BALÍSTICA - LANÇAMENTO OBLÍCUO
t = 0
v = (0, 0)

# PLAYER 1
p1_angle = 0
p1_power = 50
p1_life = 3
p1_distance = 0
p1_bullet = 1

# PLAYER 2
p2_angle = 0
p2_power = 50
p2_life = 3
p2_distance = 0
p2_bullet = 1

# playing_time = 15
MOV_X = 5
MOV_Y = 5

gun_p1_center_x = 90
gun_p1_center_y = 685

gun_p2_center_x = DISPLAY_WIDTH - 95
gun_p2_center_y = 683

p1_wins = False
p2_wins = False

PLAYER_1 = True
PLAYER_2 = False

# FUNCOES ----------------------------------------------------------------------
# PAINEL DE CONTROLE
def controlPanel():
        # PLAYER 1 - TEXTOS

        # LIFE - IMAGENS
        if p1_life == 3:
            DISPLAY.blit(LIFE_P1_TRUE_IMG, [20, 20])
            DISPLAY.blit(LIFE_P1_TRUE_IMG, [52, 20])
            DISPLAY.blit(LIFE_P1_TRUE_IMG, [84, 20])
        if p1_life == 2:
            DISPLAY.blit(LIFE_P1_FALSE_IMG, [20, 20])
            DISPLAY.blit(LIFE_P1_TRUE_IMG, [52, 20])
            DISPLAY.blit(LIFE_P1_TRUE_IMG, [84, 20])
        if p1_life == 1:
            DISPLAY.blit(LIFE_P1_FALSE_IMG, [20, 20])
            DISPLAY.blit(LIFE_P1_FALSE_IMG, [52, 20])
            DISPLAY.blit(LIFE_P1_TRUE_IMG, [84, 20])
        if p1_life == 0:
            DISPLAY.blit(LIFE_P1_FALSE_IMG, [20, 20])
            DISPLAY.blit(LIFE_P1_FALSE_IMG, [52, 20])
            DISPLAY.blit(LIFE_P1_FALSE_IMG, [84, 20])

        # ANGLE - TEXTO
        player1_text_angle = DISPLAY_FONTE.render("A " + str(p1_angle), True, WHITE)
        DISPLAY.blit(player1_text_angle, [184, 21])

        # POWER - TEXTO
        player1_text_power = DISPLAY_FONTE.render("P " + str(p1_power), True, WHITE)
        DISPLAY.blit(player1_text_power, [284, 21])

        # DISTANCE - TEXTO
        player1_text_distance = DISPLAY_FONTE.render("DM " + str(p1_distance), True, WHITE)
        DISPLAY.blit(player1_text_distance, [384, 20])

        # BULLET
        if PLAYER_1:
            if p1_bullet == 1:
                DISPLAY.blit(BULLET_1_CP, [484, 20])
            if p1_bullet == 2:
                DISPLAY.blit(BULLET_2_CP, [484, 20])
            if p1_bullet == 3:
                DISPLAY.blit(BULLET_3_CP, [484, 20])

        # INDICADOR DE JOGADA E TIMER ------------------------------------------
        if PLAYER_1:
            DISPLAY.blit(GAME_CONTROLLER_IMG, [524, 21])
        if PLAYER_2:
            DISPLAY.blit(GAME_CONTROLLER_IMG, [724, 21])

        #playing_time_text = DISPLAY_FONTE.render(str(playing_time), True, RED)
        #DISPLAY.blit(playing_time_text, [631, 51])
        # ----------------------------------------------------------------------

        # PLAYER 2
        # LIFE - IMAGENS
        if p2_life == 3:
            DISPLAY.blit(LIFE_P2_TRUE_IMG, [1230, 20])
            DISPLAY.blit(LIFE_P2_TRUE_IMG,  [1198, 20])
            DISPLAY.blit(LIFE_P2_TRUE_IMG,  [1166, 20])
        if p2_life == 2:
            DISPLAY.blit(LIFE_P2_TRUE_IMG, [1230, 20])
            DISPLAY.blit(LIFE_P2_TRUE_IMG,  [1198, 20])
            DISPLAY.blit(LIFE_P2_FALSE_IMG,  [1166, 20])
        if p2_life == 1:
            DISPLAY.blit(LIFE_P2_TRUE_IMG, [1230, 20])
            DISPLAY.blit(LIFE_P2_FALSE_IMG,  [1198, 20])
            DISPLAY.blit(LIFE_P2_FALSE_IMG,  [1166, 20])
        if p2_life == 0:
            DISPLAY.blit(LIFE_P2_FALSE_IMG, [1230, 20])
            DISPLAY.blit(LIFE_P2_FALSE_IMG,  [1198, 20])
            DISPLAY.blit(LIFE_P2_FALSE_IMG,  [1166, 20])

        # ANGLE - TEXTO
        player2_text_angle = DISPLAY_FONTE.render("A " + str(abs(p2_angle)), True, WHITE)
        DISPLAY.blit(player2_text_angle, [1066, 20])

        # POWER - TEXTO
        player2_text_power = DISPLAY_FONTE.render("P " + str(abs(p2_power)), True, WHITE)
        DISPLAY.blit(player2_text_power, [966, 20])

        # DISTANCE - TEXTO
        player2_text_distance = DISPLAY_FONTE.render("DM " + str(abs(p2_distance)), True, WHITE)
        DISPLAY.blit(player2_text_distance, [866, 20])

        # BULLET
        if PLAYER_2:
            if p2_bullet == 1:
                DISPLAY.blit(BULLET_1_CP, [766, 20])
            if p2_bullet == 2:
                DISPLAY.blit(BULLET_2_CP, [766, 20])
            if p2_bullet == 3:
                DISPLAY.blit(BULLET_3_CP, [766, 20])

def player1_wins():
    print("PLAYER 1 - WIN")
    DISPLAY.blit(PLAYER_1_WINS_IMG, [0, 0])
    pygame.display.update()
    while p1_wins:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        clock.tick(5)

def player2_wins():
    print("PLAYER 2 - WIN")
    DISPLAY.blit(PLAYER_2_WINS_IMG, [0, 0])
    pygame.display.update()

    while p2_wins:
        controlPanel()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        clock.tick(5)

# AJUSTAR ANGULO
def turnGun():
    rPLAYER_1_IMG_GUN = pygame.transform.rotate(PLAYER_1_IMG_GUN, p1_angle)
    rotatedRect = rPLAYER_1_IMG_GUN.get_rect()
    rotatedRect.center = (gun_p1_center_x, gun_p1_center_y)
    DISPLAY.blit(rPLAYER_1_IMG_GUN, rotatedRect)

    rPLAYER_2_IMG_GUN = pygame.transform.rotate(PLAYER_2_IMG_GUN, p2_angle)
    rotatedRect = rPLAYER_2_IMG_GUN.get_rect()
    rotatedRect.center = (gun_p2_center_x, gun_p2_center_y)
    DISPLAY.blit(rPLAYER_2_IMG_GUN, rotatedRect)

    if PLAYER_1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fireShell_p1(gun_p1_center_x, gun_p1_center_y, p1_angle, p1_power)
    if PLAYER_2:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fireShell_p2(gun_p2_center_x, gun_p2_center_y, p2_angle, p2_power)


# LANCAMENTO E DETECCAO DE COLISAO PLAYER 1
def fireShell_p1(gun_p1_center_x, gun_p1_center_y, p1_angle, p1_power):
    global t, dt, v, p2_life, p1_wins, PLAYER_1_BULLET_1_RECT, PLAYER_1_BULLET_2_RECT, PLAYER_1_BULLET_3_RECT
    t = 0
    fire = True

    bx = gun_p1_center_x
    by = gun_p1_center_y

    DISPLAY.blit(PLAYER_1_IMG, PLAYER_1_RECT)
    DISPLAY.blit(PLAYER_2_IMG, PLAYER_2_RECT)

    while fire:
        print("P1", bx, by)
        if p1_bullet == 1:
            DISPLAY.blit(PLAYER_1_BULLET_1_IMG, (bx-5, by-5))
            PLAYER_1_BULLET_1_RECT.x = bx-5
            PLAYER_1_BULLET_1_RECT.y = by-5
        if p1_bullet == 2:
            DISPLAY.blit(PLAYER_1_BULLET_2_IMG, (bx-5, by-5))
            PLAYER_1_BULLET_2_RECT.x = bx-5
            PLAYER_1_BULLET_2_RECT.y = by-5
        if p1_bullet == 3:
            DISPLAY.blit(PLAYER_1_BULLET_3_IMG, (bx, by))
            PLAYER_1_BULLET_3_RECT.x = bx
            PLAYER_1_BULLET_3_RECT.y = by

        # BALISTICA ITEM 2.4
        #bx = bx + p1_power *(math.cos(p1_angle))
        #by = by + p1_power *(math.sin(p1_angle))

        # LANCAMENTO OBLÍCUO - BALISTICA ITEM 3.9
        t  = t + dt/250.0
        a  = (0.0, 10.0)
        v0 = (p1_power * math.cos(math.radians(p1_angle)), -p1_power * math.sin(math.radians(p1_angle)))
        v  = (v0[0] + a[0] * t, v0[1] + a[1] * t)
        vm = math.sqrt(v[0] * v[0] + v[1] * v[1])
        s0 = (gun_p1_center_x, gun_p1_center_y)

        bx  = (gun_p1_center_x + v0[0] * t + a[0] * t * t / 2)
        by  = (gun_p1_center_y + v0[1] * t + a[1] * t * t / 2)

        # DETECCAO DE COLISAO
        if PLAYER_1_BULLET_1_RECT.colliderect(PLAYER_2_RECT) or PLAYER_1_BULLET_2_RECT.colliderect(PLAYER_2_RECT) or PLAYER_1_BULLET_3_RECT.colliderect(PLAYER_2_RECT):
            print("COLIDIU")
            p2_life -= 1

            if p2_life <= 0:
                p1_wins = True

            fire = False

        if abs(bx) > abs(DISPLAY_WIDTH) or abs(by) > abs(715):
            fire = False

        pygame.display.update()
        #clock.tick(15)

    # DESABILITA JOGADA
    global PLAYER_1
    global PLAYER_2
    PLAYER_1 = False
    PLAYER_2 = True

def fireShell_p2(gun_p2_center_x, gun_p2_center_y, p2_angle, p2_power):
    global t, dt, v, p1_life, p2_wins, PLAYER_2_BULLET_1_RECT, PLAYER_2_BULLET_2_RECT, PLAYER_2_BULLET_3_RECT
    t = 0
    fire = True

    bx = gun_p2_center_x
    by = gun_p2_center_y

    DISPLAY.blit(PLAYER_2_IMG, PLAYER_2_RECT)
    DISPLAY.blit(PLAYER_1_IMG, PLAYER_1_RECT)

    while fire:
        print(bx, by)
        if p2_bullet == 1:
            DISPLAY.blit(PLAYER_2_BULLET_1_IMG, (bx-5, by-5))
            PLAYER_2_BULLET_1_RECT.x = bx-5
            PLAYER_2_BULLET_1_RECT.y = by-5
        if p2_bullet == 2:
            DISPLAY.blit(PLAYER_2_BULLET_2_IMG, (bx-5, by-5))
            PLAYER_2_BULLET_2_RECT.x = bx-5
            PLAYER_2_BULLET_2_RECT.y = by-5
        if p1_bullet == 3:
            DISPLAY.blit(PLAYER_2_BULLET_3_IMG, (bx, by))
            PLAYER_2_BULLET_3_RECT.x = bx
            PLAYER_2_BULLET_3_RECT.y = by

        # BALISTICA ITEM 2.4
        #bx = bx + p2_power *(math.cos(p2_angle))
        #by = by + p2_power *(math.sin(p2_angle))

        # LANCAMENTO OBLÍCUO - BALISTICA ITEM 3.9
        t  = t + dt / 250.0
        a  = (0.0, 10.0)
        v0 = (p2_power * math.cos(math.radians(p2_angle)), p2_power * math.sin(math.radians(p2_angle)))
        v  = (v0[0] + a[0] * t, v0[1] + a[1] * t)
        vm = math.sqrt(v[0] * v[0] + v[1] * v[1])
        s0 = (gun_p2_center_x, gun_p2_center_y)

        bx  = (gun_p2_center_x - v0[0] * t + a[0] * t * t / 2)
        by  = (gun_p2_center_y + v0[1] * t + a[1] * t * t / 2)

        # DETECCAO DE COLISAO
        if PLAYER_2_BULLET_1_RECT.colliderect(PLAYER_1_RECT) or PLAYER_2_BULLET_2_RECT.colliderect(PLAYER_1_RECT) or PLAYER_2_BULLET_3_RECT.colliderect(PLAYER_1_RECT):
            print("COLIDIU")
            p1_life -= 1

            if p1_life <= 0:
                p2_wins = True

            fire = False

        if abs(bx) > abs(DISPLAY_WIDTH) or abs(by) > abs(715):
            fire = False

        pygame.display.update()
        #clock.tick(15)

    global PLAYER_1
    global PLAYER_2
    PLAYER_1 = True
    PLAYER_2 = False

# GAME LOOP > ------------------------------------------------------------------

while True:
    dt = clock.tick(FPS) # dt = t_now - t_previous

    # EXIBIBE VENCEDOR
    if p1_wins: player1_wins()
    if p2_wins: player2_wins()

    # EVENTOS DO TECLADO
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:

            # K_RIGHT
            if event.key == pygame.K_RIGHT:
                if PLAYER_1:
                    PLAYER_1_RECT.move_ip(MOV_X, 0)
                    gun_p1_center_x += 5
                    p1_distance += 1
                if PLAYER_2:
                    PLAYER_2_RECT.move_ip(MOV_X, 0)
                    gun_p2_center_x += 5
                    p2_distance += 1

            # K_LEFT
            if event.key == pygame.K_LEFT:
                if PLAYER_1:
                    PLAYER_1_RECT.move_ip(-MOV_X, 0)
                    gun_p1_center_x -= 5
                    p1_distance -= 1
                if PLAYER_2:
                    PLAYER_2_RECT.move_ip(-MOV_X, 0)
                    gun_p2_center_x -= 5
                    p2_distance -= 1

            # K_UP
            if event.key == pygame.K_UP:
                if PLAYER_1:
                    p1_angle = p1_angle + 1
                    if p1_angle > 90:
                        p1_angle = 90
                if PLAYER_2:
                    p2_angle = p2_angle - 1
                    if p2_angle < -90:
                        p2_angle = -90

            # K_DOWN
            if event.key == pygame.K_DOWN:
                if PLAYER_1:
                    p1_angle = p1_angle - 1
                    if p1_angle < 0:
                        p1_angle = 0
                if PLAYER_2:
                    p2_angle = p2_angle + 1
                    if p2_angle > 0:
                        p2_angle = 0

            # K_A
            if event.key == pygame.K_s:
                if PLAYER_1:
                    p1_power = p1_power + 1
                    if p1_power > 100:
                        p1_power = 100
                if PLAYER_2:
                    p2_power = p2_power + 1
                    if p2_power > 100:
                        p2_power = 100

            # K_S
            if event.key == pygame.K_a:
                if PLAYER_1:
                    p1_power = p1_power - 1
                    if p1_power < 0:
                        p1_power = 0
                if PLAYER_2:
                    p2_power = p2_power - 1
                    if p2_power < 0:
                        p2_power = 0

            # K_1
            if event.key == pygame.K_1:
                if PLAYER_1:
                    p1_bullet = 1
                if PLAYER_2:
                    p2_bullet = 1

            # K_2
            if event.key == pygame.K_2:
                if PLAYER_1:
                    p1_bullet = 2
                if PLAYER_2:
                    p2_bullet = 2

            # K_3
            if event.key == pygame.K_3:
                if PLAYER_1:
                    p1_bullet = 3
                if PLAYER_2:
                    p2_bullet = 3

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        if PLAYER_1:
            PLAYER_1_RECT.move_ip(MOV_X, 0)
            gun_p1_center_x += 5
            p1_distance += 1
        if PLAYER_2:
            PLAYER_2_RECT.move_ip(MOV_X, 0)
            gun_p2_center_x += 5
            p2_distance += 1
        if PLAYER_1:
            p1_angle = p1_angle + 1
            if p1_angle > 90:
                p1_angle = 90
        if PLAYER_2:
            p2_angle = p2_angle - 1
            if p2_angle < -90:
                p2_angle = -90

    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            if PLAYER_1:
                PLAYER_1_RECT.move_ip(MOV_X, 0)
                gun_p1_center_x += 5
                p1_distance += 1
            if PLAYER_2:
                PLAYER_2_RECT.move_ip(MOV_X, 0)
                gun_p2_center_x += 5
                p2_distance += 1
            if PLAYER_1:
                p1_angle = p1_angle - 1
                if p1_angle < 0:
                    p1_angle = 0
            if PLAYER_2:
                p2_angle = p2_angle + 1
                if p2_angle > 0:
                    p2_angle = 0

    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            if PLAYER_1:
                PLAYER_1_RECT.move_ip(-MOV_X, 0)
                gun_p1_center_x -= 5
                p1_distance -= 1
            if PLAYER_2:
                PLAYER_2_RECT.move_ip(-MOV_X, 0)
                gun_p2_center_x -= 5
                p2_distance -= 1
            if PLAYER_1:
                p1_angle = p1_angle + 1
                if p1_angle > 90:
                    p1_angle = 90
            if PLAYER_2:
                p2_angle = p2_angle - 1
                if p2_angle < -90:
                    p2_angle = -90

    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            if PLAYER_1:
                PLAYER_1_RECT.move_ip(-MOV_X, 0)
                gun_p1_center_x -= 5
                p1_distance -= 1
            if PLAYER_2:
                PLAYER_2_RECT.move_ip(-MOV_X, 0)
                gun_p2_center_x -= 5
                p2_distance -= 1
            if PLAYER_1:
                p1_angle = p1_angle - 1
                if p1_angle < 0:
                    p1_angle = 0
            if PLAYER_2:
                p2_angle = p2_angle + 1
                if p2_angle > 0:
                    p2_angle = 0

            # K_SPACE
            #if event.key == pygame.K_SPACE:
            #    if PLAYER_1:
            #        fireShell_p1(gun_p1_center_x, gun_p1_center_y, p1_angle, p1_power)
            #    if PLAYER_2:
            #        fireShell_p2(gun_p2_center_x, gun_p2_center_y, p2_angle, p2_power)

    # DISPLAY ------------------------------------------------------------------

    # BACKGROUND
    #DISPLAY.fill(BG_COLOR)
    DISPLAY.blit(BG_IMAGE, (0, 0))

    # CENARIO | EVENTOS | OBJETOS
    controlPanel()

    # LANCAMENTO | DETECCAO DE COLISAO | LANCAMENTO
    turnGun()

    # BLIT OBJETOS
    DISPLAY.blit(PLAYER_1_IMG, PLAYER_1_RECT)
    DISPLAY.blit(PLAYER_2_IMG, PLAYER_2_RECT)

    DISPLAY_CLOCK.tick(FPS) #27
    pygame.display.update()
