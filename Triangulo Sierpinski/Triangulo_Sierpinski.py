#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Computação Gráfica - Unidade II
#  Triangulo_Sierpinski.py
#  GPLv3 - 15 de Setembro de 2017, Alex Aquino dos Santos <Alex@localhost.localdomain>

# Referências
    # Triângulo de Sierpinski : https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Sierpinski
    # Documentação Turtle     : https://docs.python.org/2/library/turtle.html
    # Tutorial Sierpinski     : http://prorum.com/index.php/3104/construir-fractal-conhecido-sierpinski-utilizando-recursoes

#Importação do Módulo turtle
import turtle


def desenhar_triangulo(vertices, cor, my_turtle): # Desenha Triângulo
    # fillcolor: Coloriza a "turtle"
    my_turtle.fillcolor(cor)
    # up: Eleva a "turtle" (não deseha ao se mover)
    my_turtle.up()
    # goto: Move a "turtle" para uma posição absoluta
    my_turtle.goto(vertices[0][0], vertices[0][1])
    # down: Baixa a "turtle" (deseha ao se mover)
    my_turtle.down()
    # begin_fill: Indica que a forma será preenchida/colorizada em "end_fill()"
    my_turtle.begin_fill()
    my_turtle.goto(vertices[1][0], vertices[1][1])
    my_turtle.goto(vertices[2][0], vertices[2][1])
    my_turtle.goto(vertices[0][0], vertices[0][1])
    # end_fill: Preenche/Coloriza a forma após a última chamada para begin_fill()
    my_turtle.end_fill()


def ponto_medio(ponto_1, ponto_2):
    # Calculando e retornando os pontos médios do triângulo original
    # Retorna uma tupla [pm1, pm2]
    return [(ponto_1[0] + ponto_2[0]) / 2, (ponto_1[1] + ponto_2[1]) / 2]


def sierpinski(vertices, nivel, my_turtle):
    # Paleta de cores para colorir formas
    cores = [(0, 150, 189), (4, 150, 116), (216, 95, 30), (193, 33, 57),(129, 41, 199), (102, 205, 135), (51, 187, 204)]
    # Desenhar Triângulo
    desenhar_triangulo(vertices, cores[nivel], my_turtle)
    # Caso nível maior que 0, desenha novos triângulos em novas posições absolutas
    if nivel > 0:

        sierpinski([vertices[0],
                      ponto_medio(vertices[0], vertices[1]),
                      ponto_medio(vertices[0], vertices[2])],
                      nivel - 1, my_turtle)
        sierpinski([vertices[1],
                      ponto_medio(vertices[0], vertices[1]),
                      ponto_medio(vertices[1], vertices[2])],
                      nivel - 1, my_turtle)
        sierpinski([vertices[2],
                      ponto_medio(vertices[2], vertices[1]),
                      ponto_medio(vertices[0], vertices[2])],
                      nivel - 1, my_turtle)

# Criando uma "turtle" (caneta)
my_turtle = turtle.Turtle()
# Criando Janela
screen = turtle.Screen()
# Definindo modo de cor da Janela
screen.colormode(255)
# Definindo posições absolutas dos vertices
vertices = [[-200, -100], [0, 200], [200, -100]]
# Definindo nível (recursão)
nivel = 4

# Inicia o processo de execução da aplicação
sierpinski(vertices, nivel, my_turtle)
# Encerrar execução caso X de fechar da janela seja clicado
screen.exitonclick()
