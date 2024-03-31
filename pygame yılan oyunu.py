import pygame
import random

# PENCERE
pygame.init()
genislik = 800
yukseklik = 600
pencere = pygame.display.set_mode((genislik,yukseklik))
pygame.display.set_caption("Yılan Oyunu :)")
saat = pygame.time.Clock()

# RENKLER 
beyaz = (255,255,255)
siyah = (0,0,0)

# YILAN 
yilan_boyu = 20
yilan_hiz = 10
yilan_x = genislik / 2
yilan_y = yukseklik / 2
yilan_x_hiz = 0
yilan_y_hiz = 0
yilan_liste = []
yilan_uzunluk = 1

# YEM 
yem_x = random.randrange(0, genislik-yilan_boyu, yilan_boyu)
yem_y = random.randrange(0, yukseklik-yilan_boyu, yilan_boyu)

# SKOR 
skor = 0
font = pygame.font.Font(None, 50)

# ANA OYUN DÖNGÜSÜ
oyun = True
while oyun:
    pencere.fill(siyah)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                yilan_x_hiz -= yilan_boyu
                yilan_y_hiz = 0
            if event.key == pygame.K_RIGHT:
                yilan_x_hiz += yilan_boyu
                yilan_y_hiz = 0
            if event.key == pygame.K_UP:
                yilan_x_hiz = 0
                yilan_y_hiz -= yilan_boyu
            if event.key == pygame.K_DOWN:
                yilan_x_hiz = 0
                yilan_y_hiz += yilan_boyu
                
    # YILAN HAREKET
    yilan_x += yilan_x_hiz
    yilan_y += yilan_y_hiz

    if yilan_x >= genislik or yilan_x <= 0 or yilan_y >= yukseklik or yilan_y <= 0:
        oyun = False

    yilan_liste.append((yilan_x, yilan_y))

    if len(yilan_liste) > yilan_uzunluk:
        del yilan_liste[0]

    # ETKİLEŞİMLER
    if yilan_x == yem_x and yilan_y == yem_y:
        skor += 1
        yem_x = random.randrange(0, genislik-yilan_boyu, yilan_boyu)
        yem_y = random.randrange(0, yukseklik-yilan_boyu, yilan_boyu)
        yilan_uzunluk += 1

    skor_yazisi = font.render("Skor: {}".format(skor), True, beyaz)

    pygame.draw.rect(pencere, beyaz, [yem_x, yem_y, yilan_boyu, yilan_boyu])
    for i in yilan_liste:
        pygame.draw.rect(pencere, beyaz, [i[0], i[1], yilan_boyu, yilan_boyu])
    pencere.blit(skor_yazisi, (25,25))

    pygame.display.update()
    saat.tick(yilan_hiz)
pygame.quit()