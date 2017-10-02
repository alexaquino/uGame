#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame
from random import randrange

# pygame.init(): Inicializa todos os módulos pygame importados - Fixo
pygame.init()

# Configurações Básicas de janela {
tamanho = width, height = 800, 600
# display.set_mode: Inicializa janela com tamanho especificado
janela = pygame.display.set_mode(tamanho)
# display.set_caption: Define título da Janela
pygame.display.set_caption("Projeto Básico - Movimentando Objeto - CG 2017.1")

# Definição de variáveis
cor_background = 255, 255, 255
deslocamento = [2, 2]
mudar_backgraund = 0

# image.load: Obter imagem de arquivo # Fonte da Imagem: http://i49.tinypic.com/2u6214h.png
donuts = pygame.image.load("donuts.png")

# get_rect(): Obter a área retangular da superfície/objeto/imagem
# Retorna um novo retângulo que cobre toda a superfície.
donuts_rect = donuts.get_rect()

# Game loop - Fixo
while True:
    # pygame.event.get(): Obter eventos da fila de eventos - Fixo
    for event in pygame.event.get():
        # Encerrar execução caso X de fechar da janela seja clicado - Fixo
        if event.type == pygame.QUIT: sys.exit()

    # .move(x, y): Move o retângulo (objeto/imagem)
    # Retorna um novo retângulo movido pelo deslocamento dado.
    # Os argumentos podem ser qualquer valor inteiro, positivo ou negativo.
    donuts_rect = donuts_rect.move(deslocamento)

    # As funções Rect que alteram a posição ou o tamanho de um Rect retornam uma nova cópia do Rect com as mudanças afetadas
    # O objeto Rect possui vários atributos virtuais que podem ser usados ​​para mover e alinhar o Rect:
    # Um Rect pode ser criado a partir de uma combinação de valores de left, right, width e height

    # Genericamente: SE o objeto tocar o canto esquedo ou direito da tela, ENTÃO movimente opostamente em x
    if donuts_rect.left < 0 or donuts_rect.right > width:
        deslocamento[0] = -deslocamento[0]
    # Genericamente: SE o objeto tocar o topo ou a base da tela, ENTÃO movimente opostamente em y
    if donuts_rect.top < 0 or donuts_rect.bottom > height:
        deslocamento[1] = -deslocamento[1]

    mudar_backgraund += 1

    if mudar_backgraund == 100:
        cor_background = (randrange(255), randrange(255), randrange(255))
        mudar_backgraund = 0

    # janela.fill(x): Seta cor do Background da janela, x = R, G, B
    janela.fill(cor_background)
    # janela.blit(): Cria superfície dos objetos
    janela.blit(donuts, donuts_rect)
    # display.flip(): Atualiza a supercie da janela completamente
    pygame.display.flip()
