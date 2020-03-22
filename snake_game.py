import pygame
import random
pygame.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
screen_width=900
screen_height=600

gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SankeGame@krishna")

exit_game=False
game_over=False
init_velocity=5
score=0
snake_x=20
snake_y=25
snake_size=15
fps=60
velocity_x=0
velocity_y=0
food_x=random.randint(10,screen_width-5)
food_y=random.randint(10,screen_height-5)
snk_list=[]
snk_length=1



clock=pygame.time.Clock()
font=pygame.font.SysFont(None,60)
def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,black,[x,y,snake_size,snake_size])
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=init_velocity
                velocity_y=0

            if event.key==pygame.K_LEFT:
                velocity_x=-init_velocity
                velocity_y=0

            if event.key==pygame.K_UP:
                velocity_y=-init_velocity
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=init_velocity
                velocity_x=0
                                
    
    snake_x+=velocity_x
    snake_y+=velocity_y

    if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
        score+=1
        food_x=random.randint(0,screen_width)
        food_y=random.randint(0,screen_height)
        snk_length+=5

    gamewindow.fill(white)
    text_screen("Score:"+str(score*10),red,5,5)
    pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    
    if len(snk_list)>snk_length:
        del snk_list[0]

    plot_snake(gamewindow,black,snk_list,snake_size)    

    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()              