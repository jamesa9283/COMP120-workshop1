import pygame

pygame.init()

main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('GingerCat.jpg').convert()


def loadGrayscale(surface):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            red = pixel.r
            green = pixel.g
            blue = pixel.b
            pixelValue = (red+green+blue)/3
            surface.set_at((x, y), pixelValue)
            # how to set it to greyscale?!


loadGrayscale(my_surface)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()