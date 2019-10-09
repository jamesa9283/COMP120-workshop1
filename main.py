import pygame

pygame.init()

main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('GingerCat.jpg').convert()


def lessRed(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y),
                           pygame.Color(int(pixel.r * 0.5), pixel.g, pixel.b))


lessRed(my_surface)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()
