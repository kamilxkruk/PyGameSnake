# import pygame
# from win32api import GetSystemMetrics
# from ustawienia import *
# from Model.PunktSprite import PunktSprite
# from random import randint
# import time
#
# pygame.init()
#
# windowWidth = int(GetSystemMetrics(0) * 0.8)
# windowHeight = int(GetSystemMetrics(1) * 0.8)
#
# liczbaWierszy = windowHeight // ROZMIAR_GRACZA
# liczbaKolumn = windowWidth // ROZMIAR_GRACZA
#
# screenSize = (liczbaKolumn*ROZMIAR_GRACZA,liczbaWierszy*ROZMIAR_GRACZA)
# screenCenter = (screenSize[0]//2,screenSize[1]//2)
# display = pygame.display.set_mode(screenSize)
# display_rect = display.get_rect()
# pygame.display.set_caption('PyGame Snake')
# pyClock = pygame.time.Clock()
#
#
#
# koniecPracy = False
#
# kierunekRuchu = KIERUNEK_PRAWO
# currentPlayerSpeed = PLAYER_SPEED
#
# endGameFont = pygame.font.SysFont(None,150,bold=True)
# endGameLabel = endGameFont.render('KONIEC GRY',1,CZERWONY)
# showEndGameLabel = False
#
# punktacja = 0
# punktacjaFont = pygame.font.SysFont(None,30,bold=True)
# punktacjaLabel = punktacjaFont.render('Punkty: 0',1,CZARNY)
#
#
# #Tworzenie sprite'a
# playerSprite = pygame.sprite.Sprite()
# #Sprite image
# playerSprite.image = pygame.Surface((ROZMIAR_GRACZA, ROZMIAR_GRACZA))
# playerSprite.image.fill(NIEBIESKI)
# #Sprite rect
# playerSprite.rect = playerSprite.image.get_rect()
# playerSprite.rect.topleft = (liczbaKolumn//2*ROZMIAR_GRACZA,liczbaWierszy//2*ROZMIAR_GRACZA)
#
# #Grupa sprite'ów
# grupaGraczaSprite = pygame.sprite.Group()
# grupaGraczaSprite.add(playerSprite)
#
# bodySegmentList = []
#
# grupaPunktSprite = pygame.sprite.Group()
# grupaPunktSprite.add(PunktSprite(5,3),PunktSprite(8,5))
#
#
# numerIteracji = 0
# czasOstatnioWygenerowanegoPunktu = time.time()
#
# while not koniecPracy:
#     numerIteracji = (numerIteracji+1)%8
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             koniecPracy = True
#         elif event.type == pygame.MOUSEBUTTONUP:
#             showEndGameLabel = False
#             playerSprite.rect.topleft = (liczbaKolumn//2*ROZMIAR_GRACZA,liczbaWierszy//2*ROZMIAR_GRACZA)
#             currentPlayerSpeed = PLAYER_SPEED
#             kierunekRuchu = KIERUNEK_PRAWO
#
#     if playerSprite.rect.bottom > screenSize[1]:
#         currentPlayerSpeed = 0
#         playerSprite.rect.bottom = screenSize[1]
#         showEndGameLabel = True
#
#     if playerSprite.rect.right > screenSize[0]:
#         currentPlayerSpeed = 0
#         playerSprite.rect.right = screenSize[0]
#         showEndGameLabel = True
#
#     if playerSprite.rect.top < 0:
#         currentPlayerSpeed = 0
#         playerSprite.rect.top = 0
#         showEndGameLabel = True
#
#     if playerSprite.rect.left < 0:
#         currentPlayerSpeed = 0
#         playerSprite.rect.left = 0
#         showEndGameLabel = True
#
#     nacisnieteKlawisze = pygame.key.get_pressed()
#
#     if nacisnieteKlawisze[pygame.K_d] and kierunekRuchu != KIERUNEK_LEWO:
#         kierunekRuchu = KIERUNEK_PRAWO
#     if nacisnieteKlawisze[pygame.K_a] and  kierunekRuchu != KIERUNEK_PRAWO:
#         kierunekRuchu = KIERUNEK_LEWO
#     if nacisnieteKlawisze[pygame.K_w] and kierunekRuchu != KIERUNEK_DOL:
#         kierunekRuchu = KIERUNEK_GORA
#     if nacisnieteKlawisze[pygame.K_s] and kierunekRuchu != KIERUNEK_GORA:
#         kierunekRuchu = KIERUNEK_DOL
#
#     obecnyCzas = time.time()
#
#     #Generowanie punktów
#     if obecnyCzas - czasOstatnioWygenerowanegoPunktu > 5:
#         randomX = randint(1,liczbaKolumn)
#         randomY = randint(1, liczbaWierszy)
#
#         losowyPunkt = PunktSprite(randomX,randomY)
#         grupaPunktSprite.add(losowyPunkt)
#         czasOstatnioWygenerowanegoPunktu = obecnyCzas
#
#     #Usuwanie punktów
#
#     czasWyswietlaniaPunktu = 6
#     for punkt in grupaPunktSprite:
#         if obecnyCzas - punkt.czasUtworzenia > czasWyswietlaniaPunktu:
#             grupaPunktSprite.remove(punkt)
#
#     #Ruch gracza
#     if numerIteracji == 0:
#         headBeforeMove = playerSprite.rect.copy()
#
#         if kierunekRuchu == KIERUNEK_PRAWO:
#             playerSprite.rect.left += currentPlayerSpeed
#         elif kierunekRuchu == KIERUNEK_LEWO:
#             playerSprite.rect.left -= currentPlayerSpeed
#         elif kierunekRuchu == KIERUNEK_GORA:
#             playerSprite.rect.top -= currentPlayerSpeed
#         elif kierunekRuchu == KIERUNEK_DOL:
#             playerSprite.rect.top += currentPlayerSpeed
#
#         czyZdobytoPunkt = pygame.sprite.spritecollide(playerSprite,grupaPunktSprite,True)
#         if czyZdobytoPunkt:
#             punktacja += 1
#             punktacjaLabel = punktacjaFont.render('Punkty: '+ str(punktacja), 1, CZARNY)
#             if not len(bodySegmentList):
#                 bodySegmentList.append(headBeforeMove.copy())
#
#
#
#     #Rysowanie
#     display.fill(SZARY)
#
#     for wiersz in range(liczbaWierszy+1):
#         pygame.draw.line(display,BIALY,(0,ROZMIAR_GRACZA*wiersz),(windowWidth,ROZMIAR_GRACZA*wiersz))
#     for kolumna in range(liczbaKolumn+1):
#         pygame.draw.line(display,BIALY,(ROZMIAR_GRACZA*kolumna,0),(ROZMIAR_GRACZA*kolumna,windowHeight))
#
#     grupaGraczaSprite.update()
#     grupaGraczaSprite.draw(display)
#
#     for bodySegment in bodySegmentList:
#         pygame.draw.rect(display,NIEBIESKI,bodySegment)
#
#     grupaPunktSprite.update()
#     grupaPunktSprite.draw(display)
#
#     if showEndGameLabel:
#         endGameLabelRect = endGameLabel.get_rect()
#         display.blit(endGameLabel,(screenCenter[0]-endGameLabelRect.width//2,screenCenter[1]-endGameLabelRect.height//2))
#
#     # punktacjaLabel = punktacjaFont.render('Punkty: '+str(punktacja),1,CZARNY)
#     display.blit(punktacjaLabel,(10,10))
#
#     pygame.display.flip()
#     pyClock.tick(30)
#
# pygame.quit()

import pygame
from win32api import GetSystemMetrics
from ustawienia import *
from Model.PunktSprite import PunktSprite
from random import randint
import time

pygame.init()

windowWidth = int(GetSystemMetrics(0) * 0.8)
windowHeight = int(GetSystemMetrics(1) * 0.8)

liczbaWierszy = windowHeight // ROZMIAR_GRACZA
liczbaKolumn = windowWidth // ROZMIAR_GRACZA

screenSize = (liczbaKolumn*ROZMIAR_GRACZA,liczbaWierszy*ROZMIAR_GRACZA)
screenCenter = (screenSize[0]//2,screenSize[1]//2)
display = pygame.display.set_mode(screenSize)
display_rect = display.get_rect()
pygame.display.set_caption('PyGame Snake')
pyClock = pygame.time.Clock()

#Ladowanie dźwięków
# odtwarzaczMuzy = pygame.mixer.init()
# mojDzwiek = pygame.mixer.music.load('sounds/dzwiek.mp3')
# pygame.mixer.music.play()


koniecPracy = False

kierunekRuchu = KIERUNEK_PRAWO
currentPlayerSpeed = PLAYER_SPEED

endGameFont = pygame.font.SysFont(None,150,bold=True)
endGameLabel = endGameFont.render('KONIEC GRY',1,CZERWONY)
showEndGameLabel = False

punktacja = 0
punktacjaFont = pygame.font.SysFont(None,30,bold=True)
punktacjaLabel = punktacjaFont.render('Punkty: 0',1,CZARNY)


#Tworzenie sprite'a
playerSprite = pygame.sprite.Sprite()
#Sprite image
# snakeHeadImageRight = pygame.image.load('images/oldman_head.png')
# snakeHeadImageRight = pygame.transform.scale(snakeHeadImageRight,(50,50))

snakeHeadImageRight = pygame.image.load('images/snake_head.png')

snakeBodyImageRight = pygame.image.load('images/oldman_body.png')
snakeBodyImageRight = pygame.transform.scale(snakeBodyImageRight,(50,50))

snakeTailImageRight = pygame.image.load('images/oldman_legs.png')
snakeTailImageRight = pygame.transform.scale(snakeTailImageRight,(50,50))

snakeHeadImages = {
    "RIGHT": snakeHeadImageRight,
    "DOWN": pygame.transform.rotate(snakeHeadImageRight,-90),
    "LEFT": pygame.transform.rotate(snakeHeadImageRight,-180),
    "UP": pygame.transform.rotate(snakeHeadImageRight,90)
}

playerSprite.image = snakeHeadImages["RIGHT"]
playerSprite.image = pygame.transform.scale(playerSprite.image,(50,50))

# playerSprite.image = pygame.Surface((ROZMIAR_GRACZA, ROZMIAR_GRACZA))
# playerSprite.image.fill(ZIELONY)

#Sprite rect
playerSprite.rect = playerSprite.image.get_rect()
playerSprite.rect.topleft = (liczbaKolumn//2*ROZMIAR_GRACZA,liczbaWierszy//2*ROZMIAR_GRACZA)

#Grupa sprite'ów
grupaSprite = pygame.sprite.Group()
grupaSprite.add(playerSprite)

#Grupa sprite'ów
grupaGraczaSprite = pygame.sprite.Group()
grupaGraczaSprite.add(playerSprite)

bodySegmentList = []

grupaPunktSprite = pygame.sprite.Group()

grupaPunktSprite = pygame.sprite.Group()

grupaPunktSprite.add(PunktSprite(5,3),PunktSprite(8,5))


numerIteracji = 0
czasOstatnioWygenerowanegoPunktu = time.time()

while not koniecPracy:
    numerIteracji = (numerIteracji+1)%6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniecPracy = True
        elif event.type == pygame.MOUSEBUTTONUP:
            showEndGameLabel = False
            playerSprite.rect.topleft = (liczbaKolumn//2*ROZMIAR_GRACZA,liczbaWierszy//2*ROZMIAR_GRACZA)
            currentPlayerSpeed = PLAYER_SPEED
            kierunekRuchu = KIERUNEK_PRAWO
            playerSprite.image = snakeHeadImages["RIGHT"]
            punktacja = 0
            punktacjaLabel = punktacjaFont.render('Punkty: ' + str(punktacja), 1, CZARNY)
            bodySegmentList.clear()

    if playerSprite.rect.bottom > screenSize[1]:
        currentPlayerSpeed = 0
        playerSprite.rect.bottom = screenSize[1]
        showEndGameLabel = True

    if playerSprite.rect.right > screenSize[0]:
        currentPlayerSpeed = 0
        playerSprite.rect.right = screenSize[0]
        showEndGameLabel = True

    if playerSprite.rect.top < 0:
        currentPlayerSpeed = 0
        playerSprite.rect.top = 0
        showEndGameLabel = True

    if playerSprite.rect.left < 0:
        currentPlayerSpeed = 0
        playerSprite.rect.left = 0
        showEndGameLabel = True

    nacisnieteKlawisze = pygame.key.get_pressed()

    if nacisnieteKlawisze[pygame.K_d] and kierunekRuchu != KIERUNEK_LEWO:
        kierunekRuchu = KIERUNEK_PRAWO
        playerSprite.image = snakeHeadImages["RIGHT"]
    if nacisnieteKlawisze[pygame.K_a] and  kierunekRuchu != KIERUNEK_PRAWO:
        kierunekRuchu = KIERUNEK_LEWO
        playerSprite.image = snakeHeadImages["LEFT"]
    if nacisnieteKlawisze[pygame.K_w] and kierunekRuchu != KIERUNEK_DOL:
        kierunekRuchu = KIERUNEK_GORA
        playerSprite.image = snakeHeadImages["UP"]
    if nacisnieteKlawisze[pygame.K_s] and kierunekRuchu != KIERUNEK_GORA:
        kierunekRuchu = KIERUNEK_DOL
        playerSprite.image = snakeHeadImages["DOWN"]


    obecnyCzas = time.time()

    if not showEndGameLabel:
        #Generowanie punktów
        if obecnyCzas - czasOstatnioWygenerowanegoPunktu > 5:
            randomX = randint(1,liczbaKolumn)
            randomY = randint(1, liczbaWierszy)

            losowyPunkt = PunktSprite(randomX,randomY)
            grupaPunktSprite.add(losowyPunkt)
            czasOstatnioWygenerowanegoPunktu = obecnyCzas

        #Usuwanie punktów
        for punkt in grupaPunktSprite:
            if obecnyCzas - punkt.czasUtworzenia > 6:
                grupaPunktSprite.remove(punkt)

        # Ruch gracza
        if numerIteracji == 0:
            headBeforeMove = playerSprite.rect.copy()

            if kierunekRuchu == KIERUNEK_PRAWO:
                playerSprite.rect.left += currentPlayerSpeed
            elif kierunekRuchu == KIERUNEK_LEWO:
                playerSprite.rect.left -= currentPlayerSpeed
            elif kierunekRuchu == KIERUNEK_GORA:
                playerSprite.rect.top -= currentPlayerSpeed
            elif kierunekRuchu == KIERUNEK_DOL:
                playerSprite.rect.top += currentPlayerSpeed

            for bodySegmentIndex in range(len(bodySegmentList)-1, -1, -1):

                if bodySegmentIndex == 0:
                    bodySegmentList[bodySegmentIndex].topleft = headBeforeMove.topleft
                else:
                    bodySegmentList[bodySegmentIndex].topleft = bodySegmentList[bodySegmentIndex-1].topleft

            czyZdobytoPunkt = pygame.sprite.spritecollide(playerSprite, grupaPunktSprite, True)
            if czyZdobytoPunkt:
                punktacja += 1
                punktacjaLabel = punktacjaFont.render('Punkty: ' + str(punktacja), 1, CZARNY)
                if not len(bodySegmentList):
                    bodySegmentList.append(headBeforeMove.copy())
                else:
                    bodySegmentList.append(bodySegmentList[-1].copy())

            # Rysowanie
            display.fill(SZARY)

            for wiersz in range(liczbaWierszy + 1):
                pygame.draw.line(display, BIALY, (0, ROZMIAR_GRACZA * wiersz), (windowWidth, ROZMIAR_GRACZA * wiersz))
            for kolumna in range(liczbaKolumn + 1):
                pygame.draw.line(display, BIALY, (ROZMIAR_GRACZA * kolumna, 0), (ROZMIAR_GRACZA * kolumna, windowHeight))

            grupaGraczaSprite.update()
            grupaGraczaSprite.draw(display)

            for id,bodySegment in enumerate(bodySegmentList):
                losowaLiczbaKoloru = randint(0,len(KOLORY)-1)
                pygame.draw.rect(display, KOLORY[losowaLiczbaKoloru], bodySegment)

                # if id == len(bodySegmentList)-1:
                #     display.blit(snakeTailImageRight,bodySegment)
                # else:
                #     display.blit(snakeBodyImageRight,bodySegment)



            grupaPunktSprite.update()
            grupaPunktSprite.draw(display)

    grupaSprite.update()
    grupaSprite.draw(display)

    grupaPunktSprite.update()
    grupaPunktSprite.draw(display)

    if showEndGameLabel:
        endGameLabelRect = endGameLabel.get_rect()
        display.blit(endGameLabel,(screenCenter[0]-endGameLabelRect.width//2,screenCenter[1]-endGameLabelRect.height//2))

    # punktacjaLabel = punktacjaFont.render('Punkty: '+str(punktacja),1,CZARNY)
    display.blit(punktacjaLabel,(10,10))

    pygame.display.flip()
    pyClock.tick(30)

pygame.quit()
