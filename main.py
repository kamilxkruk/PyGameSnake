CZERWONY = (255,0,0)
ZIELONY = (0,255,0)
NIEBIESKI = (0,0,255)
BORDOWY = (125,30,50)
SZARY = (200,200,200)
BIALY = (255,255,255)
kolory = [CZERWONY,ZIELONY,NIEBIESKI,BORDOWY]

KIERUNEK_GORA = 0
KIERUNEK_PRAWO = 1
KIERUNEK_DOL = 2
KIERUNEK_LEWO = 3

ROZMIAR_GRACZA = 30

PLAYER_SPEED = ROZMIAR_GRACZA

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

liczbaWierszy = windowHeight // ROZMIAR_GRACZA
liczbaKolumn = windowWidth // ROZMIAR_GRACZA

koniecPracy = False

kierunekRuchu = KIERUNEK_PRAWO
currentPlayerSpeed = PLAYER_SPEED

endGameFont = pygame.font.SysFont(None,150,bold=True)
endGameLabel = endGameFont.render('KONIEC GRY',1,CZERWONY)
showEndGameLabel = False


#Tworzenie sprite'a
playerSprite = pygame.sprite.Sprite()
#Sprite image
playerSprite.image = pygame.Surface((ROZMIAR_GRACZA, ROZMIAR_GRACZA))
playerSprite.image.fill(NIEBIESKI)
#Sprite rect
playerSprite.rect = playerSprite.image.get_rect()
playerSprite.rect.center = screenCenter

#Grupa sprite'ów
grupaSprite = pygame.sprite.Group()
grupaSprite.add(playerSprite)

numerIteracji = 0

while not koniecPracy:
    numerIteracji = (numerIteracji+1)%8
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniecPracy = True
        elif event.type == pygame.MOUSEBUTTONUP:
            showEndGameLabel = False
            playerSprite.rect.center = screenCenter
            currentPlayerSpeed = PLAYER_SPEED
            kierunekRuchu = KIERUNEK_PRAWO

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
    if nacisnieteKlawisze[pygame.K_a] and  kierunekRuchu != KIERUNEK_PRAWO:
        kierunekRuchu = KIERUNEK_LEWO
    if nacisnieteKlawisze[pygame.K_w] and kierunekRuchu != KIERUNEK_DOL:
        kierunekRuchu = KIERUNEK_GORA
    if nacisnieteKlawisze[pygame.K_s] and kierunekRuchu != KIERUNEK_GORA:
        kierunekRuchu = KIERUNEK_DOL


    #Ruch gracza
    if numerIteracji == 0:
        if kierunekRuchu == KIERUNEK_PRAWO:
            playerSprite.rect.left += currentPlayerSpeed
        elif kierunekRuchu == KIERUNEK_LEWO:
            playerSprite.rect.left -= currentPlayerSpeed
        elif kierunekRuchu == KIERUNEK_GORA:
            playerSprite.rect.top -= currentPlayerSpeed
        elif kierunekRuchu == KIERUNEK_DOL:
            playerSprite.rect.top += currentPlayerSpeed


    #Rysowanie
    display.fill(SZARY)

    for wiersz in range(liczbaWierszy):
        pygame.draw.line(display,BIALY,(0,ROZMIAR_GRACZA*wiersz),(windowWidth,ROZMIAR_GRACZA*wiersz))


    grupaSprite.update()
    grupaSprite.draw(display)

    if showEndGameLabel:
        endGameLabelRect = endGameLabel.get_rect()
        display.blit(endGameLabel,(screenCenter[0]-endGameLabelRect.width//2,screenCenter[1]-endGameLabelRect.height//2))

    pygame.display.flip()
    pyClock.tick(30)

pygame.quit()
