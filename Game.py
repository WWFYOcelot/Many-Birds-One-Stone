import random, time, pygame
q = 0

throw = False
playing = False
opening = True
left = False
right = False
dead = True
dead2 = True
dead3 = True
dead4 = True
dead5 = True
end = False

pygame.init()

height = 1000
width = 800

x = 0
y = 0
score = 0

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Many Birds, One Stone')
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)

font = pygame.font.Font ('freesansbold.ttf', 100)
font2 = pygame.font.Font ('freesansbold.ttf', 15)
font3 = pygame.font.Font ('freesansbold.ttf', 50)
font4 = pygame.font.Font ('freesansbold.ttf', 25)

person = pygame.image.load('New Piskel.gif')
personrect = person.get_rect()
personrect.center = (400, 900)
circle = pygame.image.load('circle-xxl.png')
circlerect = circle.get_rect()
circlerect.x = personrect.x + 50
circlerect.y = personrect.y + 100

bird = pygame.image.load('male_humming_bird_png_by_doloresdevelde-d4ktla0.png')
birdrect = bird.get_rect()
birdrect.x = random.randint(50, 750)
birdrect.y = random.randint(50, 500)

bird2 = pygame.image.load('male_humming_bird_png_by_doloresdevelde-d4ktla0.png')
birdrect2 = bird2.get_rect()
birdrect2.x = random.randint(50, 750)
birdrect2.y = random.randint(50, 500)

bird3 = pygame.image.load('male_humming_bird_png_by_doloresdevelde-d4ktla0.png')
birdrect3 = bird3.get_rect()
birdrect3.x = random.randint(50, 750)
birdrect3.y = random.randint(50, 500)

bird4 = pygame.image.load('male_humming_bird_png_by_doloresdevelde-d4ktla0.png')
birdrect4 = bird4.get_rect()
birdrect4.x = random.randint(50, 750)
birdrect4.y = random.randint(50, 500)

bird5 = pygame.image.load('male_humming_bird_png_by_doloresdevelde-d4ktla0.png')
birdrect5 = bird5.get_rect()
birdrect5.x = random.randint(50, 750)
birdrect5.y = random.randint(50, 500)

text2 = font2.render("Press Esc to Close the Game", True, white)
text2rect = text2.get_rect()
text2rect.center = (115, 25)
gameDisplay.blit(text2, text2rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                throw = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                opening = False
                playing = True
                startTime = time.clock()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False

    if circlerect.colliderect (birdrect):
        score += 1
        dead = False
        birdrect.x = random.randint(50, 750)
        birdrect.y = random.randint(50, 500)
    if circlerect.colliderect (birdrect2):
        dead2 = False
        score += 1
        birdrect2.x = random.randint(50, 750)
        birdrect2.y = random.randint(50, 500)
    if circlerect.colliderect (birdrect3):
        score += 1
        dead3 = False
        birdrect3.x = random.randint(50, 750)
        birdrect3.y = random.randint(50, 500)
    if circlerect.colliderect (birdrect4):
        score += 1
        dead4 = False
        birdrect4.x = random.randint(50, 750)
        birdrect4.y = random.randint(50, 500)
    if circlerect.colliderect (birdrect5):
        score += 1
        dead5 = False
        birdrect5.x = random.randint(50, 750)
        birdrect5.y = random.randint(50, 500)

    if opening:
        text = font.render("Many Birds,", True, white)
        textRect = text.get_rect()
        textRect.center = (400, 200)
        gameDisplay.blit(text, textRect)

        text3 = font.render("One Stone", True, white)
        text3rect = text3.get_rect()
        text3rect.center = (400, 325)
        gameDisplay.blit(text3, text3rect)

        text4 = font4.render("Press ENTER to Start", True, white)
        text4rect = text4.get_rect()
        text4rect.center = (400, 600)
        gameDisplay.blit(text4, text4rect)

    if playing:
        q = 1 - (time.clock() - startTime)

        gameDisplay.fill(black)

        gameDisplay.blit(person, personrect)

        if dead:
            gameDisplay.blit(bird, birdrect)
        if dead2:
            gameDisplay.blit(bird2, birdrect2)
        if dead3:
            gameDisplay.blit(bird2, birdrect3)
        if dead4:
            gameDisplay.blit(bird2, birdrect4)
        if dead5:
            gameDisplay.blit(bird2, birdrect5)

        if throw:
            gameDisplay.blit(circle, circlerect)
            circlerect.y -= 10

        if q <= -3:
            playing = False
            end = True

    if right:
        circlerect.x += 15
    if left:
        circlerect.x -= 15

    if circlerect.y > 1000:
        playing = False
        end = True

    if circlerect.x < 0 or circlerect.x > 800:
        playing = False
        end = True

    if end:
        gameDisplay.fill(black)

        text = font.render(str(score), True, white)
        textRect = text.get_rect()
        textRect.center = (400, 375)
        text3 = font3.render("Your Score Was:", True, white)

        text4 = font4.render("Press ENTER to Play Again", True, white)
        text4rect = text4.get_rect()
        text4rect.center = (400, 800)
        text3rect = text3.get_rect()
        text3rect.center = (400, 200)
        gameDisplay.blit(text4, text4rect)
        gameDisplay.blit(text3, text3rect)
        gameDisplay.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end = False
                    playing = True
                    score = 0


    pygame.display.update()
    clock.tick(60)