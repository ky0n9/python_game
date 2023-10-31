import pygame
import sys
import random
import time
import re
from pygame.locals import *
import color
import font


class HangmanGame:
    def __init__(self, screen):  # screen을 인자로 받도록 수정
        pygame.init()
        pygame.display.set_caption("행맨")
        self.screen = screen
        self.display = self.screen  # 화면 설정을 받은 screen으로 업데이트
        self.choice = 0
        self.easy_words = ["BELL", "STAR", "PICNIC", "PIE", "HAT", "HEART", "FLAG"]
        self.medium_words = ["CARPET", "POPCORN", "SEAFOOD", "DOORBELL", "COWBOY", "INSIDE", "OUTSIDE", "RAINBOW", "POSTMAN", "WATERMELON", "FOOTBALL", "STRAWBERRY"]
        self.hard_words = ["BACKGROUND", "BOOKWORM", "FIREFIGHTER", "SOUNDPROOF", "THUNDERSTORM", "CAMPGROUND", "FRIENDSHIP", "SKYSCRAPER", "SUPERHUMAN", "FINGERPRINT", "MASTERPIECE", "LOUDSPEAKER"]
        self.color_words = ["BLACK", "WHITE", "RED", "GREEN", "blue", "GREY"]
        self.font = font.variablefont_medium
        self.font2 = font.variablefont_small
        self.condition = 0
        self.start_time = 0
        self.the_word = ""
        self.empty_list = []

    def random_num(self, choice):
        if choice == 1:
            return random.randint(0, len(self.easy_words) - 1)
        elif choice == 2:
            return random.randint(0, len(self.medium_words) - 1)
        elif choice == 3:
            return random.randint(0, len(self.hard_words) - 1)
        elif choice == 4:
            return random.randint(0, len(self.color_words) - 1)

    def get_word(self, number, choice):
        if choice == 1:
            return self.easy_words[number]
        elif choice == 2:
            return self.medium_words[number]
        elif choice == 3:
            return self.hard_words[number]
        elif choice == 4:
            return self.color_words[number]

    def pre_hangman(self):
        pygame.draw.line(self.display, color.BLACK, (10, 400), (300, 400), 8)
        pygame.draw.line(self.display, color.BLACK, (50, 50), (50, 400), 8)
        pygame.draw.line(self.display, color.BLACK, (50, 60), (250, 60), 8)
        pygame.draw.line(self.display, color.BLACK, (150, 60), (150, 100), 8)
        pygame.draw.circle(self.display, color.BLACK, (150, 150), 50, 8) # 머리
        pygame.draw.line(self.display, color.BLACK, (150, 200), (150, 300), 8) # 몸
        pygame.draw.line(self.display, color.BLACK, (150, 210), (100, 250), 8) # 왼팔
        pygame.draw.line(self.display, color.BLACK, (150, 210), (200, 250), 8)  # 오른팔
        pygame.draw.line(self.display, color.BLACK, (150, 300), (100, 350), 8)  # 왼다리
        pygame.draw.line(self.display, color.BLACK, (150, 300), (200, 350), 8)  # 오른다리


    def hangman(self,condition):
        if condition == 0:
            pygame.draw.line(self.display, color.GREY, (10, 400), (300, 400), 8)
            pygame.draw.line(self.display, color.GREY, (50, 50), (50, 400), 8)
            pygame.draw.line(self.display, color.GREY, (50, 60), (250, 60), 8)
            pygame.draw.line(self.display, color.GREY, (150, 60), (150, 100), 8)
            pygame.draw.circle(self.display, color.GREY, (150, 150), 50, 8)
            pygame.draw.line(self.display, color.GREY, (150, 200), (150, 300), 8)
            pygame.draw.line(self.display, color.GREY, (150, 210), (100, 250), 8)
            pygame.draw.line(self.display, color.GREY, (150, 210), (200, 250), 8)
            pygame.draw.line(self.display, color.GREY, (150, 300), (100, 350), 8)
            pygame.draw.line(self.display, color.GREY, (150, 300), (200, 350), 8)


    def start_screen(self):
        self.display.fill(color.WHITE)  # 메인 메뉴 화면을 지우고 화면을 설정
        self.display.blit(self.font.render("행 맨", True, color.BLACK), (350, 20))
        self.display.blit(self.font.render("난이도", True, color.BLACK), (330, 130))
        self.display.blit(self.font2.render("1 - 쉬움", True, color.BLACK), (330, 200))
        self.display.blit(self.font2.render("2 - 보통", True, color.BLACK), (330, 250))
        self.display.blit(self.font2.render("3 - 어려움", True, color.BLACK), (330, 300))
        pygame.display.update()

    def main(self):
        pygame.init()
        self.start_screen()
        self.pre_hangman()
        first_condition = True

        while first_condition:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_1 or event.key == 257:  # 257 is 1 in numpad
                        self.choice = 1
                        first_condition = False
                        break
                    elif event.key == K_2 or event.key == 258:  # 258 is 2 in numpad
                        self.choice = 2
                        first_condition = False
                        break
                    elif event.key == K_3 or event.key == 259:  # 259 is 3 in numpad
                        self.choice = 3
                        first_condition = False
                        break
                # Handle mouse click events
                elif event.type == MOUSEBUTTONDOWN:
                    if 290 < pygame.mouse.get_pos()[0] < 370 and 200 < pygame.mouse.get_pos()[1] < 215:
                        self.choice = 1
                        first_condition = False
                        break
                    elif 290 < pygame.mouse.get_pos()[0] < 370 and 250 < pygame.mouse.get_pos()[1] < 265:
                        self.choice = 2
                        first_condition = False
                        break
                    elif 290 < pygame.mouse.get_pos()[0] < 390 and 300 < pygame.mouse.get_pos()[1] < 315:
                        self.choice = 3
                        first_condition = False
                        break
            if self.choice != 0:
                self.display.fill(color.WHITE)
                pygame.display.update()  # 화면을 업데이트
                pygame.time.Clock().tick(30)

            self.the_num = self.random_num(self.choice)
            self.the_word = self.get_word(self.the_num, self.choice)

        self.the_num = self.random_num(self.choice)
        self.the_word = self.get_word(self.the_num, self.choice)

        for i in range(len(self.the_word)):
            self.empty_list.append('-')

        hidden = self.font.render("".join(self.empty_list), True, color.BLACK)
        hidden_rect = hidden.get_rect()
        hidden_rect.center = (350, 250)
        self.display.blit(hidden, hidden_rect)

        self.off = 0
        self.the_time = 0
        self.start_time = time.time()

        self.display.blit(self.font2.render("Time(s):", True, color.BLACK), (300, 10))

        last_key_pressed = ""
        self.display.blit(
            font.variablefont_small.render(
                "게임을 종료하려면 0을 누르세요.", True,color.BLACK), (20, 10))

        while True:
            self.hangman(self.condition)
            end = time.time()
            if int(end) - int(self.start_time) == 1:
                pygame.draw.rect(self.display, color.WHITE, (385, 0, 100, 50))
                self.the_time += 1
                timer = self.font2.render(str(self.the_time), True, color.BLACK)
                self.display.blit(timer, (400, 10))
                self.start_time = time.time()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    last_key_pressed = event.key
                    pygame.draw.rect(self.display, color.WHITE, (220, 200, 280, 100))
                    pygame.draw.rect(self.display, color.WHITE, (260, 50, 200, 100))
                    user_input = event.key
                    if re.search("[a-z]", chr(event.key)):
                        if chr(event.key).upper() in self.the_word or chr(event.key).lower() in self.the_word:
                            for i in range(len(self.the_word)):
                                if self.the_word[i] == chr(event.key).upper() or self.the_word[i] == chr(event.key).lower():
                                    self.empty_list[i] = self.the_word[i]
                        else:
                            self.condition += 1

                        hidden = self.font.render("".join(self.empty_list), True, color.BLACK)
                        hidden_rect = hidden.get_rect()
                        hidden_rect.center = (350, 250)
                        self.display.blit(hidden, hidden_rect)
                    else:
                        if event.key == K_0 or event.key == 256:
                            self.display.blit(self.font.render("EXIT?", True,color.RED), (340, 220))
                            self.display.blit(self.font2.render("Yes", True, color.blue), (340, 270))
                            self.display.blit(self.font2.render("No", True, color.blue), (415, 270))
                        else:
                            input_text = self.font2.render("INVALID INPUT!!!", True, color.RED)
                            input_rect = input_text.get_rect()
                            input_rect.center = (350, 100)
                            self.display.blit(input_text, input_rect)
                            self.display.blit(hidden, hidden_rect)
                elif event.type == KEYUP:
                    pygame.draw.rect(self.display, color.WHITE, (260, 50, 200, 100))
                elif event.type == MOUSEBUTTONDOWN:
                    if last_key_pressed == K_0 or last_key_pressed == 256:
                        if 340 < pygame.mouse.get_pos()[0] < 385 and 270 < pygame.mouse.get_pos()[1] < 285:
                            pygame.draw.rect(self.display, color.WHITE, (340, 270, 35, 25))
                            self.display.blit(self.font2.render("Yes", True, color.GREEN), (340, 270))
                        elif 415 < pygame.mouse.get_pos()[0] < 450 and 270 < pygame.mouse.get_pos()[1] < 285:
                            pygame.draw.rect(self.display, color.WHITE, (415, 270, 35, 25))
                            self.display.blit(self.font2.render("No", True, color.GREEN), (415, 270))
                elif event.type == MOUSEBUTTONUP:
                    if last_key_pressed == K_0 or last_key_pressed == 256:
                        if 340 < pygame.mouse.get_pos()[0] < 385 and 270 < pygame.mouse.get_pos()[1] < 285:
                            pygame.quit()
                            sys.exit()
                        elif 415 < pygame.mouse.get_pos()[0] < 450 and 270 < pygame.mouse.get_pos()[1] < 285:
                            pygame.draw.rect(self.display, color.WHITE, (415, 270, 35, 25))
                            self.display.blit(self.font2.render("No", True, color.blue), (415, 270))
                            pygame.draw.rect(self.display, color.WHITE, (300, 200, 200, 100))
                            hidden = self.font.render("".join(self.empty_list), True, color.BLACK)
                            hidden_rect = hidden.get_rect()
                            hidden_rect.center = (400, 250)
                            self.display.blit(hidden, hidden_rect)
                            last_key_pressed = ""

            if self.condition == 10:
                self.display.fill(color.WHITE)
                self.hangman(self.condition + 1)
                over_text = self.font2.render("게임 오버!!!", True, color.RED)
                over_rect = over_text.get_rect()
                over_rect.center = (400, 250)
                self.display.blit(over_text, over_rect)
                self.off = 1
            elif self.the_word == "".join(self.empty_list):
                self.display.fill(color.WHITE)
                congrats = self.font.render("게임 승리!!!", True, color.GREEN)
                congrats_rect = congrats.get_rect()
                congrats_rect.center = (250, 220)
                self.display.blit(congrats, congrats_rect)
                word = self.font2.render("정답은:", True, color.BLACK)
                word_rect = word.get_rect()
                word_rect.center = (250, 250)
                self.display.blit(word, word_rect)
                word2 = self.font.render(self.the_word, True, color.BLACK)
                word2_rect = word2.get_rect()
                word2_rect.center = (250, 285)
                self.display.blit(word2, word2_rect)
                self.off = 1
            pygame.display.update()
            pygame.time.Clock().tick(30)
            if self.off == 1:
                time.sleep(5)
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    game = HangmanGame()
    game.main()
