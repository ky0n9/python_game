import pygame
import sys
import random
import time
import re

from pygame.locals import *

def run_game():
    #색상 정의
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    GREY = (200,200,200)
    LEFT_CLICK = (1,0,0)
    RIGHT_CLICK = (0,0,1)
    
    #파이게임 초기화
    pygame.init()

    # 게임 타이틀 설정
    pygame.display.set_caption("행맨")
    
    # 배경 이미지 로드
    background_image = pygame.image.load('western.jpg')
    background_rect = background_image.get_rect()

    #32 bit display
    Display = pygame.display.set_mode((500,500))

    Easy = ["BELL","STAR","PICNIC", "PIE","HAT","HEART","FLAG"]

    Medium = ["CARPET","POPCORN","SEAFOOD","DOORBELL","COWBOY",\
            "INSIDE","OUTSIDE","RAINBOW","POSTMAN","WATERMELON",\
            "FOOTBALL","STRAWBERRY"]

    Hard = ["BACKGROUND","BOOKWORM","FIREFIGHTER","SOUNDPROOF","THUNDERSTORM",\
            "CAMPGROUND","FRIENDSHIP","SKYSCRAPER","SUPERHUMAN","FINGERPRINT",\
            "MASTERPIECE", "LOUDSPEAKER"]

    Color = ["BLACK","WHITE","RED","GREEN","BLUE","GREY"]

    #Font = pygame.font.Font("/Users/junggonlee/Projects/python_game/python game/Typo_DabangguB.ttf",33)
    #Font2 = pygame.font.Font("/Users/junggonlee/Projects/python_game/python game/Typo_DabangguB.ttf",20)
    Font = pygame.font.SysFont("malgungothic",33)
    Font2 = pygame.font.SysFont("malgungothic",20)

    Display.fill(WHITE)

    def randomNum(choice):
        RandomNum = 0
        if choice == 1:
            RandomNum == random.randint(0,len(Easy)-1)

        elif choice == 2:
            RandomNum = random.randint(0,len(Medium)-1)

        elif choice == 3:
            RandomNum = random.randint(0,len(Hard)-1)

        elif choice == 4:
            RandomNum =  random.randint(0,len(Color)-1)# as elements of color is 0,1,2,3,4
            
        return RandomNum

    def List(number,choice):
        if (choice == 1):
            Word = Easy[number]

        elif (choice == 2):
            Word = Medium[number]

        elif (choice == 3):
            Word = Hard[number]

        elif (choice == 4):
            Word = Color[number]
            
        return Word

    # 배경 이미지 그리기
    Display.blit(background_image, background_rect)

    #기본 행맨 그림
    def Hangman(condition):
        if (condition == 0):
            pygame.draw.line(Display, GREY, (10,400),(300,400),8)  #막대1
            pygame.draw.line(Display, GREY, (50,50),(50,400),8)    #막대2
            pygame.draw.line(Display, GREY, (50,60),(250,60),8)    #막대3
            pygame.draw.line(Display, GREY, (150,60),(150,100),8)  #로프
            pygame.draw.circle(Display, GREY, (150,150),50,8)      #머리
            pygame.draw.line(Display, GREY, (150,200),(150,300),8) #몸
            pygame.draw.line(Display, GREY, (150,210),(100,250),8) #왼팔
            pygame.draw.line(Display, GREY, (150,210),(200,250),8) #오른팔
            pygame.draw.line(Display, GREY, (150,300),(100,350),8) #왼다리
            pygame.draw.line(Display, GREY, (150,300),(200,350),8) #오른다리

    #시도 횟수가 증가할 때 마다 하나씩 검게 칠함
        elif (condition == 1):
            pygame.draw.line(Display, BLACK, (10,400),(300,400),8) #막대1
        elif (condition == 2):
            pygame.draw.line(Display, BLACK, (50,50),(50,400),8)   #막대2
        elif (condition == 3):
            pygame.draw.line(Display, BLACK, (50,60),(250,60),8)   #막대3
        elif (condition == 4):
            pygame.draw.line(Display, BLACK, (150,60),(150,100),8) #로프
        elif (condition == 5):
            pygame.draw.circle(Display, BLACK, (150,150),50,8)     #머리
        elif (condition == 6):
            pygame.draw.line(Display, BLACK, (150,200),(150,300),8)#몸
        elif (condition == 7):
            pygame.draw.line(Display, BLACK, (150,210),(100,250),8)#왼팔
        elif (condition == 8):
            pygame.draw.line(Display, BLACK, (150,210),(200,250),8)#오른팔
        elif (condition == 9):
            pygame.draw.line(Display, BLACK, (150,300),(100,350),8)#왼다리
        elif (condition == 10):
            pygame.draw.line(Display, BLACK, (150,300),(200,350),8)#오른다리

        #게임 오버 시 행맨
        elif (condition == 11):
            pygame.draw.line(Display, BLUE, (10,400),(300,400),8)  #막대1
            pygame.draw.line(Display, BLUE, (50,50),(50,400),8)    #막대2
            pygame.draw.line(Display, BLUE, (50,60),(250,60),8)    #막대3
            pygame.draw.line(Display, BLUE, (150,60),(150,100),8)  #로프
            pygame.draw.circle(Display, BLUE, (150,150),50,8)      #머리
            pygame.draw.line(Display, BLUE, (150,200),(150,300),8) #몸
            pygame.draw.line(Display, BLUE, (150,210),(100,250),8) #왼팔
            pygame.draw.line(Display, BLUE, (150,210),(200,250),8) #오른팔
            pygame.draw.line(Display, BLUE, (150,300),(100,350),8) #왼다리
            pygame.draw.line(Display, BLUE, (150,300),(200,350),8) #오른다리

    #메인화면 행맨
    def PreHangMan():
        pygame.draw.line(Display, BLUE, (10,400),(190,400),8)      #막대1
        pygame.draw.line(Display, BLUE, (30,90),(30,400),8)        #막대2
        pygame.draw.line(Display, BLUE, (30,100),(160,100),8)      #막대3
        pygame.draw.line(Display, BLUE, (100,100),(100,120),8)     #로프
        pygame.draw.circle(Display, BLUE, (100,170),50,8)          #머리
        pygame.draw.line(Display, BLUE, (100,220),(100,320),8)     #몸
        pygame.draw.line(Display, BLUE, (100,230),(50,270),8)      #왼팔
        pygame.draw.line(Display, BLUE, (100,230),(150,270),8)     #오른팔
        pygame.draw.line(Display, BLUE, (100,320),(50,360),8)      #왼다리
        pygame.draw.line(Display, BLUE, (100,320),(150,360),8)     #오른다리
            
    #메인화면
    def StartScreen():
        Display.blit(pygame.font.SysFont("malgungothic",40).render("행 맨",True,BLACK), (210,20))
        Display.blit(Font.render("난이도",True,BLACK), (290,130))
        Display.blit(Font2.render("1 - 쉬움",True,BLACK), (290,200))
        Display.blit(Font2.render("2 - 보통",True,BLACK), (290,250))
        Display.blit(Font2.render("3 - 어려움",True,BLACK), (290,300))
        #Display.blit(Font2.render("4 - 색깔",True,GREY), (200,350))
            
    def main():
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        RED = (255,0,0)
        GREEN = (0,255,0)
        BLUE = (0,0,255)

        GREY = (200,200,200)

        TheChoice = 0
            
        StartScreen()
            
        PreHangMan()
        
        FirstCondi = True
        while FirstCondi:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    #print(FirstCondi)
                    if (event.key == K_1) or (event.key == 257):#257 is 1 in numpad
                        TheChoice = 1
                        FirstCondi = False
                        break
                    elif event.key == K_2 or event.key == 258:#258 is 2 in numpad
                        TheChoice = 2
                        FirstCondi = False
                        break
                    elif event.key == K_3 or event.key == 259:#259 is 3 in numpad
                        TheChoice = 3
                        FirstCondi = False
                        break
                    elif event.key == K_4 or event.key == 260:#260 is 4 in numpad
                        TheChoice = 4
                        FirstCondi = False
                        break

                #마우스 클릭 이벤트
                elif event.type == MOUSEBUTTONDOWN:                    
                    #쉬움
                    if (pygame.mouse.get_pos()[0] > 290 and\
                        pygame.mouse.get_pos()[1] > 200 and\
                        pygame.mouse.get_pos()[0] < 370 and\
                        pygame.mouse.get_pos()[1] < 215):
                        TheChoice = 1
                        FirstCondi = False
                        break
                    #보통
                    elif (pygame.mouse.get_pos()[0] > 290 and\
                        pygame.mouse.get_pos()[1] > 250 and\
                        pygame.mouse.get_pos()[0] < 370 and\
                        pygame.mouse.get_pos()[1] < 265):
                        TheChoice = 2
                        FirstCondi = False
                        break
                    #어려움
                    elif (pygame.mouse.get_pos()[0] > 290 and\
                        pygame.mouse.get_pos()[1] > 300 and\
                        pygame.mouse.get_pos()[0] < 390 and\
                        pygame.mouse.get_pos()[1] < 315):
                        TheChoice = 3
                        FirstCondi = False
                        break
                    
            if (TheChoice!= 0):
                Display.fill(WHITE)
                
            pygame.display.update()
            pygame.time.Clock().tick(30) #30fps        
        
        #난수, 랜덤 단어 생성이 잘 되는지 확인
        TheNum = randomNum(TheChoice)
        TheWord = List(TheNum, TheChoice)

        EmptyList = []

        for i in range(len(TheWord)):
            EmptyList.append('-')

        Hidden = Font.render("".join(EmptyList),True,BLACK)
        HiddenRect = Hidden.get_rect()
        HiddenRect.center = (350,250)
        Display.blit(Hidden,HiddenRect)
        
        #컨디션 즉 시도 횟수가 10이 되면 게임 종료
        Condition = 0;

        #이기거나 게임 오버되면 종료
        Off = 0 

        TheTime = 0
        Start = time.time() #현재 시간

        Display.blit(Font2.render("Time(s):",True,BLACK),(300,10))

        LastKeyPressed = ""

        Display.blit(pygame.font.SysFont("malgungothic",15).render("게임을 종료하려면 0을 누르세요.",True,BLACK),(20,10))
        
        while True:
            Hangman(Condition)
            End = time.time()
            if (int(End) - int(Start) == 1):
                pygame.draw.rect(Display,WHITE,(385,0,100,50))
                TheTime = TheTime + 1
                Timer = Font2.render(str(TheTime),True,BLACK)
                Display.blit(Timer, (400,10))
                Start = time.time()
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == KEYDOWN:                
                    #키보드 이벤트
                    LastKeyPressed = event.key
                    pygame.draw.rect(Display,WHITE,(220,200,280,100))
                    pygame.draw.rect(Display,WHITE,(260,50,200,100))
                    UserInput = event.key
                    if re.search("[a-z]",chr(event.key)):
                        if ((chr(event.key).upper() in TheWord) or (chr(event.key).lower() in TheWord)):
                            for i in range(len(TheWord)):
                                if ((TheWord[i] == (chr(event.key)).upper()) or (TheWord[i] == (chr(event.key)).lower())):
                                    EmptyList[i] = TheWord[i]
                        else:
                            Condition = Condition + 1

                        Hidden = Font.render("".join(EmptyList),True,BLACK)
                        HiddenRect = Hidden.get_rect()
                        HiddenRect.center = (350,250)
                        Display.blit(Hidden,HiddenRect)                    
                    else:
                        if (event.key == K_0 or event.key == 256): #256은 숫자패드의 0
                            Display.blit(Font.render("EXIT?",True,RED),(340,220))
                            Display.blit(Font2.render("Yes",True,BLUE),(340,270))
                            Display.blit(Font2.render("No",True,BLUE),(415,270))
                        else:
                            Input = Font2.render("INVALID INPUT!!!",True,RED)
                            InputRect = Input.get_rect()
                            InputRect.center = (350,100)
                            Display.blit(Input, InputRect)
                            Display.blit(Hidden,HiddenRect)                        
                elif event.type == KEYUP:
                    pygame.draw.rect(Display,WHITE,(260,50,200,100))                     
                elif event.type == MOUSEBUTTONDOWN:                    
                    if (LastKeyPressed == K_0 or LastKeyPressed == 256): #256은 숫자패드의 0
                        if (pygame.mouse.get_pressed() == LEFT_CLICK):
                            if (pygame.mouse.get_pos()[0] > 340 and\
                                pygame.mouse.get_pos()[1] > 270 and\
                                pygame.mouse.get_pos()[0] < 385 and\
                                pygame.mouse.get_pos()[1] < 285):
                                pygame.draw.rect(Display,WHITE,(340,270,35,25)) #hide yes
                                Display.blit(Font2.render("Yes",True,GREEN),(340,270))
                            elif (pygame.mouse.get_pos()[0] > 415 and\
                                pygame.mouse.get_pos()[1] > 270 and\
                                pygame.mouse.get_pos()[0] < 450 and\
                                pygame.mouse.get_pos()[1] < 285):
                                pygame.draw.rect(Display,WHITE,(415,270,35,25))
                                Display.blit(Font2.render("No",True,GREEN),(415,270))                            
                elif event.type == MOUSEBUTTONUP:
                    if (LastKeyPressed == K_0 or LastKeyPressed == 256): #256은 숫자패드의 0
                        if (pygame.mouse.get_pos()[0] > 340 and\
                        pygame.mouse.get_pos()[1] > 270 and\
                        pygame.mouse.get_pos()[0] < 385 and\
                        pygame.mouse.get_pos()[1] < 285):
                            
                            #게임 종료
                            pygame.quit()
                            sys.exit()         

                        elif (pygame.mouse.get_pos()[0] > 415 and\
                            pygame.mouse.get_pos()[1] > 270 and\
                            pygame.mouse.get_pos()[0] < 450 and\
                            pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(Display,WHITE,(415,270,35,25))
                            Display.blit(Font2.render("No",True,GREEN),(415,270))
                            pygame.draw.rect(Display,WHITE,(300,200,200,100))

                            Hidden = Font.render("".join(EmptyList),True,BLACK)
                            HiddenRect = Hidden.get_rect()
                            HiddenRect.center = (400,250)
                            Display.blit(Hidden,HiddenRect)

                            LastKeyPressed = ""                
                            
                        else:
                            pygame.draw.rect(Display,WHITE,(340,270,35,25))
                            Display.blit(Font2.render("Yes",True,BLUE),(340,270))
                            pygame.draw.rect(Display,WHITE,(415,270,35,25))
                            Display.blit(Font2.render("No",True,BLUE),(415,270))

            if (Condition == 10):
                Display.fill(WHITE)
                Hangman(Condition+1)
                Over = Font2.render("게임 오버!!!",True,RED)
                OverRect = Over.get_rect()
                OverRect.center = (400,250)
                Display.blit(Over,OverRect)
                Off = 1

            elif (TheWord == "".join(EmptyList)):
                Display.fill(WHITE)
                Cong = Font.render("게임 승리!!!",True,GREEN)
                CongRect = Cong.get_rect()
                CongRect.center = (250,220)
                Display.blit(Cong,CongRect)
                
                Word = Font2.render("정답은 :",True,BLACK)
                WordRect = Word.get_rect()
                WordRect.center = (250,250)
                Display.blit(Word,WordRect)

                Word2 = Font.render(TheWord,True,BLACK)
                Word2Rect = Word2.get_rect()
                Word2Rect.center = (250,285)
                Display.blit(Word2,Word2Rect)
                
                Off = 1         

            pygame.display.update()
            pygame.time.Clock().tick(30) #30fps
            
            if (Off == 1):
                #5초 대기
                time.sleep(5)
                #게임 종료
                pygame.quit()
                sys.exit()

    main()