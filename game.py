import pygame
pygame.init()


screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Simple Game")

image = pygame.image.load('ex game.png')


sound = pygame.mixer.Sound('ex song.wav')
sound.play()


x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    x += 5
    if x > 1000:
        x = 0

    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    screen.blit(image, (100, 100))
    pygame.display.flip()


pygame.quit()