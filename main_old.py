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
kwadracik = pygame.Rect(10,10,50,50)
ruchomyKwadracik = pygame.Rect(0,0,20,20)
ruchomyKwadracik.center = screenCenter
numerKoloruKwadratu = 0

predkoscX = 1
predkoscY = 2

kierunekRuchu = KIERUNEK_PRAWO
predkoscGracza = 3

#Tworzenie sprite'a
pierwszySprite = pygame.sprite.Sprite()
#Sprite image
# monsterImage = pygame.image.load('images/monster.png').convert_alpha()
# monsterImage = pygame.transform.scale(monsterImage,(100,100))
# pierwszySprite.image = monsterImage
pierwszySprite.image = pygame.Surface((30,30))
pierwszySprite.image.fill(NIEBIESKI)
#Sprite rect
pierwszySprite.rect = pierwszySprite.image.get_rect()
pierwszySprite.rect.center = screenCenter


#Grupa sprite'ów
grupaSprite = pygame.sprite.Group()
grupaSprite.add(pierwszySprite)


while not koniecPracy:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniecPracy = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousePosition = pygame.mouse.get_pos()
            ifCollide = kwadracik.collidepoint(mousePosition)
            if ifCollide:
                if numerKoloruKwadratu < len(kolory)-1:
                    numerKoloruKwadratu += 1
                else:
                    numerKoloruKwadratu = 0


    ruchomyKwadracik.left += predkoscX
    ruchomyKwadracik.top += predkoscY

    if ruchomyKwadracik.bottom > screenSize[1]:
        predkoscY = predkoscY*-1
        ruchomyKwadracik.bottom = screenSize[1]

    if ruchomyKwadracik.right > screenSize[0]:
        predkoscX *= -1
        ruchomyKwadracik.right = screenSize[0]

    if ruchomyKwadracik.top < 0:
        predkoscY *= -1
        ruchomyKwadracik.top = 0

    if ruchomyKwadracik.left < 0:
        predkoscX *= -1
        ruchomyKwadracik.left = 0



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
        pierwszySprite.rect.left += predkoscGracza
    elif kierunekRuchu == KIERUNEK_LEWO:
        pierwszySprite.rect.left -= predkoscGracza
    elif kierunekRuchu == KIERUNEK_GORA:
        pierwszySprite.rect.top -= predkoscGracza
    elif kierunekRuchu == KIERUNEK_DOL:
        pierwszySprite.rect.top += predkoscGracza


    #Rysowanie
    display.fill(SZARY)
    pygame.draw.rect(display, ZIELONY, ruchomyKwadracik)
    pygame.draw.rect(display,kolory[numerKoloruKwadratu],kwadracik)

    grupaSprite.update()
    grupaSprite.draw(display)

    pygame.display.flip()
    pyClock.tick(30)

pygame.quit()
