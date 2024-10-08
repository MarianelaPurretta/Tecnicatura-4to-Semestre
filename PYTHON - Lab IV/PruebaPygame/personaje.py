import pygame



#config de pantalla
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

#Posicion del jugador
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#Velocidad del jugador
player_speed = 5

#Bucle principal:
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Detectar las teclas para presionar:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:  # FLECHA IZQUIERDA
        player_pos.x -= player_speed  # Mueve hacia la izquierda (disminuye X)
    if keys[pygame.K_RIGHT]:  # FLECHA DERECHA
        player_pos.x += player_speed  # Mueve hacia la derecha (aumenta X)
    if keys[pygame.K_DOWN]:  # FLECHA ABAJO
        player_pos.y += player_speed  # Mueve hacia abajo (aumenta Y)
    if keys[pygame.K_UP]:  # FLECHA ARRIBA
        player_pos.y -= player_speed  # Mueve hacia arriba (disminuye Y)

    #Limpiar pantalla
    screen.fill('green')

    #Dibujar el jugador:
    pygame.draw.circle(screen,(255, 0, 0),(int(player_pos.x), int(player_pos.y)), 10)

    #Actializar pantalla
    pygame.display.flip()

    #Control de velocidad del jugador:
    clock.tick(60)



pygame.quit() #termina el programa
