import pygame
import time
import random
from datetime import datetime
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Snake 2')
running = True


class Snake:
    def MakeFood():
        foodx = round(random.randint(15, 625), -1) * 2
        foody = round(random.randint(15, 315), -1) * 2
        food = pygame.Rect(foodx, foody, 20, 20)
        
        if food[0] == snakehead[0] and food[1] == snakehead[1]:
            food = Snake.MakeFood()
                
        for snakesegment in snake:
            if food[0] == snakesegment[0] and food[1] == snakesegment[1]:
                food = Snake.MakeFood()
                
        for lava in lavasplotches:
            if lava.collidepoint((food[0], food[1])):
                food = Snake.MakeFood()
        
        for banana in bananas:
            if pygame.Rect(banana).collidepoint((food[0], food[1])):
                food = Snake.MakeFood()
                
        return food
    
    def FramePerfectTrickPrevention(going, snakehead, snake):
        global newtime, frameperfecttricktime, disaster
        testsnakehead = snakehead
        if going == "LEFT":
            testsnakehead = (snakehead[0] - 20, snakehead[1], snakehead[2], snakehead[3])
        elif going == "UP":
            testsnakehead = (snakehead[0], snakehead[1] - 20, snakehead[2], snakehead[3])
        elif going == "DOWN":
            testsnakehead = (snakehead[0], snakehead[1] + 20, snakehead[2], snakehead[3])
        elif going == "RIGHT":
            testsnakehead = (snakehead[0] + 20, snakehead[1], snakehead[2], snakehead[3])
        else:
            testsnakehead = snakehead
        
        if pygame.Rect(testsnakehead).colliderect(snake[1]):
            if going == "LEFT":
               going = "RIGHT"
            elif going == "RIGHT":
                going = "LEFT"
            elif going == "UP":
                going = "DOWN"
            elif going == "DOWN":
                going = "UP"
            
            if disaster != "MONKEY MODE":    
                frameperfecttricktime = newtime
        return going
        
    def MoveHead(going):
        global snakehead, running, snake, deathmessage, actions
        
        going = Snake.FramePerfectTrickPrevention(going, snakehead, snake)
        
        if going == "LEFT":
            snakehead = (snakehead[0] - 20, snakehead[1], snakehead[2], snakehead[3])
        elif going == "UP":
            snakehead = (snakehead[0], snakehead[1] - 20, snakehead[2], snakehead[3])
        elif going == "DOWN":
            snakehead = (snakehead[0], snakehead[1] + 20, snakehead[2], snakehead[3])
        elif going == "RIGHT":
            snakehead = (snakehead[0] + 20, snakehead[1], snakehead[2], snakehead[3])
        else:
            snakehead = snakehead
        
        for snakesegment in snake:
            if pygame.Rect(snakesegment).colliderect(pygame.Rect(snakehead[0], snakehead[1], 20, 20)):
                snakehead = (-900000, -1000000000, snakehead[2], snakehead[3])
                if snakesegment == snake[1]:
                    deathmessage = "FRAME PERFECT TRICK"
                else:
                    deathmessage = "RAN INTO ITSELF"
                
                if actions > 3:
                    deathmessage = "SLIPPED ON THE BANANA"
                
        for lava in lavasplotches:
            if lava.collidepoint((snakehead[0], snakehead[1])):
                snakehead = (-900000, -1000000000, snakehead[2], snakehead[3])
                deathmessage = "SWAM IN LAVA"
            
    def MoveBody(snake): 
        for i in range(len(snake)):
            snakesegment = len(snake) - i - 1  
            if snakesegment > 0:
                snake[snakesegment] = snake[snakesegment - 1]
            else:
                snake[snakesegment] = snakehead   
    
    def Screen():  
        global running, lavasplotches, foodtimeset, spotlight, radius, warpfood, spits, bananas, reverse, mansplaining, bullets, bullethell, finaltime
        global bombs, disaster, movingfood, food, actions, going, deathmessage, newtime, frameperfecttricktime, snakehead, snake
        going = None
        running = True
        
        snakehead = pygame.Rect(80, 360, 20, 20) 
        snake1 = pygame.Rect(60, 360, 20, 20)
        snake2 = pygame.Rect(40, 360, 20, 20)
        snake = [snake1, snake2]
        
        
        currenttime = time.time()
        speedtime = time.time()
        movetime = time.time()
        spittime = time.time()
        foodspawntime = time.time()
        bullettime = time.time()
        bulletspawntime = time.time()
        percentincreasetime = time.time()
        frameperfecttricktime = time.time()
        spotlighttime = time.time()
        
        radius = 0
        spotlight = [80, 60]
        warpfood = False
        started = False
        spits = []
        bananas = []
        reverse = False
        mansplaining = False
        bullets = []
        bullethell = False
        bombs = []
        movingfood = False
        percentage = 0
        
        eattime = currenttime
        foodtimeset = 20
        fooddirection = ["UP", "LEFT"]
        
        disaster = "NONE"
        spotlightdirection = ["DOWN", "LEFT"]
        
        x = 0
        y = 0
        z = 0
        lavasplotches = []
        spotlight = pygame.Rect(80, 60, 0, 0)
        disscore = 0
        disasternum = 0
        food = pygame.Rect(600, 360, 20, 20)
        score = 0
        actions = 1
        speedboost = False
        deathmessage = "SKILL ISSUE"
        
        inputs = [119, 1073741906, 97, 1073741904, 115, 1073741905, 100, 1073741903, 32]
        while running:
            bruh = False
            pressed = False
            newtime = time.time()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quit()
            if disaster == "GREEN":
                backgroundcolor = (32, 120, 81)
            elif disaster == "REVERSE":
                backgroundcolor = (254, 254, 237)
            else:
                backgroundcolor = (1, 1, 18)
            screen.fill(backgroundcolor)    
            foodcolor = (131, 50, 40)  

            for event in events:
                if event.type == pygame.KEYDOWN and event.key in inputs and newtime - movetime > 0.047:
                    movetime = newtime
                    if started == False:
                        starttime = time.time()
                        started = True
                    if event.key == 119 or event.key == 1073741906:
                        if reverse == True:
                            if going != "DOWN" or going != "UP":
                                going = "UP"
                                pressed = True
                        else:
                            if going != "DOWN" and going != "UP":
                                going = "UP"
                                pressed = True
                            
                    elif event.key == 97 or event.key == 1073741904:
                        if reverse == True:
                            if going != "RIGHT" or going != "LEFT":
                                going = "LEFT"
                                pressed = True
                        else:
                            if going != "RIGHT" and going != "LEFT":
                                going = "LEFT"
                                pressed = True
                            
                    elif event.key == 115 or event.key == 1073741905:
                        if reverse == True:
                            if going != "UP" or going != "DOWN":
                                going = "DOWN"
                                pressed = True
                        else:
                            if going != "UP" and going != "DOWN":
                                going = "DOWN"
                                pressed = True
                                
                    elif event.key == 100 or event.key == 1073741903:
                        if reverse == True:
                            if going != "LEFT" or going != "RIGHT":
                                going = "RIGHT" 
                                pressed = True
                        else:
                            if going != "LEFT" and going != "RIGHT":
                                going = "RIGHT" 
                                pressed = True
                    if reverse == True:
                        if going == "DOWN":
                            if snakehead[1] - 20 != snake[0][1]:
                                going = "UP"
                        elif going == "UP":
                            if snakehead[1] + 20 != snake[0][1]:
                                going = "DOWN"
                        elif going == "LEFT":
                            if snakehead[0] + 20 != snake[0][0]:
                                going = "RIGHT"
                        elif going == "RIGHT":
                            if snakehead[0] - 20 != snake[0][0]:
                                going = "LEFT" 
                    
                    if event.key == 32 and percentage == 1:
                        speedboost = True
                        pressedtime = newtime
                        speedtime = newtime
                        percentage = 0
                    
            if pressed == True and newtime - currenttime > 0.05:
                currenttime = newtime
                Snake.MoveBody(snake)
                Snake.MoveHead(going)

            disasters = []
          
            if speedboost == True:
                if reverse == True:
                    boosttime = 1.5
                else:
                    boosttime = 0.5
                if newtime - pressedtime < boosttime:
                    actions = 2
                    if reverse == True:
                        actions = 0
                else:
                    speedboost = False
                    if reverse == True:
                        Snake.MoveBody(snake)
                        Snake.MoveHead(going)
                
            else:
                actions = 1
                speedboost = False
            
            for i in range(5):
                disasters.append("NONE")
            for i in range(10):
                disasters.append("LAVA")
            for i in range(10):
                disasters.append("FAST FOOD")
            for i in range(10):
                disasters.append("SPOTLIGHT")
            for i in range(10):
                disasters.append("WARP FOOD")
            for i in range(10):
                disasters.append("GREEN")
            for i in range(10):
                disasters.append("MONKEY MODE")
            for i in range(4): # 4, because i don't like it
                disasters.append("SPIT")
            for i in range(10):
                disasters.append("REVERSE")
            for i in range(10):
                disasters.append("MANSPLAINING")
            for i in range(10):
                disasters.append("BULLET HELL")
            for i in range(10):
                disasters.append("BOMB FIELD")
            for i in range(10):
                disasters.append("MOVING FOOD")
            
            if score % 5 == 0 and score > 0 and x < 2:
                deathmessage = disaster
                disaster = None
                x += 1
                
                if x == 1:
                    x += 1
                    disaster = random.choice(disasters)
                    disscore = score
                    disasternum = int(score / 5)
                    Snake.RouteDisaster(disaster)
            
            if disaster == "WARP FOOD":
                foodcolor = (190, 56, 167)      
            elif disaster == "FAST FOOD":
                foodcolor = (255, 0, 0)
            elif disaster == "MOVING FOOD":
                foodcolor = (245, 81, 122)
            
            if score > disscore:
                newdisasternum = int(score / 5)
                if newdisasternum > disasternum:
                    x = 0

            snakecolor = (43, 134, 229)
            snakeheadcolor = (0, 91, 186)
            
            if disaster == "GREEN":
                snakecolor = (32, 120, 81)
                snakeheadcolor = (32, 120, 81)
                foodcolor = (29, 115, 76)
            elif disaster == "MONKEY MODE":
                foodcolor = (240, 193, 38)
                snakecolor = (89, 43, 25)
                snakeheadcolor = (51, 28, 16)
                actions = random.randint(1, 3)
                if snake[1][0] == food[0] and snake[1][1] == food[1]:
                    food = Snake.MakeFood()
                    eattime = newtime
                    snake.append(pygame.Rect(0, 0, 20, 20))
                    score += 1
                for banana in bananas:
                    pygame.draw.rect(screen, (201, 158, 16), banana)
                    if pygame.Rect(banana).collidepoint((snakehead[0], snakehead[1])):
                        actions = 8
                        directions = ["RIGHT", "LEFT", "UP", "DOWN"]
                        if going == "RIGHT":
                            directions.remove("LEFT")
                        elif going == "LEFT":
                            directions.remove("RIGHT")
                        elif going == "UP":
                            directions.remove("DOWN")
                        elif going == "DOWN":
                            directions.remove("UP")
                        going = random.choice(directions)
                        
            elif disaster == "REVERSE":
                snakecolor = (212, 121, 36)
                snakeheadcolor = (255, 164, 69)
                foodcolor = (144, 195, 210)  
            
            linecolor = (3, 14, 25)
            if disaster == "REVERSE":
                linecolor = (252, 241, 230)
                
            for line in range(64):
                pygame.draw.line(screen, linecolor, ((line+1) * 20, 0), ((line+1) * 20, 720))
            for line in range(36):
                pygame.draw.line(screen, linecolor, (0, (line+1) * 20), (1280, (line+1) * 20))
            
            for snakesegment in snake:
                pygame.draw.rect(screen, snakecolor, snakesegment)
            
            if newtime - spotlighttime > 0.05:
                for movement in range(actions):
                    Snake.SpotlightMove(spotlight, spotlightdirection)
                spotlighttime = newtime
            
            
            if newtime - currenttime >= 0.105 and going != None and pressed != True: 
                currenttime = newtime
                for movement in range(actions):
                    Snake.MoveBody(snake)
                    Snake.MoveHead(going)
                    if movingfood == True:
                        Snake.MoveFood(food, fooddirection)
                        pygame.draw.rect(screen, (245, 81, 122), food)
                        Snake.MoveFood(food, fooddirection)
            
            if 0 < snakehead[0] < 1260:
                if 0 < snakehead[1] < 680:
                    bruh = True
                    if actions > 3:
                        deathmessage = "SLIPPED ON BANANA PEEL"
    
            running = bruh
        
            for lavasplotch in lavasplotches:
                pygame.draw.rect(screen, (185, 42, 49), lavasplotch)
                if pygame.Rect(snakehead[0], snakehead[1], 20, 20).collidepoint((lavasplotch[0], lavasplotch[1])):
                    running = False
                    
                if lavasplotch.collidepoint((food[0], food[1])):
                    food = Snake.MakeFood()
            
            if pygame.Rect(snakehead[0], snakehead[1], 20, 20).colliderect(food):
                food = Snake.MakeFood()
                y = 0
                eattime = newtime
                snake.append(pygame.Rect(0, 0, 20, 20))
                score += 1
                percentage += 0.15
                if warpfood == True:
                    Snake.WarpSnake()     
                    going = random.choice(["RIGHT", "LEFT", "UP", "DOWN"])
       
            if pygame.Rect(snake[0][0], snake[0][1], 20, 20).collidepoint((food[0], food[1])):
                food = Snake.MakeFood()
                y = 0
                eattime = newtime
                snake.append(pygame.Rect(0, 0, 20, 20))
                score += 1
                percentage += 0.15
                if warpfood == True:
                    Snake.WarpSnake()
                    going = random.choice(["RIGHT", "LEFT", "UP", "DOWN"])
                    
            if newtime - eattime > foodtimeset and y == 0:
                y += 1
                food = Snake.MakeFood()
                foodspawntime = newtime
            
            pygame.draw.circle(screen, (255, 238, 183), (spotlight[0], spotlight[1]), radius)
            if disaster == "SPOTLIGHT":
                snakeheadmeetspotlight = Snake.CheckForSpotlight(snakehead, spotlight)
                if snakeheadmeetspotlight == True:
                    snakeheadcolor = (255, 0, 0)
                    running = False
                    deathmessage = "COULDN'T HANDLE FAME"
            
            if newtime - bulletspawntime > 5 and bullethell == True:
                bullets = Snake.SpawnBullets()
                bulletspawntime = newtime
            elif newtime - bullettime > 0.1:
                bullettime = newtime
                for bullet in bullets:
                    bullet[0] -= (random.randint(1, 3)) * 20
            
            for bomb in bombs:
                timesincespawn = newtime - bomb[5]
                timeuntilexplode = bomb[4] - timesincespawn
                bombrect = pygame.Rect(bomb[0], bomb[1], bomb[2], bomb[3]) 
                if timeuntilexplode > 0:
                    red = 120 - (timeuntilexplode*10)
                    green = 60 + (timeuntilexplode*10)
                    blue = 60 + (timeuntilexplode*10)
                    
                    bombcolor = (red, green, blue)
                    text = round(timeuntilexplode, 1)
                elif timeuntilexplode < 0:
                    bombcolor = (255, 50, 35)
                    text = "BOOM"
                    if bombrect.collidepoint((snakehead[0], snakehead[1])):
                        running = False
                        deathmessage = "BLOWN UP"
                    
                    bombs.remove(bomb)
                    Snake.MakeBomb(1)

                pygame.draw.circle(screen, bombcolor, bombrect.center, 80)
                bombfont = pygame.font.SysFont(None, 43, bold = True)
                bombtext = bombfont.render(f'{text}', True, (255, 255, 255))
                bombsurface = bombtext.get_rect(center=bombrect.center)
                screen.blit(bombtext, bombsurface)
            
            pygame.draw.rect(screen, snakeheadcolor, snakehead)
            for snakesegment in snake:
                pygame.draw.rect(screen, snakecolor, snakesegment)
            
            for bullet in bullets:
                pygame.draw.rect(screen, (60, 60, 75), bullet)
                if pygame.Rect(bullet) == snakehead:
                    running = False
                    deathmessage = "GOT SHOT"
                      
            pygame.draw.rect(screen, foodcolor, food)
            
            ######################
            
            bordera = pygame.Rect((0, 0, 20, 700))
            borderb = pygame.Rect((1260, 0, 20, 700))
            borderc = pygame.Rect((0, 0, 1280, 20))
            borderd = pygame.Rect((0, 680, 1280, 40))
            borders = [bordera, borderb, borderc, borderd]
            
            for border in borders:
                pygame.draw.rect(screen, (20, 20, 35), border)
            
            toptextfont = pygame.font.Font(None, 20)
            
            basecolor = (55, 65, 75)
            readycolor = (175, 205, 185)
            pygame.draw.rect(screen, basecolor, (1100, 1, 150, 18))
            
            if newtime - percentincreasetime > 0.06:
                percentage += 0.01
                percentincreasetime = newtime
            if percentage > 1:
                percentage = 1
                if random.randint(1, 2) == 1:
                    readycolor = (205, 230, 255)
                else:
                    readycolor = (205, 255, 235)
                
            pygame.draw.rect(screen, readycolor, (1100, 1, 150*percentage, 18))
            
            timeuntilfood = foodtimeset - int(newtime - eattime)
            
            if timeuntilfood <= 0:
                eattime = newtime
                food = Snake.MakeFood()
            
            foodtimertext = toptextfont.render(f"FOOD MOVES IN: {timeuntilfood}", True, (155, 215, 255))
            foodtimersurface = foodtimertext.get_rect(center = (65, 10))
            screen.blit(foodtimertext, foodtimersurface)
            try:
                timeingame = newtime - starttime
            except:
                timeingame = 0
            minutes = 0
            hours = 0
            
            if timeingame >= 60:
                minutes = int(timeingame / 60)
            
            if timeingame >= 3600:
                hours = int(timeingame / 3600)
                minutes -= (60 * hours)
                
            Hours = 3600*hours
            Minutes = 60*minutes
            
            seconds = timeingame - Hours - Minutes    
            
            timeingame = f'{hours} : {minutes} : {round(seconds, 2)}'
            
            speedruntext = toptextfont.render(timeingame, True, (155, 215, 255))
            speedrunsurface = speedruntext.get_rect(center = (640, 10))
            screen.blit(speedruntext, speedrunsurface)
            
            scorefont = pygame.font.Font(None, 42)
            scoretext = scorefont.render(f"SCORE: {score}", True, (235, 245, 255))
            scoresurface = scoretext.get_rect(center = (640, 697))
            screen.blit(scoretext, scoresurface)
            
            bytext = scorefont.render(f"BY EDWARD MERCADO", True, (155, 215, 255))
            bysurface = bytext.get_rect(left = 30, centery = 697)
            screen.blit(bytext, bysurface)     
            
            eventtext = scorefont.render(f"DISASTER: {disaster}", True, (155, 215, 255))
            eventsurface = eventtext.get_rect(right = 1250, centery = 697)
            screen.blit(eventtext, eventsurface)  
            
            if disaster == "SPIT":
                for spit in spits:
                    pygame.draw.circle(screen, (200, 253, 210), (spit[0], spit[1]), spit[2])
            if newtime - spittime > 0.6:
                for spit in spits:
                    spit[1] += (random.randint(5, 20)) / 10
                    if spit[1] > 600:
                        spits = Snake.HawkTuah()
                spittime = newtime
            
            if mansplaining == True:
                if snakehead[0] - food[0] > 0:
                    action = "LEFT!"
                elif snakehead[0] - food[0] < 0:
                    action = "RIGHT!"
                else:
                    action = "GOOD!"
                
                if snakehead[1] - food[1] > 0:
                    actiontwo = "UP!"
                elif snakehead[1] - food[1] < 0:
                    actiontwo = "DOWN!"
                else:
                    action = "GOOD!"
                
                if newtime - movetime < 0.5:
                    action = "TURNED"
                    actiontwo = f'{going}!'

                if newtime - speedtime < 0.5:
                    action = "SPEED"
                    actiontwo = "BOOST!"
                    
                if newtime - eattime < 0.5:
                    action = "ATE"
                    actiontwo = "FOOD!"
                    
                if newtime - foodspawntime < 0.5:
                    action = "NEW FOOD"
                    actiontwo = "SPAWNED!"
                
                if newtime - frameperfecttricktime < 1.7:
                    action = "FRAME!"
                    actiontwo = "PERFECT!"
                    actionthree = "TRICK!"
                
                if action != "FRAME!":
                    mansplainfont = pygame.font.SysFont(None, 520, bold = True)
                    
                    mansplain = mansplainfont.render(action, True, (255, 255, 255))
                    mansplainsurface = mansplain.get_rect(center=(640, 200))
                    screen.blit(mansplain, mansplainsurface)
                    
                    mansplaintwo = mansplainfont.render(actiontwo, True, (255, 255, 255))
                    mansplainsurfacetwo = mansplaintwo.get_rect(center=(640, 500))
                    screen.blit(mansplaintwo, mansplainsurfacetwo)
                else:
                    mansplainfont = pygame.font.SysFont(None, 290, bold = True)
                    colors = [(250, 245, 225), (255, 255, 255)]
                    color = random.choice(colors)
                    
                    mansplain = mansplainfont.render(action, True, color)
                    mansplainsurface = mansplain.get_rect(center=(640, 155))
                    screen.blit(mansplain, mansplainsurface)
                    
                    mansplaintwo = mansplainfont.render(actiontwo, True, color)
                    mansplainsurfacetwo = mansplaintwo.get_rect(center=(640, 355))
                    screen.blit(mansplaintwo, mansplainsurfacetwo)
                    
                    mansplainthree = mansplainfont.render(actionthree, True, color)
                    mansplainsurfacethree = mansplainthree.get_rect(center=(640, 555))
                    screen.blit(mansplainthree, mansplainsurfacethree)
            
            pygame.display.update()
        
        print(f'SCORE: {score}')
        finaltime = timeingame
        Snake.HighScoreStuff(score)
          
    def RouteDisaster(disaster):
        global foodtimeset, lavasplotches, spotlight, radius, warpfood, spits, actions, bananas, reverse, mansplaining, bullets, bullethell, bombs
        global movingfood
        if disaster == "LAVA":
            bullets = []
            lavasplotches = Snake.Lava()
            foodtimeset = 20
            radius = 0 
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = False
        elif disaster == "FAST FOOD":
            bullets = []
            lavasplotches = [ ]
            foodtimeset = 3
            radius = 0
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = False
        elif disaster == 'SPOTLIGHT':
            bullets = []
            lavasplotches = [ ]
            foodtimeset = 20
            radius = 110
            if Snake.CheckForSpotlight(spotlight, snakehead) == True:
                spotlight[0] += 200
                if spotlight[0] > 200:
                    spotlight[0] -= 500
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = False
        elif disaster == "WARP FOOD":
            bullets = []
            warpfood = True
            lavasplotches = []
            foodtimeset = 20
            radius = 0
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = False
        elif disaster == "SPIT":
            bullets = []
            lavasplotches = []
            foodtimeset = 8
            radius = 0
            warpfood = False
            spits = Snake.HawkTuah()
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = False
        elif disaster == "MONKEY MODE":
            bullets = []
            lavasplotches = []
            foodtimeset = 20
            radius = 0
            warpfood = False
            spits = []
            actions = 3
            bananas = Snake.BananaPeels()
            reverse = False
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = False
        elif disaster == "REVERSE":
            bullets = []
            lavasplotches = []
            foodtimeset = 20
            radius = 0
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = True
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = False
        elif disaster == "MANSPLAINING":
            bullets = []
            lavasplotches = []
            foodtimeset = 20
            radius = 0
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = True
            bullethell = False
            bombs = []
            movingfood = False
        elif disaster == "BULLET HELL":
            bullets = Snake.SpawnBullets()
            lavasplotches = []
            foodtimeset = 20
            radius = 0
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = True
            bombs = []
            movingfood = False
        elif disaster == "BOMB FIELD":
            lavasplotches = []
            foodtimeset = 20
            radius = 0
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = False
            if len(bombs) == 0:
                bombs = Snake.MakeBomb(35)
            else:
                bombs = Snake.MakeBomb(10)
            movingfood = False
        elif disaster == "MOVING FOOD":
            lavasplotches = []
            foodtimeset = 20
            radius = 0
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = True
        else:
            lavasplotches = []
            foodtimeset = 20
            radius = 0
            warpfood = False
            spits = []
            actions = 1
            bananas = []
            reverse = False
            mansplaining = False
            bullethell = False
            bombs = []
            movingfood = False
   
    def MoveFood(food, fooddirection):
        global snakehead, actions, going
        food[2] += 1
        if food[2] > 50:
            food[2] = 50
        food[3] += 1
        if food[3] > 50:
            food[3] = 50
        if actions > 1:
            food[2] = food[3] = 20
            if going == "RIGHT":
                food[0] -= round(random.randint(0, 40), -1) * 2
            elif going == "LEFT":
                food[0] += round(random.randint(0, 40), -1) * 2
            elif going == "UP":
                food[1] += round(random.randint(0, 40), -1) * 2
            elif going == "DOWN":
                food[1] -= round(random.randint(0, 40), -1) * 2

        if "UP" in fooddirection:
            food[1] -= 8
            if food[1] < 40:
                fooddirection.remove("UP")
                fooddirection.append("DOWN")
        elif "DOWN" in fooddirection:
            food[1] += 8
            if food[1] > 660:
                fooddirection.remove("DOWN")
                fooddirection.append("UP")
        
        if "LEFT" in fooddirection:
            food[0] -= 8
            if food[0] < 40:
                fooddirection.remove("LEFT")
                fooddirection.append("RIGHT")
        elif "RIGHT" in fooddirection:
            food[0] += 8
            if food[0] > 1240:
                fooddirection.remove("RIGHT")
                fooddirection.append("LEFT")
        
    def MakeBomb(number):
        global bombs
        for i in range(number):
            bombx = round(random.randint(15, 640), -1) * 2
            bomby = round(random.randint(15, 340), -1) * 2
            dimensionx = 150
            dimensiony = 150
            explodetimer = random.randint(4, 8)
            spawntimer = time.time()
            bomb = [bombx, bomby, dimensionx, dimensiony, explodetimer, spawntimer]
            bombs.append(bomb)
        return bombs
    
    def SpawnBullets():
        global bullets, snakehead
        bullets = []
        for i in range(30):
            bulletx = round(random.randint(605, 640), -1) * 2
            bullety = round(random.randint(15, 340), -1) * 2
            dimensionx = 20
            dimensiony = 20
            bullet = [bulletx, bullety, dimensionx, dimensiony]
            if pygame.Rect(bullet) != snakehead:
                bullets.append(bullet)      
        return bullets
    
    def HawkTuah():
        global spits
        spits = []
        for i in range(6):
            spitx = round(random.randint(15, 625), -1) * 2
            spity = round(random.randint(15, 205), -1) * 2
            radius = round(random.randint(40, 105), -1) * 2
            spit = [spitx, spity, radius]
            spits.append(spit)        
        return spits

    def BananaPeels():
        global bananas
        bananas = []
        for i in range(10):
            bananax = round(random.randint(15, 625), -1) * 2
            bananay = round(random.randint(15, 205), -1) * 2
            dimensionx = 80
            dimensiony = 80
            banana = [bananax, bananay, dimensionx, dimensiony]
            for otherbanana in bananas:
                if pygame.Rect(otherbanana).colliderect(pygame.Rect(banana)):
                    bananax = round(random.randint(15, 625), -1) * 2
                bananay = round(random.randint(15, 205), -1) * 2
                dimensionx = 80
                dimensiony = 80
                banana = [bananax, bananay, dimensionx, dimensiony]
            bananas.append(banana)        
        return bananas
            
    def Lava():
        global lavasplotches, snakehead
        lavasplotches = []
        for i in range(4):
            lavax = round(random.randint(15, 625), -1) * 2
            lavay = round(random.randint(15, 315), -1) * 2
            dimensionx = round(random.randint(90, 200), -1) * 2
            dimensiony = round(random.randint(90, 200), -1) * 2
            lavasplotch = pygame.Rect(lavax, lavay, dimensionx, dimensiony)
            if not lavasplotch.collidepoint((snakehead[0], snakehead[1])):
                lavasplotches.append(lavasplotch)
            
        return lavasplotches

    def SpotlightMove(spotlight, spotlightdirection):
        if "UP" in spotlightdirection:
            spotlight[1] -= 20
            if spotlight[1] < 40:
                spotlightdirection.remove("UP")
                spotlightdirection.append("DOWN")
        elif "DOWN" in spotlightdirection:
            spotlight[1] += 20
            if spotlight[1] > 660:
                spotlightdirection.remove("DOWN")
                spotlightdirection.append("UP")
        
        if "LEFT" in spotlightdirection:
            spotlight[0] -= 20
            if spotlight[0] < 40:
                spotlightdirection.remove("LEFT")
                spotlightdirection.append("RIGHT")
        elif "RIGHT" in spotlightdirection:
            spotlight[0] += 20
            if spotlight[0] > 1240:
                spotlightdirection.remove("RIGHT")
                spotlightdirection.append("LEFT")
    
    def CheckForSpotlight(spotlight, snakehead):
        corner = (spotlight[0] - 93, spotlight[1] - 93)
        
        spotlighthitbox = pygame.Rect(corner[0], corner[1], 186, 186)
        if spotlighthitbox.collidepoint((snakehead[0], snakehead[1])):
            return True
        else:
            return False 
        
    def WarpSnake():
        global snakehead, snake
        snakeheadx = round(random.randint(35, 595), -1) * 2
        snakeheady = round(random.randint(35, 295), -1) * 2
        
        snakehead = (snakeheadx, snakeheady, 20, 20)
        
        for snakesegment in snake:
            if snakesegment == pygame.Rect(snakehead[0], snakehead[1], 20, 20):
                Snake.WarpSnake()   
    
    def GetDate():
        currentdate = datetime.now()
        formatteddate = currentdate.strftime("%B %d, %Y")
        return formatteddate  
             
    def HighScoreStuff(score):
        global name, finaltime, disaster, deathmessage
        import json     
        with open('highscores.json', 'r') as file:
            highscores = json.load(file)

        for oldscore in highscores:
            if oldscore['name'] == 'test':
                highscores.remove(score)
                
        highestscore = False
        alreadythere = False
        
        highscoreentry = {
                "name" : name,
                "score" : score
            }

        if len(highscores) > 0:
            for oldscore in highscores:
                if oldscore['name'].upper() == highscoreentry['name'].upper():
                    highscores.remove(oldscore)
                    if oldscore['high-score'] < score:
                        print('NEW HIGH SCORE! NICE WORK!')
                        highestscore == True
                        newhighscore = highscoreentry['score']
                    else:
                        newhighscore = oldscore['high-score']  
                else:
                    newhighscore = score       
        else:
            newhighscore = score
    
        newentry = {
                "name" : name.upper(),
                "high-score" : newhighscore,
                "date" : Snake.GetDate(),
                "time" : finaltime,
                "disasters-survived" : int(score/5) - 1,
                "died-to" : deathmessage
            }       

        if highestscore == True or alreadythere == False:
            highscores.append(newentry)
            
        with open("highscores.json", "w") as file:
            json.dump(highscores, file, indent=2)
            
    def TitleScreen():
        global titlescreen, running, name
        titlescreen = True
        typing = False
        canbepressed = False
        currentstring = ""
        
        while titlescreen:
            screen.fill((17, 22, 35))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quit()
            
            titlerect = pygame.Rect(20, 20, 1240, 180)
            pygame.draw.rect(screen, (10, 13, 25), titlerect)
            titlefont = pygame.font.SysFont(None, 170, bold=True)
            titletext = titlefont.render("SNAKE,                2.", True, (255, 255, 255))
            titlesurface = titletext.get_rect(center=titlerect.center)
            screen.blit(titletext, titlesurface)
            
            buttonfont = pygame.font.SysFont(None, 130, bold=True)
            mousepos = pygame.mouse.get_pos()
            
            startbuttonrect = pygame.Rect(120, 240, 1040, 150)
            if startbuttonrect.collidepoint(mousepos):
                color = (55, 75, 110)
            else:
                color = (30, 42, 80)
            pygame.draw.rect(screen, color, startbuttonrect)
            
            starttext = buttonfont.render("START GAME", True, (255, 255, 255))
            startsurface = starttext.get_rect(center=startbuttonrect.center)
            screen.blit(starttext, startsurface)
            
            typebox = pygame.Rect(120, 420, 1040, 200)
            if typing == True:
                typecolor = (45, 60, 95)
            elif typing == False:
                typecolor = (30, 42, 80)
            pygame.draw.rect(screen, typecolor, typebox)
            
            for event in events:
                if typecolor[0] == 30 and event.type == pygame.MOUSEBUTTONDOWN:
                    typing = True
                elif typecolor[0] == 45 and event.type == pygame.MOUSEBUTTONDOWN:
                    typing = False
                    
            if typing == True:
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            currentstring += "A"
                        elif event.key == pygame.K_b:
                            currentstring += "B"
                        elif event.key == pygame.K_c:
                            currentstring += "C"
                        elif event.key == pygame.K_d:
                            currentstring += "D"
                        elif event.key == pygame.K_e:
                            currentstring += "E"
                        elif event.key == pygame.K_f:
                            currentstring += "F"
                        elif event.key == pygame.K_g:
                            currentstring += "G"
                        elif event.key == pygame.K_h:
                            currentstring += "H"
                        elif event.key == pygame.K_i:
                            currentstring += "I"
                        elif event.key == pygame.K_j:
                            currentstring += "J"
                        elif event.key == pygame.K_k:
                            currentstring += "K"
                        elif event.key == pygame.K_l:
                            currentstring += "L"
                        elif event.key == pygame.K_m:
                            currentstring += "M"
                        elif event.key == pygame.K_n:
                            currentstring += "N"
                        elif event.key == pygame.K_o:
                            currentstring += "O"
                        elif event.key == pygame.K_p:
                            currentstring += "P"
                        elif event.key == pygame.K_q:
                            currentstring += "Q"
                        elif event.key == pygame.K_r:
                            currentstring += "R"
                        elif event.key == pygame.K_s:
                            currentstring += "S"
                        elif event.key == pygame.K_t:
                            currentstring += "T"
                        elif event.key == pygame.K_u:
                            currentstring += "U"
                        elif event.key == pygame.K_v:
                            currentstring += "V"
                        elif event.key == pygame.K_w:
                            currentstring += "W"
                        elif event.key == pygame.K_x:
                            currentstring += "X"
                        elif event.key == pygame.K_y:
                            currentstring += "Y"
                        elif event.key == pygame.K_z:
                            currentstring += "Z"
                        elif event.key == pygame.K_BACKSPACE:
                            currentstring = currentstring[:-1]
                        elif event.key == pygame.K_2:
                            currentstring += "2"
                        elif event.key == pygame.K_RETURN and len(currentstring) > 0:
                            canbepressed = True
                            typing = False
                            name = currentstring
                    
            typingtext = buttonfont.render(currentstring, True, (255, 255, 255))
            typingsurface = typingtext.get_rect(center=typebox.center)
            screen.blit(typingtext, typingsurface)               
            
            for event in events:
                if color[0] == 55 and event.type == pygame.MOUSEBUTTONDOWN and canbepressed == True:
                    Snake.Screen()
     
            pygame.display.update()

Snake.TitleScreen()