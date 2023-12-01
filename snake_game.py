import pygame
import random
import math
pygame.init()

#screen
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()

#font 
font = pygame.font.Font('media/ARCADE.TTF', 60)
gameover = font.render("Game Over", True, (255, 255, 255))

againfont = pygame.font.Font('media/ARCADE.TTF', 30)
try_again = againfont.render("press 'C' to try again", True, (255, 255, 255))

scorefont = pygame.font.Font('media/ARCADE.TTF', 20)



#snake 
player_block = 10
snake_speed = 20


foodX = round(random.randrange(0, 500 - player_block) / 10.0) * 10.0
foodY = round(random.randrange(0, 500 - player_block) / 10.0) * 10.0


def our_snake(player_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], player_block, player_block])

def isCollision(foodX, foodY, playerX, playerY):
    if foodX == playerX and foodY == playerY:
        return True 
    else:
        return False


def score_show(score):
    scoretext = scorefont.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(scoretext, (0,0))
 


#game loop
def gameLoop():
    game_over = False
    game_close = False

    #snake 

    playerX = 250
    playerY = 250
    playerX_change = 0
    playerY_change = 0

    snake_List = []
    Length_of_snake = 1
    
    score = 0

    foodX = round(random.randrange(0, 500 - player_block) / 10.0) * 10.0
    foodY = round(random.randrange(0, 500 - player_block) / 10.0) * 10.0
    while not game_over:

        screen.fill((0, 0, 0))

        while game_close == True:

            screen.fill((0, 0, 0))    

            screen.blit(gameover, (120, 200))
            screen.blit(try_again, (100, 300))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    
                    if event.key == pygame.K_c:
                        gameLoop()
        # quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False

                if event.key == pygame.K_c:
                            gameLoop()

                if event.key == pygame.K_LEFT:
                    playerX_change = -10
                    playerY_change = 0
                if event.key == pygame.K_RIGHT:
                    playerX_change = 10
                    playerY_change = 0
                if event.key == pygame.K_DOWN:
                    playerX_change = 0
                    playerY_change = 10
                if event.key == pygame.K_UP:
                    playerX_change = 0
                    playerY_change = -10

        playerX += playerX_change
        playerY += playerY_change

        if playerX >= 500:
            playerX = 0
        elif playerX < 0:
            playerX = 500
        if playerY > 490:
            playerY = 0
        elif playerY < 0:
            playerY = 490
        #snake

        pygame.draw.rect(screen, (255, 0, 0), [foodX, foodY, 10, 10])

        snake_Head = []
        snake_Head.append(playerX)
        snake_Head.append(playerY)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(player_block, snake_List)
        

        collision = isCollision(foodX, foodY, playerX, playerY)
        if collision:
            foodX = round(random.randrange(0, 500 - 10) / 10.0) * 10.0
            foodY = round(random.randrange(0, 500 - 10) / 10.0) * 10.0
            Length_of_snake += 1
            

        clock.tick(snake_speed)
        score_show((Length_of_snake -1) * 10)
        pygame.display.update()
        

    pygame.quit()
    quit()
 
 
gameLoop()