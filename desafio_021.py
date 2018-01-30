#import pygame # não esta executando desta forma
#pygame.init()
#pygame.mixer.music.load('desafio021.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

# codigo funcionando
#from pygame import mixer # importa o mixer do pygame
#mixer.init()  # inicia o mixer do pygame
#mixer.music.load('musica.mp3') #carrega musica
#mixer.music.play() # toca musica
#input('Agora você escuta?')

from os import startfile # executa a musica no player padrão
startfile('musica.mp3')
