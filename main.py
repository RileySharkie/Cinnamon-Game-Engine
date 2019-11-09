import pygame
import controls
import testroom
import player

pygame.init()

# the screen
screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("Cinnamon")
# icon = pygame.image.load('filename.png')
# pygame.display.set_icon(icon)

controls = controls.Controls()

room = testroom.TestRoom()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # get key changes
        if event.type == pygame.KEYDOWN:
            controls.key_down(event)
        if event.type == pygame.KEYUP:
            controls.key_up(event)

    #actions are taken here
    for entity in room.get_live():
        if type(entity) is player.Player:
            entity.action(controls)
        else:
            entity.action()



    screen.fill((0, 0, 0))
    # updating the display is the last thing that happens
    for blit_pair in room.blit():
        (blit_item, blit_location) = blit_pair
        screen.blit(blit_item, blit_location)

    pygame.display.update()
    clock.tick(30)