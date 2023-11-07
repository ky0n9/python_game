import pygame
import random

def run_game():
    def random_num():
        random_number = random.randint(1, 99)
        return random_number


    BLCAK =(0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    BLUE = (0,0,255)
    screen_width = 800
    screen_height = 600
    Display = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("업다운 게임")

    image = pygame.image.load("Arrow-100.png")
    image = pygame.transform.scale(image, (100, 100))
    image_rect = image.get_rect()
    image_rect.topleft = (5200, 1000)

    background = pygame.image.load("updown-background.png")
    background = pygame.transform.scale(background,(1200,1200))
    background_rect = background.get_rect()

    font = pygame.font.SysFont("malgungothic", 36)
    title_font = pygame.font.SysFont("malgungothic", 70)
    result_font = pygame.font.SysFont("malgungothic", 80)
    result_font2 = pygame.font.SysFont("malgungothic", 65)
    # font = pygame.font.Font("/Users/junggonlee/Downloads/13151B114AE7E3A025/malgunbd.ttf",36)
    # title_font = pygame.font.Font("/Users/junggonlee/Downloads/13151B114AE7E3A025/malgunbd.ttf", 70)
    # result_font = pygame.font.Font("/Users/junggonlee/Downloads/13151B114AE7E3A025/malgunbd.ttf", 80)
    # result_font2 = pygame.font.Font("/Users/junggonlee/Downloads/13151B114AE7E3A025/malgunbd.ttf", 65)
    result_text = font.render("", True, BLCAK)
    gametitle_text = title_font.render("업다운 게임", True, (0, 0, 0))
    random_code = random_num()
    input_num = ""
    trynum = 10

    up_text=font.render("",False,BLCAK)
    down_text=font.render("",False,BLCAK)
    rotated_image=pygame.transform.rotate(image, -90)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    # 백스페이스 키를 눌렀을 때
                    input_num = input_num[:-1]
                elif event.key == pygame.K_RETURN:
                    trynum -= 1
                    if  trynum < 1:
                        Display.fill(WHITE)
                        image_rect.topleft = (52000, 52000)
                        input_num_text = font.render("", True, (BLCAK))
                        up_text = font.render("", True, BLCAK)
                        down_text = font.render("", True, BLCAK)
                        result_text = result_font.render("GAME OVER",True,BLCAK)
                    else:
                        if int(input_num) == random_code:
                            Display.fill(WHITE)
                            result_text = result_font2.render(f"축하 합니다 정답입니다!",True,BLCAK)
                            image_rect.topleft = (52000, 52000)
                            input_num_text = font.render("", True, (BLCAK))
                            up_text = font.render("", True, BLCAK)
                            down_text = font.render("", True, BLCAK)
                            pygame.display.update()
                            break
                        elif int(input_num) < random_code:
                            input_num_text = font.render("", True, (BLCAK))
                            up_text = font.render("UP",True,BLCAK)
                            down_text = font.render("",True,BLCAK)
                            image_rect.topleft = (520, 150)
                            rotated_image = pygame.transform.rotate(image,90)
                            rotated_image.fill(BLUE, special_flags=pygame.BLEND_ADD)
                        elif int(input_num) > random_code:
                            input_num_text = font.render("", True, (BLCAK))
                            up_text =font.render("",True,BLCAK)
                            down_text = font.render("DOWN",True,BLCAK)
                            image_rect.topleft = (520, 300)
                            rotated_image = pygame.transform.rotate(image, -90)
                            rotated_image.fill(RED, special_flags=pygame.BLEND_ADD)
                elif event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                    # 숫자 키 입력 처리
                    input_num += event.unicode


        Display.fill((WHITE))

        trynum_text = font.render(f"남은 시도 횟수{trynum}", True, (BLCAK))
        input_num_text = font.render(f"입력한 답: {input_num}", True, (BLCAK))

        Display.blit(background, background_rect)
        Display.blit(gametitle_text, (220, 50))
        Display.blit(trynum_text, (260, 140))
        Display.blit(input_num_text,(250,250))
        Display.blit(result_text,(160 ,350))
        Display.blit(up_text,(540,260))
        Display.blit(down_text,(525,400))
        Display.blit(rotated_image, image_rect)
        pygame.display.update()

    pygame.quit()
