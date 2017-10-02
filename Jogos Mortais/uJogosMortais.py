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
cor_background = 255, 0, 0
deslocamento = [3, 3]

# image.load: Obter imagem de arquivo ## Fonte da Imagem: http://i49.tinypic.com/2u6214h.png
imagem = pygame.image.load("doll_1.png")

# get_rect(): Obter a área retangular da superfície/objeto/imagem
# Retorna um novo retângulo que cobre toda a superfície.
imagem_rect = imagem.get_rect()

# Game loop - Fixo
while True:
    # pygame.event.get(): Obter eventos da fila de eventos - Fixo
    for event in pygame.event.get():
        # Encerrar execução caso X de fechar da janela seja clicado - Fixo
        if event.type == pygame.QUIT: sys.exit()

    # .move(x, y): Move o retângulo (objeto/imagem)
    # Retorna um novo retângulo movido pelo deslocamento dado.
    # Os argumentos podem ser qualquer valor inteiro, positivo ou negativo.
    imagem_rect = imagem_rect.move(deslocamento)

    # As funções Rect que alteram a posição ou o tamanho de um Rect retornam uma nova cópia do Rect com as mudanças afetadas
    # O objeto Rect possui vários atributos virtuais que podem ser usados ​​para mover e alinhar o Rect:
    # Um Rect pode ser criado a partir de uma combinação de valores de left, right, width e height

    # Genericamente: SE o objeto tocar o canto esquedo ou direito da tela, ENTÃO movimente opostamente em x
    if imagem_rect.left < 0 or imagem_rect.right > width:
        deslocamento[0] = -deslocamento[0]
    # Genericamente: SE o objeto tocar o topo ou a base da tela, ENTÃO movimente opostamente em y
    if imagem_rect.top < 0 or imagem_rect.bottom > height:
        deslocamento[1] = -deslocamento[1]

    # janela.fill(x): Seta cor do Background da janela, x = R, G, B
    janela.fill(cor_background)
    # janela.blit(): Cria superfície dos objetos
    janela.blit(imagem, imagem_rect)
    # display.flip(): Atualiza a supercie da janela completamente
    pygame.display.flip()
