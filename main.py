import pygame
import controls
import debugroom
import player

pygame.init()

# the screen
screen = pygame.display.set_mode((800, 640))


pygame.display.set_caption("Cinnamon")
# icon = pygame.image.load('filename.png')
# pygame.display.set_icon(icon)

controls = controls.Controls()

room = debugroom.DebugRoom()

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

    # actions are taken here
    room.check_action(controls)

    # move the camera if needed
    room.camera.follow()

    screen.fill((0, 0, 0))
    # updating the display is the last thing that happens
    for blit_item in room.blit():
        (blit_sprite, blit_location, crop) = blit_item
        screen.blit(blit_sprite, blit_location, crop)

    pygame.display.update()
    clock.tick(30)
