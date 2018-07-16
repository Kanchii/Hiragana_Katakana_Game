import pygame
from libs.InputBox import InputBox
from libs.funcoesGerais import *

BACKGROUND_COLOR = (255, 255, 255)
(width, height) = (300, 200)
IMAGE_PATH = "Images/"
BLACK = (0, 0, 0)

TIME_FADING = 1
FPS = 30
CORRECT_ANS = 1
WRONG_ANS = 2

all_images = []
pygame.init()

clock = pygame.time.Clock()

all_images = loadImages(IMAGE_PATH)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiragana/Katakana Game")

input_box = InputBox(55, 125, 140, 32)

running = True

# all_fonts = pygame.font.get_fonts()

correctImage = pygame.image.load("Images/correct.jpg").convert()
wrongImage = pygame.image.load("Images/wrong.jpg").convert()

myFont = pygame.font.SysFont('monospace', 15)
myFontFinal = pygame.font.SysFont(None, 48)
myFontFinal2 = pygame.font.SysFont("impact", 24)
colorFinal = pygame.Color("darkslateblue")
colorFinal_Correct = pygame.Color(0,201,87)
colorFinal_Wrong = pygame.Color("firebrick1")

cntAcertos = 0
cntAtual = 1
cntTotal = len(all_images)

finished = False
current_image = getRandomImage(all_images, IMAGE_PATH)
image = pygame.image.load(current_image)
fading = 0
cntFading = 0

contador = 0

while running:
    if(fading == 0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif not finished and event.key == pygame.K_RETURN:
                    if(input_box.getText() == current_image[7:-4]):
                        fading = 1
                        cntAcertos += 1
                    else:
                        fading = 2
            input_box.handle_event(event)

    if(not finished):
        if(fading != 0): cntFading += 1
        if(cntFading == TIME_FADING * FPS):
            fading = 0
            cntFading = 0

            current_image = getRandomImage(all_images, IMAGE_PATH)
            image = pygame.image.load(current_image)

            cntAtual += 1

            if(current_image[-3:] == 'jpg'):
                finished = True
                input_box.setActive(False)
                input_box.update()
                continue

        input_box.update()
        screen.fill(BACKGROUND_COLOR)
        input_box.draw(screen)
        screen.blit(image, (width / 2 - 35, height / 2 - 70))
        label = myFont.render(str(cntAtual) + "/" + str(cntTotal), 1, (0, 0, 0))
        screen.blit(label, (width / 2 - 20, height / 2 + 70))

        if(fading == CORRECT_ANS):
            correctImage.set_alpha(round(255 - 255 * (cntFading / float(FPS))))
            screen.blit(correctImage, (width / 2 + 30, height / 2 - 90))
        elif(fading == WRONG_ANS):
            wrongImage.set_alpha(round(255 - 255 * (cntFading / float(FPS))))
            screen.blit(wrongImage, (width / 2 + 30, height / 2 - 90))
    else:
        screen.fill(BACKGROUND_COLOR)
        labelEst = myFontFinal.render("Completed!", 1, colorFinal)
        screen.blit(labelEst, (width / 2 - 92, height / 2 - 80))
        correctImage.set_alpha(255)
        wrongImage.set_alpha(255)
        screen.blit(correctImage, (40, 70))
        screen.blit(wrongImage, (39, 135))
        numCorrect = myFontFinal2.render(str(cntAcertos), 1, colorFinal_Correct)
        numWrong = myFontFinal2.render(str(cntTotal - cntAcertos), 1, colorFinal_Wrong)
        screen.blit(numCorrect, (130, 80))
        screen.blit(numWrong, (129, 150))
    pygame.display.flip()
    clock.tick(FPS)
