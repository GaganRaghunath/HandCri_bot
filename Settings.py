import pygame


class Setting:

    def __init__(self):
        self.Disp_Height = 600
        self.Disp_Width = 900

        self.AQUA = (0, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.FUCHSIA = (255, 0, 255)
        self.GRAY = (128, 128, 128)
        self.GREEN = (0, 128, 0)
        self.LIME = (0, 255, 0)
        self.MAROON = (128, 0, 0)
        self.NAVY_BLUE = (0, 0, 128)

        self.score = 0
        self.p_count = 0
        self.innings = 1
        self.p1_score = 0

        self.one_img = pygame.image.load('images/one.png')
        self.two_img = pygame.image.load('images/two.png')
        self.three_img = pygame.image.load('images/three.png')
        self.four_img = pygame.image.load('images/four.png')
        self.five_img = pygame.image.load('images/five.png')
        self.six_img = pygame.image.load('images/six.png')
        self.out_img = pygame.image.load('images/out.png')
        self.start_img = pygame.image.load('images/play-button.png')

        self.one_img1 = pygame.image.load('images/number1.png')
        self.two_img2 = pygame.image.load('images/number2.png')
        self.three_img3 = pygame.image.load('images/number3.png')
        self.four_img4 = pygame.image.load('images/number4.png')
        self.five_img5 = pygame.image.load('images/number5.png')
        self.six_img6 = pygame.image.load('images/number6.png')

        self.Comp_img = [self.one_img1, self.two_img2, self.three_img3, self.four_img4, self.five_img5, self.six_img6]
