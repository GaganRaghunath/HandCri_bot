import pygame
import sys
from pygame.locals import *
import random

from Settings import Setting


def blit_Img(DISPLAY_SURF, setting):
    DISPLAY_SURF.fill(setting.GRAY)
    DISPLAY_SURF.blit(setting.one_img, (40, 400))
    DISPLAY_SURF.blit(setting.two_img, (180, 400))
    DISPLAY_SURF.blit(setting.three_img, (320, 400))
    DISPLAY_SURF.blit(setting.four_img, (460, 400))
    DISPLAY_SURF.blit(setting.five_img, (600, 400))
    DISPLAY_SURF.blit(setting.six_img, (740, 400))

    basicFont = pygame.font.SysFont(None, 48)
    st1 = "Computer"
    st2 = "PLAYER"
    text1 = basicFont.render(str(st1), True, setting.BLACK, setting.GRAY)
    text2 = basicFont.render(str(st2), True, setting.BLACK, setting.GRAY)
    text1rect = text1.get_rect()
    text2rect = text2.get_rect()
    text1rect.centerx = 90
    text1rect.centery = 100
    text2rect.centerx = 90
    text2rect.centery = 260
    DISPLAY_SURF.blit(text1, text1rect)
    DISPLAY_SURF.blit(text2, text2rect)


def Game_operation(k, r, setting, DISPLAY_SURF):
    if setting.innings == 2 and setting.p_count == 5:
        game_over(DISPLAY_SURF, setting)

    if k == r:
        setting.p_count += 1
    else:
        setting.score += k + 1

    if setting.innings == 1 and setting.p_count == 5:
        DISPLAY_SURF.fill(setting.FUCHSIA)
        basicFont = pygame.font.SysFont(None, 48)
        st = "All Out!! PLAYER2 Target {0}".format(setting.score)
        text = basicFont.render(str(st), True, setting.BLACK, setting.GRAY)
        textrect = text.get_rect()
        textrect.centerx = 450
        textrect.centery = 300
        DISPLAY_SURF.blit(text, textrect)
        pygame.display.update()
        setting.innings = 2
        setting.p1_score = setting.score
        setting.score, setting.p_count = 0, 0


def game_over(DISPLAY_SURF, setting):
    DISPLAY_SURF.fill(setting.FUCHSIA)
    basicFont = pygame.font.SysFont(None, 48)
    if setting.p1_score > setting.score:
        st = "GAME OVER PLAYER1 WINS"
    else:
        st = "GAME OVER PLAYER2 WINS"
    text = basicFont.render(str(st), True, setting.BLACK, setting.GRAY)
    textrect = text.get_rect()
    textrect.centerx = 450
    textrect.centery = 300
    DISPLAY_SURF.blit(text, textrect)
    pygame.display.update()
    while True:
        for i in pygame.event.get():
            if i.type == QUIT:
                pygame.quit()
                sys.exit()


def getScore(DISPLAYSURF, setting):
    basicFont = pygame.font.SysFont(None, 48)
    st = "Score :{0}/{1}".format(setting.score, setting.p_count)
    text = basicFont.render(str(st), True, setting.BLACK, setting.GRAY)
    textrect = text.get_rect()
    textrect.centerx = 750
    textrect.centery = 50
    DISPLAYSURF.blit(text, textrect)


def check_key(DISPLAY_SURF, setting):
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_1:
                blit_Img(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.one_img1, (180, 200))
                r = random.randint(0, 5)
                Game_operation(0, r, setting, DISPLAY_SURF)
                getScore(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.Comp_img[r], (180, 40))
            elif i.key == pygame.K_2:
                blit_Img(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.two_img2, (180, 200))
                r = random.randint(0, 5)
                Game_operation(1, r, setting, DISPLAY_SURF)
                getScore(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.Comp_img[r], (180, 40))
            elif i.key == pygame.K_3:
                blit_Img(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.three_img3, (180, 200))
                r = random.randint(0, 5)
                Game_operation(2, r, setting, DISPLAY_SURF)
                getScore(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.Comp_img[r], (180, 40))
            elif i.key == pygame.K_4:
                blit_Img(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.four_img4, (180, 200))
                r = random.randint(0, 5)
                Game_operation(3, r, setting, DISPLAY_SURF)
                getScore(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.Comp_img[r], (180, 40))
            elif i.key == pygame.K_5:
                blit_Img(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.five_img5, (180, 200))
                r = random.randint(0, 5)
                Game_operation(4, r, setting, DISPLAY_SURF)
                getScore(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.Comp_img[r], (180, 40))
            elif i.key == pygame.K_6:
                blit_Img(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.six_img6, (180, 200))
                r = random.randint(0, 5)
                Game_operation(5, r, setting, DISPLAY_SURF)
                getScore(DISPLAY_SURF, setting)
                DISPLAY_SURF.blit(setting.Comp_img[r], (180, 40))
            else:
                pass
    pygame.display.update()


def main_Game():
    pygame.init()
    setting = Setting()

    DISPLAY_SURF = pygame.display.set_mode((setting.Disp_Width, setting.Disp_Height))
    pygame.display.set_caption("HAND CRICKET")
    FPS = 30
    fps_clock = pygame.time.Clock()
    blit_Img(DISPLAY_SURF, setting)

    while True:
        check_key(DISPLAY_SURF, setting)
        fps_clock.tick(FPS)


main_Game()
