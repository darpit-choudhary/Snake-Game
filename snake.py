import pygame 
import time
import random

#initialize the python modules
pygame.init()          

#define colors
blue = (0,0,255)
red = (255,0,0)
bg_color = (0,204,106)
green = (255,255,0)
black = (0,0,0)
yellow = (0,255,255)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))            #surface
pygame.display.set_caption("Snake Game")      

clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont('comicsansms', 30)
score_style = pygame.font.SysFont('comicsansms', 15)

#define the score function
def my_score(score):
    sc = score_style.render(f"Your Score: {score}", True, yellow)
    dis.blit(sc, [10,10])

#message function
def message(msg, color):
    global i
    mess = font_style.render(msg, True, color)
    dis.blit(mess, [100, 250])

#length increase function
def snakeLength(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0],x[1],snake_block,snake_block])


def game_loop():
    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0      #to store the changes in x1 and y1 due to moving
    y1_change = 0
    
    snake_list = []
    length_snake = 1
    
    game_close = False
    game_over = False                           #while this is true the game will not close until we do so 
    
    foodx = round(random.randrange(10, dis_width - snake_block)/10.0)*10.0
    foody = round(random.randrange(10, dis_height - snake_block)/10.0)*10.0
    #giving the option to play or continue
    while not game_over:
        while game_close == True:
            dis.fill(black)
            messa = font_style.render("You Lost!", True, red)
            dis.blit(messa, [300, 200])
            message("Press ESC - Quit or SPACE - Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        game_loop()
            
            
        for event in pygame.event.get():
            #print(event)          #prints all the events that take place on the screen like mousebutton clicks
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
        
        # to make sure that the game will be over if the snake touches the boundary
        if x1==0 or x1>=dis_width or y1==0 or y1>=dis_height:      
            game_close = True
        
        #update the co-ordinates and the background color
        x1+=x1_change                                                    
        y1+=y1_change
        dis.fill(bg_color)
        
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        
        snake_list.append(snake_head)
       
        # to make sure snake does not grow just by moving around
        if len(snake_list)>length_snake:
            del snake_list[0]
        
         #  To make sure that game is over if snake collides with itself
        for x in snake_list[:-1]:                                
            if x == snake_head:
                game_close = True
        
        #call the function for increasing length and score
        snakeLength(snake_list)
        my_score(length_snake-1)
        
        pygame.display.update()
        
        # if snake eats the food, make new food
        if x1 == foodx and y1 == foody:
           foodx = round(random.randrange(10, dis_width - snake_block)/10.0)*10.0
           foody = round(random.randrange(10, dis_height - snake_block)/10.0)*10.0
           length_snake+=1
        
        clock.tick(snake_speed)
    
    
    pygame.quit()
    quit()
    
game_loop()