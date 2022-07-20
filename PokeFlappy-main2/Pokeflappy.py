from turtle import Screen
import numpy as np
import pygame
import math
import button
import pymunk
from pygame.locals import *
import pymunk.pygame_util

#=====================================================================================================================================================#

#Alguns componentes serão retirados, visto que sua implantação foram visadas como forma de se testar o funcionamento de determinado recurso
#ALém disso, haverá alteração no modelo de alguns botões, adição de um título apropriado, mudança de fonte textual e na estética de algumas telas
#Caso sobre tempo, sprites novos serão adicionados como forma de disponibilizar ao usuário um modelo de personalização à gosto

#======================================================================================================================================================#


def create_poke(space): #cria o bloco de colisão do personagem principal
    body = pymunk.Body(10,100, body_type = pymunk.Body.DYNAMIC) #mass, inertia and type
    body.position = (50,300) #posição inicial do bloco
    shape = pymunk.Circle(body, 30) #cria o formato do bloco de colisão
    space.add(body, shape) #adiciona o corpo
    return shape

def draw_poke(characters): #desenha o personagem na tela
    for character in characters:
        posxx = int(character.body.position.x)
        posyy = int(character.body.position.y)
        character_rect = character_surface.get_rect(center = (posxx, posyy))
        screen.blit(character_surface, character_rect)

def create_static(space): #cria um bloco de colisões
    body = pymunk.Body(body_type = pymunk.Body.STATIC) #mass, inertia and type
    body.position = (50,500)
    #shape = pymunk.Poly.create_box(body,(90,90))
    shape = pymunk.Circle(body, 20)
    space.add(body, shape)
    return shape

def draw_static(balls): #desenha uma esfera
    for ball in balls:
        posxx = int(ball.body.position.x)
        posyy = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(posxx,posyy),20)

def pause(): #funcao de pause
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        menu = "main"
        pygame.display.update()
        clock.tick(5)

if __name__ == "__main__":

 # ================ variaveis ======================
    pygame.init() 
    pygame.display.set_caption("PokeFlappy") # muda o titulo da tela
    FPS = 60  # frames por segundo
    scroll_x = 0
    width = 400 # largura da tela
    height = 800 # altura da tela
    clock = pygame.time.Clock() 
    screen = pygame.display.set_mode((width, height)) #inicia a tela do pygame
    pygame.mouse.set_cursor(*pygame.cursors.broken_x) #altera o modelo do cursor
    menu = "main" #determina o menu inicial como main
    volume = 0.5 #volume inicial da trilha sonora
    volume_texto = round(volume*100, 0) #texto que representa o volume configurado pelo usuario
    music_text = []
    musicas = 1 #variavel que determina alteração de tirlha sonora
    space = pymunk.Space() #cria o espaço de simulação
    space.gravity = (0,600) #determina aceleração gravitacional horizontal e vertical, respectivamente
    character_size = (90,90) #tamanho do modelo do pesonagem
    surface = pygame.image.load('images/magikarp.png') #carrega modelo do personagem
    character_size = pygame.transform.scale(surface, character_size) #redimensiona o personagem ao tamanho escolhido em outra variavel
    character_surface = pygame.transform.flip(character_size, True, False) #gira o personagem 180°

    characters = []
    characters.append(create_poke(space)) #cria o bloco de colisão do personagem principal

    balls = []
    balls.append(create_static(space)) #cria o bloco de colisão de um obstáculo - puramente para testes

# ===============================================

    #inicia uma fonte de texto      
    pygame.font.init() 
    fonte = pygame.font.Font("fonts/Eight-Bit Madness.ttf",50) 
    fonte_menu = pygame.font.SysFont('Eight-Bit Madness.ttf', 50)
    volume_text = fonte_menu.render(str(volume_texto), 1, (255,255,255)) #fonte da barra de volumes

    #background
    scene = pygame.image.load("images/background.jpg")
    scene = pygame.transform.scale(scene, (width, height))

    #musica
    pygame.mixer.music.load("music/music1.ogg") #musica
    pygame.mixer.music.play(-1) #loop
    pygame.mixer.music.set_volume(volume) #volume
    music_text = fonte_menu.render("Musica 1", 1, (255,255,255))

# ================= Botões ===================

    #Botão de play
    play_img = pygame.image.load("images/play2.png").convert_alpha() #carregar imagem do botão
    play_size = (240, 160)                                           #tamanho da imagem
    play_img = pygame.transform.scale(play_img, play_size)           #dimensionamento da imagem
    play_button = button.Button(80, 290, play_img, 1)                #faz com que a imagem dimensionada funcione como um botão

    #botão de options
    options_img = pygame.image.load("images/option3.png").convert_alpha()
    options_size = (100,100)
    options_img = pygame.transform.scale(options_img, options_size)
    options_button = button.Button(1, 320, options_img, 1) \
    
    # botão leaderboards
    lb_img = pygame.image.load("images/leaderboard2.png").convert_alpha()
    lb_size = (90,120)
    lb_img = pygame.transform.scale(lb_img, lb_size)
    lb_button = button.Button(300, 300, lb_img, 1)

    #botão back
    back_img = pygame.image.load("images/back2.png").convert_alpha()
    back_size = (80, 80)
    back_img = pygame.transform.scale(back_img, back_size)
    back_button = button.Button(1, 1, back_img, 1)

    #botão aumentar volume
    volup_img = pygame.image.load("images/volume_up.png").convert_alpha()
    volup_size = (100,100)
    volup_img = pygame.transform.scale(volup_img, volup_size)
    volup_button = button.Button(300, 350, volup_img, 1)

    #botão diminuir volume
    voldown_img = pygame.image.load("images/volume_down.png").convert_alpha()
    voldown_size = (100,100)
    voldown_img = pygame.transform.scale(voldown_img, voldown_size)
    voldown_button = button.Button(1, 350, voldown_img, 1)

    #botao mudar a musica 
    msc_img = pygame.image.load("images/volume_up.png").convert_alpha()
    msc_size = (100,100)
    msc_img = pygame.transform.scale(msc_img, msc_size)
    msc_button = button.Button(300, 450, msc_img, 1)

 # ====================================================================================

    #loop inicial do jogo
    game_on = True
    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False            
            if event.type == pygame.KEYDOWN:#funcao de pausar o jogo
                if event.key == pygame.K_p: #quando a tecla 'p' é pressionada, o joog pausa
                    pause()
                if event.key == pygame.K_w: #quando a tecla'w' é pressionada, a gravidade do jogo diminui - personagem sobe
                    space.gravity = (0,-600)
                if event.key == pygame.K_s: #quando a tecla'w' é pressionada, a gravidade do jogo aumenta - personagem desce
                    space.gravity = (0,600)
        for i in range(0, 5):  # garante que há continuidade na movimentação do cenário
            screen.blit(scene, (i * scene.get_width() + scroll_x, 0))
        scroll_x -= 2
        if (abs(scroll_x) > width):
            scroll_x = 0

    #configura a troca de telas

        #==========Configuração de telas ==============
        if menu == "main": #determina a 1a tela do jogo como tela de menu inicial
            if play_button.draw(screen): #muda a tela para a do jogo quando o botão "play" é pressionado
                menu = "play"
            if options_button.draw(screen): #muda a tela para a de opções quando o botão "options" é pressionado
                menu = "options"
            if lb_button.draw(screen): #muda a tela para a de ranks quando o botão "leaderboards" é pressionado
                menu = "leaderboard"

        # ========= tela do jogo ===========
        if menu == "play": #tela do jogo em si - faz com que o jogo carregue quando a tela é chamada
            draw_poke(characters)
            draw_static(balls)
        
        # ========= tela de opções ============

        if menu == "options": #tela de opcoes
            #=======textos do menu de opções=======
            screen.blit(volume_text,(160,380)) #carrega o texto da barra de volume
            screen.blit(music_text,(100,480)) #carrega o texto da musica

            #========= botão de retornar =========
            if back_button.draw(screen): #faz com que uma tela retorne ao menu inicial quando o botão "back" é pressionado
                menu = "main"

            # ========= Volume da trilha sonoroa =========
            if volup_button.draw(screen): #Aumenta o volume ao clicar o botão "+"
                if (volume < 1 and volume_texto < 100):
                    volume+=0.1
                    volume_texto+=10
                    volume_text = fonte_menu.render(str(volume_texto), 1, (255,255,255))
                    pygame.mixer.music.set_volume(volume)
                else:  #faz com que o valor de volume não fique acima de 100  
                    volume = 1
                    volume_texto = 100
                    pygame.mixer.music.set_volume(volume)
            if voldown_button.draw(screen): #diminui o volume ao clicar o botão "-"
                if(volume > 0 and volume_texto > 0):
                    volume-=0.1 #diminui o valor de volume setado nas variáveis
                    volume_texto-=10 #altera o texto junto ao volume
                    volume_text = fonte_menu.render(str(volume_texto), 1, (255,255,255)) #carrega o texto que representa o volume
                    pygame.mixer.music.set_volume(volume)
                else: #faz com que o valor de volume não fique abaixo de 0
                    volume=0
                    volume_texto = 0
                    pygame.mixer.music.set_volume(volume)

            #========= Alteração de trilha sonora =========
            if msc_button.draw(screen):  #troca as musicas
                musicas+= 1               
                if(musicas == 2):
                    pygame.mixer.music.load("music/Lavender.ogg") #carrega a musica de acordo com a escolhida
                    pygame.mixer.music.play(-1) #deixa as musicas em loop
                    pygame.mixer.music.set_volume(volume)  #seta o volume das musicas
                    music_text = fonte_menu.render("Lavender", 1, (255,255,255))  #carrega o texto que informa a musica      
                elif(musicas == 3):
                    pygame.mixer.music.load("music/Cerulean.ogg") #carrega a musica de acordo com a escolhida
                    pygame.mixer.music.play(-1) #deixa as musicas em loop
                    pygame.mixer.music.set_volume(volume)   #seta o volume das musicas
                    music_text = fonte_menu.render("Cerulean", 1, (255,255,255)) #carrega o texto que informa a musica
                elif(musicas == 4):
                    pygame.mixer.music.load("music/Pewtter.ogg") #carrega a musica de acordo com a escolhida
                    pygame.mixer.music.play(-1) #deixa as musicas em loop
                    pygame.mixer.music.set_volume(volume)   #seta o volume das musicas
                    music_text = fonte_menu.render("Pewter", 1, (255,255,255)) #carrega o texto que informa a musica
                elif(musicas>4):
                    musicas = 1
                    pygame.mixer.music.load("music/music1.ogg") #carrega a musica de acordo com a escolhida
                    pygame.mixer.music.play(-1) #deixa as musicas em loop
                    pygame.mixer.music.set_volume(volume)   #seta o volume das musicas
                    music_text = fonte_menu.render("Musica 1", 1, (255,255,255))    #carrega o texto que informa a musica

                    # ============================================================
            

        # ======== Ranking ===============    
        if menu == "leaderboard": #tela de ranking
            if back_button.draw(screen):
                menu = "main"

        # ================================

        space.step(1/FPS) #atualiza a gravidade da variavel space
        pygame.display.update()
    pygame.quit()
