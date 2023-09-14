import pygame
import random

def main():
    pygame.init()
    screen=pygame.display.set_mode((300,400))
    pygame.display.set_caption('똥 피하기')

    font = pygame.font.SysFont(None, 30)
    gameover_font = pygame.font.SysFont(None, 50)
    gameover_text = gameover_font.render('GAME OVER',
                                        True,
                                        (255,0,0))
    score = 0
    speed = 0

    image_char = pygame.image.load('./img/ramg.png')
    image_char = pygame.transform.scale(image_char, (50,50))
    image_bg = pygame.image.load('./img/sky.jpg')
    image_bg = pygame.transform.scale(image_bg, (300,400))
    
    image_enemy = pygame.image.load('./img/ddong.png')
    image_enemy = pygame.transform.scale(image_enemy, (50,50))
    enemy = [image_enemy for i in range(10)]
    enemy_y = [random.randrange(-1600, -50) for i in range(10)]

    x_pos = 150 - 25
    y_pos = 400 - 50

    running = True
    while running:
        for i in range(10):
            if enemy_y[i] >= 400:
                enemy_y[i] = random.randrange(-500, -50) 
                score+=1
            enemy_y[i] += 0.1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    speed = 0.1
                elif event.key == pygame.K_LEFT:
                    speed = -0.1           
            if event.type == pygame.KEYUP:
                speed=0
        if 0 <= x_pos <= 250:
            x_pos += speed
        elif x_pos > 250:
            x_pos = 250
        else:
             x_pos = 0

        screen.blit(image_bg, (0,0))

        for i in range(10):
            screen.blit(enemy[i], (30*i-10, enemy_y[i]))
            if enemy_y[i]+50 >= y_pos:
                if x_pos-30 <= 30*i -10 <= x_pos+30:
                    screen.blit(gameover_text, (70,150))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    running=False
        
        scoreText = font.render('Score :'+str(score),
                                True,
                                (0,0,0))
        screen.blit(scoreText, (10,10))


        screen.blit(image_char, (x_pos,y_pos))
        pygame.display.update()


if __name__ == "__main__":
    main()