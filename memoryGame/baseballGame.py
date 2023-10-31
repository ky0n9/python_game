import pygame
import random
#import font
#import color

def run_game():
    #파이게임 초기화
    pygame.init()
    
    #화면 크기 설정
    Display = pygame.display.set_mode((800,600))
    
    # 게임 타이틀 설정
    pygame.display.set_caption("숫자 야구")
    
    # 배경 이미지 로드
    background_image = pygame.image.load('baseballGround.jpg')
    background_rect = background_image.get_rect()

    # 폰트 설정
    font = pygame.font.SysFont("malgungothic", 36)
    title_font = pygame.font.SysFont("malgungothic", 62)
    font_color = (0, 0, 0) # 폰트 색상 설정
    
    #게임 제목 설정
    gametitle_text = title_font.render("숫자 야구", True, (0, 0, 0))

    # 난수로 4자리 비밀 번호 생성
    def generate_secret_number():
        digits = [str(i) for i in range(10)]
        random.shuffle(digits)
        secret_number = ''.join(digits[:4])
        return secret_number

    secret_number = generate_secret_number()
    attempts = 0

    # 사용자 입력을 저장할 변수
    user_input = ""
    
    # 게임 결과를 저장할 변수
    result_text = ""

    # 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    # 사용자 입력 확인
                    attempts += 1
                    if len(user_input) != 4 or not user_input.isdigit():
                        user_input = ""
                        continue

                    # 스트라이크와 볼 계산
                    strike, ball = 0, 0
                    for i in range(4):
                        if user_input[i] == secret_number[i]:
                            strike += 1
                        elif user_input[i] in secret_number:
                            ball += 1

                    # 게임 결과 확인
                    if strike == 4:
                        result_text = f"홈런! {attempts} 번만에 맞추셨습니다."
                        running = False
                    elif strike == 0 and ball == 0:
                        result_text = "아웃!"
                    else:
                        result_text = f"{strike} 스트라이크, {ball} 볼"
                        
                    # 입력 초기화
                    user_input = ""
                elif event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                    # 숫자 키 입력 처리
                    user_input += event.unicode

        # 화면 지우기
        Display.fill((255, 255, 255))

        # 게임 상태 표시
        attempts_text = font.render(f"시도 횟수: {attempts}", True, font_color)
        user_input_text = font.render(f"입력한 답: {user_input}", True, font_color)
        result_surface = font.render(result_text, True, font_color)
        
        # 배경 이미지 그리기
        Display.blit(background_image, background_rect)
        
        Display.blit(gametitle_text, (270, 50))
        Display.blit(attempts_text, (290, 190))
        Display.blit(user_input_text, (260, 300))
        Display.blit(result_surface, (240, 410))
                
        # 화면 업데이트
        pygame.display.update()

    # 게임 종료
    pygame.quit()