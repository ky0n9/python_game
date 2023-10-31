import pygame

# 폰트 초기화
pygame.font.init()

# 폰트 파일 경로
FONT_FILE_PATH_Variable = "/Users/junggonlee/Library/Fonts/NotoSansKR-VariableFont_wght.ttf"

# 다양한 크기의 폰트 생성
FONT_SIZE_SMALL = 20
FONT_SIZE_MEDIUM = 33
FONT_SIZE_LARGE = 48

variablefont_small = pygame.font.Font(FONT_FILE_PATH_Variable, FONT_SIZE_SMALL)
variablefont_medium = pygame.font.Font(FONT_FILE_PATH_Variable, FONT_SIZE_MEDIUM)
variablefont_large = pygame.font.Font(FONT_FILE_PATH_Variable, FONT_SIZE_LARGE)