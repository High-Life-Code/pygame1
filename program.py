import random
import pygame
import sys
import random
import os

FPS = 50

if __name__ == '__main__':
    def terminate():
        pygame.quit()
        sys.exit()


    def start_screen():
        intro_text = ["",
                      "",
                      "",
                      "",
                      "                                                   SURVIVOR", "",
                      "The goal is to stay alive as long as possible!",
                      "If fabric or solar panels are broken,",
                      "Take tools from warehouse and stay on broken stuff until the recovery",
                      "Avoid meteorites and take oxygen from home if your skin with red spot",
                      "You can watch your results in the file 'your score' "]

        fon = pygame.transform.scale(pygame.image.load('fon.jpeg'), (1200, 800))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 50)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()
            clock.tick(FPS)


    m = 1200
    prem = 2400
    d = 0
    pred = 1600
    n = 800
    pren = 1600
    e = 400
    pree = 800
    c = 0

    tools = False
    tools1 = False
    tools2 = False
    aval = True
    sourcing = True
    home_oxygen = 0
    oxygen = 450
    water = 0
    own_water = 10000
    energy = 0
    metan = 0
    carbon = 0
    hydrogen = 0
    on_solar = 0
    on_fabric = 0

    score_file = open('your score', mode='a', encoding='utf-8')
    read_file = open('your score', mode='r', encoding='utf-8')

    '''class Player(pygame.sprite.Sprite):
        image = pygame.image.load("image.png")

        def __init__(self, *group):
            super().__init__(*group)
            self.image = Player.image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        '''


    class Meteorite(pygame.sprite.Sprite):
        image = pygame.image.load("meteoritee2.png")
        image2 = pygame.image.load("ghost2.png")
        image.set_colorkey(image.get_at((0, 0)))

        def __init__(self, *group):
            super().__init__(*group)
            self.image = Meteorite.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(300, 1000)
            self.rect.y = 0

        def update(self):
            if pygame.sprite.spritecollideany(self, all_sprites):
                self.kill()
            else:
                self.rect = self.rect.move(random.randrange(3) - 5,
                                           random.randrange(3) + 5)


    def sandstorm():
        for dust in range(100000):
            screen.fill(pygame.Color('brown'),
                        (random.random() * width,
                         random.random() * height, 1, 1))


    def load_image(name, colorkey=None):
        img = pygame.image.load(name)
        if colorkey is not None:
            img = img.convert()
            if colorkey == -1:
                colorkey = img.get_at((0, 0))
            elif colorkey == -2:
                colorkey = img.get_at((0, 0))
            img.set_colorkey(colorkey)
        else:
            img = img.convert_alpha()
        return img


    FPS = 60
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    pygame.display.flip()
    picture = pygame.image.load("2133x1200_1530549_[www.ArtFile.ru].jpg")
    morning = pygame.image.load("morening.jpg")
    night = pygame.image.load("night.jpg")

    all_sprites = pygame.sprite.Group()
    meteorite = pygame.sprite.Group()
    players = pygame.sprite.Group()

    player = pygame.sprite.Sprite()
    player.image = load_image("image.png")
    player.rect = player.image.get_rect()
    player.rect.x = 835
    player.rect.y = 648
    solar = pygame.sprite.Sprite()
    solar.image = load_image("solarroof.jpg")
    solar.rect = solar.image.get_rect()
    solar.rect.x = 340
    solar.rect.y = 360
    rocket = pygame.sprite.Sprite()
    rocket.image = load_image("rocket.jpg", -1)
    rocket.rect = rocket.image.get_rect()
    rocket.rect.x = 70
    rocket.rect.y = 350
    fabric = pygame.sprite.Sprite()
    fabric.image = load_image('fabric.jpg', -1)
    fabric.rect = fabric.image.get_rect()
    fabric.rect.x = 900
    fabric.rect.y = 325
    home = pygame.sprite.Sprite()
    home.image = load_image('home.png', -1)
    home.rect = home.image.get_rect()
    home.rect.x = 850
    home.rect.y = 580
    reservator = pygame.sprite.Sprite()
    reservator.image = load_image("reserv.jpg", -1)
    reservator.rect = reservator.image.get_rect()
    reservator.rect.x = 280
    reservator.rect.y = 640
    warehouse = pygame.sprite.Sprite()
    warehouse.image = load_image("warehouse.jpg", -1)
    warehouse.rect = warehouse.image.get_rect()
    warehouse.rect.x = 10
    warehouse.rect.y = 640

    all_sprites.add(reservator)
    all_sprites.add(warehouse)
    all_sprites.add(home)
    all_sprites.add(fabric)
    all_sprites.add(rocket)
    all_sprites.add(solar)
    players.add(player)

    delta = 'day'
    speed = 5
    x = 835
    y = 648
    x_1_rect = 1200
    x_2_rect = 800
    rect = pygame.Rect(0, 0, x_1_rect, x_2_rect)
    # главный цикл
    run = True
    start = True
    while run:
        if start:
            start_screen()
            start = False

        clock.tick(FPS)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        water += 6
        hydrogen += 4
        home_oxygen += 4
        oxygen -= 1
        own_water -= 6
        carbon += 1
        if aval and sourcing:
            metan += 1
            hydrogen -= 4
            carbon -= 1
        else:
            carbon -= 1
            hydrogen -= 4
            home_oxygen -= 4
            water -= 6
        if oxygen > 200 and own_water > 1000:
            player.image = load_image('image.png')
        elif oxygen <= 200 or own_water <= 1000:
            player.image = load_image("image2.png")
        if oxygen == 0 or own_water == 0:
            run = False

        c += 1
        d += 1
        m += 1
        e += 1
        n += 1
        if c > 1600:
            if d - 1600 == pred:
                screen.blit(picture, (0, 0))
                delta = 'day'
                pred = d
            elif m - 1600 == prem:
                screen.blit(morning, (0, 0))
                delta = 'more'
                prem = m
            elif e - 1600 == pree:
                screen.blit(morning, (0, 0))
                delta = 'more'
                pree = e
            elif n - 1600 == pren:
                screen.blit(night, (0, 0))
                delta = 'night'
                pren = n
        else:
            screen.blit(picture, (0, 0))
            delta = 'day'
        if delta == 'day':
            screen.blit(picture, (0, 0))
        elif delta == 'more':
            screen.blit(morning, (0, 0))
        else:
            screen.blit(night, (0, 0))

        all_sprites.draw(screen)
        meteorite.draw(screen)

        if c % 1000 == 0:
            for i in range(5):
                Meteorite(meteorite)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        if x >= 1100:
            const = x - 1100
            x = x - const
        if y >= 700:
            const = y - 700
            y = y - const
        if x <= 0:
            const = 0 - x
            x = x + const
        if y <= 300:
            const = 300 - y
            y = y + const
        if (y >= 425) and (y <= 525) and (x >= 700) and x <= 850:
            if keys[pygame.K_LEFT]:
                x = 850
            if keys[pygame.K_RIGHT]:
                const = x - 700
                x = x - const
            if keys[pygame.K_UP]:
                const = 525 - y
                y = y + const
            if keys[pygame.K_DOWN]:
                const = y - 425
                y = y - const
        player.rect.x = x
        player.rect.y = y
        if player.rect.colliderect(reservator.rect):
            if water - (10000 - own_water) >= 0:
                water -= (10000 - own_water)
                own_water = 10000
            else:
                own_water += water
                water = 0
        if player.rect.colliderect(warehouse.rect):
            tools1 = True
            tools2 = True
        if player.rect.colliderect(solar.rect):
            if tools1:
                on_solar += 1
        if player.rect.colliderect(fabric.rect):
            if tools2:
                on_fabric += 1
        if player.rect.colliderect(home.rect):
            if sourcing and home_oxygen - (450 - oxygen) >= 0:
                home_oxygen -= (450 - oxygen)
                oxygen = 450
            elif sourcing:
                oxygen += home_oxygen
                home_oxygen = 0
        if pygame.sprite.spritecollideany(player, meteorite):
            run = False
        if pygame.sprite.spritecollideany(solar, meteorite):
            solar.image = load_image("solarroofcrash.jpg")
            sourcing = False
            on_solar = 0
        if pygame.sprite.spritecollideany(fabric, meteorite):
            fabric.image = load_image("fabriccrash.jpg", -1)
            aval = False
            on_fabric = 0
        if on_fabric >= 100:
            fabric.image = load_image("fabric.jpg", -1)
            aval = True
            tools2 = False
        if on_solar >= 100:
            solar.image = load_image("solarroof.jpg")
            sourcing = True
            tools1 = False

        all_sprites.update()
        meteorite.update()
        players.draw(screen)
        players.update()

        clock.tick(FPS)
        pygame.display.flip()
    score_file.write(str(c) + '\n')
    score_file.close()
    pygame.quit()
