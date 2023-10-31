import pygame
import random
import color
import font


class UpdownGame:
    def __init__(self, screen):
        self.screen = screen
        pygame.display.set_caption("업 다운 게임")

        # 게임 변수
        self.target_number = random.randint(1, 100)  # 1부터 100 사이의 숫자 선택
        self.guess = None
        self.attempts = 0

        # 폰트 설정
        self.font = pygame.font.SysFont('NotoSansKR', 36)
        self.result_font = pygame.font.SysFont('NotoSansKR', 24)

    def draw(self):
        self.screen.fill(color.WHITE)

        title_text = self.font.render("Up and Down 게임", True, (255, 255, 255))
        self.screen.blit(title_text, (50, 50))

        if self.guess is not None:
            guess_text = self.result_font.render(f"당신의 추측: {self.guess}", True, (255, 255, 255))
            self.screen.blit(guess_text, (50, 150))

            if self.guess < self.target_number:
                hint_text = self.result_font.render("Up", True, (255, 0, 0))
            elif self.guess > self.target_number:
                hint_text = self.result_font.render("Down", True, (0, 0, 255))
            else:
                hint_text = self.result_font.render("정답!", True, (0, 255, 0))

            self.screen.blit(hint_text, (50, 200))

        attempts_text = self.result_font.render(f"시도 횟수: {self.attempts}", True, (255, 255, 255))
        self.screen.blit(attempts_text, (50, 250))

        pygame.display.flip()

    def main(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_RETURN:
                        if self.guess is not None:
                            self.attempts += 1
                            if self.guess == self.target_number:
                                self.draw()
                            self.guess = None
                        else:
                            # 플레이어의 추측 입력
                            try:
                                self.guess = int(input("추측 숫자를 입력하세요: "))
                                self.draw()
                            except ValueError:
                                pass  # 정수가 아닌 입력 무시

        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    updown_game = UpdownGame(screen)
    updown_game.main()
