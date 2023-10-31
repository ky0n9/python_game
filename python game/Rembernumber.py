import pygame
import random

class RembernumberGame:
    def __init__(self, screen):
        self.screen = screen
        self.secret_number = self.generate_secret_number()
        self.max_attempts = 5
        self.attempts = 0
        self.reset_game()
        self.font = pygame.font.Font(None, 36)

    def generate_secret_number(self):
        return [random.randint(0, 9) for _ in range(4)]

    def reset_game(self):
        self.attempts = 0
        self.guess = [0, 0, 0, 0]
        self.result_message = None

    def check_guess(self, guess):
        self.attempts += 1

        if guess == self.secret_number:
            return "정답입니다!"
        elif self.attempts >= self.max_attempts:
            return f"게임 오버! 정답은 {self.secret_number[0]}{self.secret_number[1]}{self.secret_number[2]}{self.secret_number[3]}"
        else:
            return "틀렸습니다. 다시 시도하세요."

    def draw(self):
        self.screen.fill((20, 184, 20))

        if self.result_message:
            text = self.font.render(self.result_message, True, (255, 255, 255))
            self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 50))
        else:
            input_text = self.font.render(f"시도: {self.attempts}/{self.max_attempts}", True, (255, 255, 255))
            self.screen.blit(input_text, (50, 50))

            for i in range(4):
                digit = str(self.guess[i])
                pygame.draw.rect(self.screen, (255, 255, 255), (100 + 60 * i, 100, 40, 40))
                text = self.font.render(digit, True, (0, 0, 0))
                self.screen.blit(text, (120 + 60 * i, 110))

        pygame.display.flip()

    def handle_event(self, event):
        if not self.result_message:
            if event.type == pygame.KEYDOWN:
                if pygame.K_0 <= event.key <= pygame.K_9:
                    digit = event.key - pygame.K_0
                    self.guess[self.attempts % 4] = digit
                elif event.key == pygame.K_RETURN:
                    result = self.check_guess(self.guess)
                    self.result_message = result
                elif event.key == pygame.K_BACKSPACE:
                    self.guess[self.attempts % 4] = 0
                    if self.attempts > 0:
                        self.attempts -= 1

def main():
    pygame.init()

    # 화면 설정
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("숫자 기억 게임")

    # 게임 변수
    rembernumber_game = RembernumberGame(screen)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                rembernumber_game.handle_event(event)

        rembernumber_game.draw()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
