import pygame
import random
import font
import color

class BaseballGame:
    def __init__(self, screen):
        self.screen = screen
        self.secret_number = self.generate_secret_number()
        self.max_attempts = 5
        self.attempts = 0
        self.reset_game()
        self.font = font.variablefont_large
        self.font2 = font.variablefont_medium
        self.guess_colors = [color.WHITE, color.WHITE, color.WHITE]
        self.game_over = False
        self.result_message = font.variablefont_small

    def generate_secret_number(self):
        return random.sample(range(1, 10), 3)


    def reset_game(self):
        self.attempts = 0
        self.guess = [0, 0, 0]
        self.result_message = ""
        self.guess_colors = [color.WHITE, color.WHITE, color.WHITE]

    def check_guess(self, guess):
        self.attempts += 1
        correct_digits = 0
        correct_positions = 0

        for i in range(3):
            if guess[i] == self.secret_number[i]:
                correct_positions += 1
            elif guess[i] in self.secret_number:
                correct_digits += 1

        if correct_positions == 3:
            self.guess_colors = [color.GREEN, color.GREEN, color.GREEN]
            self.result_message = "정답입니다!"
        elif self.attempts >= self.max_attempts:
            self.guess_colors = [color.RED, color.RED, color.RED]
            self.result_message = f"게임 오버! 정답은 {self.secret_number[0]}{self.secret_number[1]}{self.secret_number[2]}"
        else:
            for i in range(3):
                self.guess_colors[i] = color.GREEN if guess[i] == self.secret_number[i] else color.RED
            self.result_message = f"{correct_positions}개 숫자와 위치가 일치, {correct_digits}개 숫자만 일치"

        self.game_over = True

    def draw(self):
        self.screen.fill(color.WHITE)

            
        for i in range(3):
            digit = str(self.guess[i])
            x = 300 + 60 * i
            y = 100
            width = 50
            height = 40

            pygame.draw.rect(self.screen, self.guess_colors[i], (x, y, width, height))
            text = self.font.render(digit, True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (x + width // 2, y + height // 2)
            self.screen.blit(text, text_rect)

        input_text = self.font2.render(f"시도: {self.attempts}/{self.max_attempts}", True, color.BLACK)
        input_text_rect = input_text.get_rect()
        input_text_rect.center = (self.screen.get_width() // 2, 50)
        self.screen.blit(input_text, input_text_rect)

        if self.game_over:
            text = self.font.render(self.result_message, True, color.BLACK)
            text_rect = text.get_rect()
            text_rect.center = (self.screen.get_width() // 2, 200)
            self.screen.blit(text, text_rect)

        pygame.display.flip()

    def handle_event(self, event):
        if not self.game_over:
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    digit = event.key - pygame.K_0
                    self.guess[self.attempts % 3] = digit
                elif event.key == pygame.K_RETURN:
                    self.check_guess(self.guess)
                elif event.key == pygame.K_BACKSPACE:
                    self.guess[self.attempts % 3] = 0
                    if self.attempts > 0:
                        self.attempts -= 1

    def main(self):
        pygame.init()

        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("숫자 야구 게임")

        baseball_game = BaseballGame(screen)
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    baseball_game.handle_event(event)

            baseball_game.draw()
            clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    BaseballGame().main()

