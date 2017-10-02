#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame

# pygame.init(): Inicializa todos os módulos pygame importados - Fixo
pygame.init()

# Configurações Básicas de janela {
tamanho = width, height = 800, 600
# display.set_mode: Inicializa janela com tamanho especificado
janela = pygame.display.set_mode(tamanho)
# display.set_caption: Define título da Janela
pygame.display.set_caption("Projeto Básico - Movimentando Objeto - CG 2017.1")

# Definição de variáveis
# Definindo background com uma cor RGB
cor_background = 255, 0, 0
# Definindo background com uma imagem
# Fonte Background: http://www.textures4photoshop.com/tex/thumbs/space-background-with-starfield-free-download-thumb45.jpg
background_imagem = "space.jpg"
background = pygame.image.load(background_imagem).convert()

deslocamento_1 = [1, 1]
deslocamento_2 = [2, 2]
deslocamento_3 = [4, 4]

# image.load: Obter imagem de arquivo
# Fonte das Imagems: http://www.softicons.com/web-icons/halloween-avatars-icons-by-deleket
alien_1 = pygame.image.load("alien_1.png")
alien_2 = pygame.image.load("alien_2.png")
alien_3 = pygame.image.load("alien_3.png")


# get_rect(): Obter a área retangular da superfície/objeto/imagem
# Retorna um novo retângulo que cobre toda a superfície.
alien_1_rect = alien_1.get_rect()
alien_2_rect = alien_2.get_rect()
alien_3_rect = alien_3.get_rect()

# Game loop - Fixo
while True:
    # pygame.event.get(): Obter eventos da fila de eventos - Fixo
    for event in pygame.event.get():
        # Encerrar execução caso X de fechar da janela seja clicado - Fixo
        if event.type == pygame.QUIT: sys.exit()

    # .move(x, y): Move o retângulo (objeto/imagem)
    # Retorna um novo retângulo movido pelo deslocamento dado.
    # Os argumentos podem ser qualquer valor inteiro, positivo ou negativo.
    alien_1_rect = alien_1_rect.move(deslocamento_1)
    alien_2_rect = alien_2_rect.move(deslocamento_2)
    alien_3_rect = alien_3_rect.move(deslocamento_3)

    # As funções Rect que alteram a posição ou o tamanho de um Rect retornam uma nova cópia do Rect com as mudanças afetadas
    # O objeto Rect possui vários atributos virtuais que podem ser usados ​​para mover e alinhar o Rect:
    # Um Rect pode ser criado a partir de uma combinação de valores de left, right, width e height

    # Genericamente: SE o objeto tocar o canto esquedo ou direito da tela, ENTÃO movimente opostamente em x
    if alien_1_rect.left < 0 or alien_1_rect.right > width:
        deslocamento_1[0] = -deslocamento_1[0]
    # Genericamente: SE o objeto tocar o topo ou a base da tela, ENTÃO movimente opostamente em y
    if alien_1_rect.top < 0 or alien_1_rect.bottom > height:
        deslocamento_1[1] = -deslocamento_1[1]

    # Genericamente: SE o objeto tocar o canto esquedo ou direito da tela, ENTÃO movimente opostamente em x
    if alien_2_rect.left < 0 or alien_2_rect.right > width:
        deslocamento_2[0] = -deslocamento_2[0]
    # Genericamente: SE o objeto tocar o topo ou a base da tela, ENTÃO movimente opostamente em y
    if alien_2_rect.top < 0 or alien_2_rect.bottom > height:
        deslocamento_2[1] = -deslocamento_2[1]

    # Genericamente: SE o objeto tocar o canto esquedo ou direito da tela, ENTÃO movimente opostamente em x
    if alien_3_rect.left < 0 or alien_3_rect.right > width:
        deslocamento_3[0] = -deslocamento_3[0]
    # Genericamente: SE o objeto tocar o topo ou a base da tela, ENTÃO movimente opostamente em y
    if alien_3_rect.top < 0 or alien_3_rect.bottom > height:
        deslocamento_3[1] = -deslocamento_3[1]

    # janela.fill(x): Seta cor do background da janela, x = R, G, B
    # janela.fill(cor_background)
    # screen.blit(x, y): Seta imagem como backgroud da janela, x = imagem, y = posição superior esquerda
    janela.blit(background, (0, 0))
    # janela.blit(): Cria superfície dos objetos
    janela.blit(alien_1, alien_1_rect)
    janela.blit(alien_2, alien_2_rect)
    janela.blit(alien_3, alien_3_rect)

    # display.flip(): Atualiza a supercie da janela completamente
    pygame.display.flip()
