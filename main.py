import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

win.fill((0, 0, 0))
x = 50
y = 420
width = 100
height = 20
speed = 10
bound = 5

g = 10
isJump = False
JumpCount = g

c2s = 30
clock = pygame.time.Clock()
animCount = 0
left, right = False, False
lastmove = "right"

bg = pygame.image.load('pictures/bg.jpg')
playerStand = pygame.image.load('pictures/idle.png')
walkRight = [pygame.image.load('pictures/right_1.png'), pygame.image.load('pictures/right_2.png'),
             pygame.image.load('pictures/right_3.png'), pygame.image.load('pictures/right_4.png'),
             pygame.image.load('pictures/right_5.png'), pygame.image.load('pictures/right_6.png')]
walkLeft= [pygame.image.load('pictures/left_1.png'), pygame.image.load('pictures/left_2.png'),
           pygame.image.load('pictures/left_3.png'), pygame.image.load('pictures/left_4.png'),
           pygame.image.load('pictures/left_5.png'), pygame.image.load('pictures/left_6.png')]


class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x, self.y, self.radius = x, y, radius
        self.color = color
        self.facing, self.vel = facing, 8*facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


bullets = []

def drawWindow():
    global animCount
    win.blit(bg, (0, 0))
    if animCount + 1 >= c2s:
        animCount = 0
    # win.fill((0, 0, 0))

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


run = True

while run:
    clock.tick(c2s)

    # pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not isJump:
        # if keys[pygame.K_UP] and y > bound:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < HEIGHT - height - bound:
        #     y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -g:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = g

    if keys[pygame.K_LEFT] and x > bound:
        x -= speed
        left, right = True, False
        lastmove = "left"
    elif keys[pygame.K_RIGHT] and x < WIDTH - width - bound:
        x += speed
        left, right = False, True
        lastmove = "right"
    else:
        left, right, animCount = False, False, 0

    if keys[pygame.K_f]:
        facing = 1 if lastmove == "right" else -1
        if len(bullets) < 5:
            xb = round(x + width // 2)
            yb = round(y + height // 2)
            color = (255, 0, 0)
            bullet = Projectile(xb, yb, 5, color, facing)
            bullets.append(bullet)

    for bullet in bullets:
        if 0 < bullet.x < WIDTH:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    drawWindow()


pygame.quit()
