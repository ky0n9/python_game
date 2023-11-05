import pygame
from Baseball import BaseballGame
from Hangman import HangmanGame
from Updown import UpdownGame
from Rembernumber import RembernumberGame

pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("메인 메뉴")

# 게임 변수
current_game = None  # 현재 실행 중인 게임을 저장할 변수
menu_items = ["숫자 야구", "행맨", "숫자 맞추기", "업다운게임", "게임 종료"]
selected_item = 0  # 현재 선택된 메뉴 아이템 인덱스

# 폰트 설정
font = pygame.font.Font('/Users/junggonlee/Library/Fonts/NotoSansKR-VariableFont_wght.ttf', 36)

# 화면에 타이틀 텍스트 그리기
title_font = pygame.font.Font('/Users/junggonlee/Library/Fonts/NotoSansKR-VariableFont_wght.ttf', 48)
gametitle_text = title_font.render("치매 예방 게임", True, (255, 255, 255))
title_rect = gametitle_text.get_rect()
title_rect.center = (screen_width // 2, 100)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item == 0:
                    current_game = BaseballGame(screen)
                elif selected_item == 1:
                    current_game = HangmanGame(screen)
                elif selected_item == 2:
                    current_game = RembernumberGame(screen)
                elif selected_item == 3:
                    current_game = UpdownGame(screen)
                elif selected_item == 4:
                    running = False

    # 게임 화면 업데이트
    if current_game:
        current_game.main()  # 현재 게임 실행

    screen.fill((20, 184, 20))

    # 게임 타이틀 그리기
    screen.blit(gametitle_text, title_rect)

    # 모든 메뉴 항목의 텍스트 중에서 가장 긴 텍스트를 찾기
    max_text_width = max([font.size(item)[0] for item in menu_items])

    for i, item in enumerate(menu_items):
        text = font.render(item, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen_width // 2, 200 + i * (text_rect.height + 10))

        # 테두리 상자의 위치를 가장 긴 텍스트에 맞추기
        border_rect = pygame.Rect((text_rect.centerx - max_text_width // 2, text_rect.centery - text_rect.height // 2), (max_text_width, text_rect.height))
        if i == selected_item:
            pygame.draw.rect(screen, (255, 255, 255), border_rect, 2)

        screen.blit(text, text_rect)

    pygame.display.flip()

# 게임 종료
pygame.quit()
