import pygame
#import SnakeGame
pygame.init()
displayx = 800
displayy = 600
display = pygame.display.set_mode((displayx,displayy))
pygame.display.update()
pygame.display.set_caption("Ett fönster")
running = True

class board:
    score = 0
    bounds = [0,displayx,80,displayy]
    font = pygame.font.SysFont("arial", 20)
    text = font.render(f"Score: {score}", True, (255,255,255),(0,0,0))
    def draw(self, display):
        pygame.draw.line(display,(255,255,255),(0,self.bounds),(800,self.bounds))
        display.blit(self.text, self.text.get_rect())
class object:
    pos = [20, 20]
    color  = (255, 128, 5)
    size = 20
    body = pygame.Rect((pos[0], pos[1]),(size,size))
    
    def draw(self, display):
        pygame.draw.rect(display,self.color, self.body)
    def update(self):
        self.body.update((self.pos[0],self.pos[1]),(self.size,self.size))
    def __init__(self, pos):
        self.pos = pos
    def __init__(self):
        pass

player = object()
tail = []
food = object()

b = board()
player.pos[1] = b.bounds + 40

boarders = []
boarders.append(pygame.Rect((0,b.bounds),(5,5)))
boarders.append(pygame.Rect((795,b.bounds),(5,5)))
boarders.append(pygame.Rect((0,595),(5,5)))
boarders.append(pygame.Rect((795,595),(5,5)))

def keyStroke(key):
    if key == pygame.K_LEFT:
        return [-1,0]
    if key == pygame.K_RIGHT:
        return [1,0]
    if key == pygame.K_DOWN:
        return [0,1]
    if key == pygame.K_UP:
        return [0,-1]

clock = pygame.time.Clock()
direction = [1,0]
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

            direction = keyStroke(event.key)
    
    player.pos[0] += direction[0]*10
    player.pos[1] += direction[1]*10
    display.fill((0,0,0))
    player.update()
    b.draw(display)
    player.draw(display)
    
    for x in boarders:
        pygame.draw.rect(display,(255,0,0),x)


    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()