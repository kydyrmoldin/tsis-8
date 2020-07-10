import pygame
import sys
import random
pygame.init()

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 255)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (255,0 ,0)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 240, 0)
COUNT_BLOCKS = 20 
HEADER_MARGIN = 70

MARGIN = 1
size = (SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCKS, 
SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCKS + HEADER_MARGIN)
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("snake Sula1")
img = pygame.image.load("snake.png")
pygame.display.set_icon(img)
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier',36)


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS 

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y    

def random_block():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = SnakeBlock(x,y)
    while empty_block in snake_block:
        empty_block.x =  random.randint(0, COUNT_BLOCKS - 1)
        empty_block.y =  random.randint(0, COUNT_BLOCKS - 1)
    return empty_block 
def draw_block(color,row, column ):
    pygame.draw.rect(screen, color, [SIZE_BLOCK+column*SIZE_BLOCK + MARGIN*(column+1), 
                HEADER_MARGIN + SIZE_BLOCK + row*SIZE_BLOCK + MARGIN*(row+1), SIZE_BLOCK, SIZE_BLOCK])

snake_block = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]                
apple = random_block()
direct_row = 0
direct_col = 1
score = 0 
speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ('exit')
            quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direct_col !=0:
                direct_row = -1
                direct_col = 0
            elif event.key == pygame.K_DOWN and direct_col !=0:
                direct_row = 1
                direct_col = 0 
            elif event.key == pygame.K_LEFT and direct_row !=0:
                direct_row = 0
                direct_col = -1 
            elif event.key == pygame.K_RIGHT and direct_row !=0:
                direct_row = 0
                direct_col = 1         

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0,0, size[0], HEADER_MARGIN])

    text_score = courier.render(f"Score: {score}", 0, WHITE)
    text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
    screen.blit(text_score, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK+200, SIZE_BLOCK))

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            
            draw_block(color, row, column)   
    
    head = snake_block[-1]
    if  not head.is_inside():
        print ('crash')
        quit()
        sys.exit()

    draw_block(RED, apple.x, apple.y)    

    for block in snake_block:
        draw_block(SNAKE_COLOR, block.x, block.y) 
    
    
    pygame.display.flip()
    if apple == head:
        score+=1
        speed += score//5 + 1
        snake_block.append(apple)
        apple = random_block()


    new_head = SnakeBlock(head.x + direct_row, head.y + direct_col)         
    snake_block.append(new_head)
    snake_block.pop(0)

    #if new_head in snake_block:
     #   print ('crash yourself')
      #  quit()
       # sys.exit()

    
       
    timer.tick(3 + speed)         