CZERWONY = (255,0,0)
ZIELONY = (0,255,0)
NIEBIESKI = (0,0,255)
BORDOWY = (125,30,50)
SZARY = (200,200,200)
kolory = [CZERWONY,ZIELONY,NIEBIESKI,BORDOWY]

KIERUNEK_GORA = 0
KIERUNEK_PRAWO = 1
KIERUNEK_DOL = 2
KIERUNEK_LEWO = 3

import pygame
from win32api import GetSystemMetrics

pygame.init()

windowWidth = int(GetSystemMetrics(0) * 0.8)
windowHeight = int(GetSystemMetrics(1) * 0.8)

screenSize = (windowWidth,windowHeight)
screenCenter = (screenSize[0]//2,screenSize[1]//2)
display = pygame.display.set_mode(screenSize)
display_rect = display.get_rect()
pygame.display.set_caption('PyGame Snake')
pyClock = pygame.time.Clock()

koniecPracy = False

kierunekRuchu = KIERUNEK_PRAWO
predkoscGracza = 3

#Tworzenie sprite'a
playerSprite = pygame.sprite.Sprite()
#Sprite image
playerSprite.image = pygame.Surface((30, 30))
playerSprite.image.fill(NIEBIESKI)
#Sprite rect
playerSprite.rect = playerSprite.image.get_rect()
playerSprite.rect.center = screenCenter


#Grupa sprite'ów
grupaSprite = pygame.sprite.Group()
grupaSprite.add(playerSprite)


while not koniecPracy:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniecPracy = True


    if playerSprite.rect.bottom > screenSize[1]:
        predkoscGracza = 0
        playerSprite.rect.bottom = screenSize[1]

    if playerSprite.rect.right > screenSize[0]:
        predkoscGracza = 0
        playerSprite.rect.right = screenSize[0]

    if playerSprite.rect.top < 0:
        predkoscGracza = 0
        playerSprite.rect.top = 0

    if playerSprite.rect.left < 0:
        predkoscGracza = 0
        playerSprite.rect.left = 0



    nacisnieteKlawisze = pygame.key.get_pressed()

    #Nacisniety klawisz D i kierunekRuchu jest inny niz KIERUNEK_LEWO
    if nacisnieteKlawisze[pygame.K_d] and kierunekRuchu != KIERUNEK_LEWO:
        kierunekRuchu = KIERUNEK_PRAWO
    if nacisnieteKlawisze[pygame.K_a] and  kierunekRuchu != KIERUNEK_PRAWO:
        kierunekRuchu = KIERUNEK_LEWO
    if nacisnieteKlawisze[pygame.K_w] :
        kierunekRuchu = KIERUNEK_GORA
    if nacisnieteKlawisze[pygame.K_s] :
        kierunekRuchu = KIERUNEK_DOL


    #Ruch gracza
    if kierunekRuchu == KIERUNEK_PRAWO:
        playerSprite.rect.left += predkoscGracza
    elif kierunekRuchu == KIERUNEK_LEWO:
        playerSprite.rect.left -= predkoscGracza
    elif kierunekRuchu == KIERUNEK_GORA:
        playerSprite.rect.top -= predkoscGracza
    elif kierunekRuchu == KIERUNEK_DOL:
        playerSprite.rect.top += predkoscGracza


    #Rysowanie
    display.fill(SZARY)

    grupaSprite.update()
    grupaSprite.draw(display)

    pygame.display.flip()
    pyClock.tick(30)

pygame.quit()
