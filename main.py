import pygame
from headers.InputBox import InputBox
from headers.funcoesGerais import *
from headers.switcherButton import Switcher

BACKGROUND_COLOR = (255, 255, 255)
(width, height) = (300, 200)
IMAGE_PATH = "Images/"
BLACK = (0, 0, 0)

TIME_FADING = 0.1
FPS = 30
CORRECT_ANS = 1
WRONG_ANS = 2

all_images = []
pygame.init()

clock = pygame.time.Clock()

# all_images = loadImages(True, True, False)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiragana/Katakana Game")

input_box = InputBox(55, 125, 140, 32)

hiragana_switcher = Switcher(150, height / 2 - 35, 70, 20)
katakana_switcher = Switcher(150, height / 2, 70, 20)
kanji_switcher = Switcher(150, height / 2 + 35, 70, 20)

switchers = [hiragana_switcher, katakana_switcher, kanji_switcher]

running = True

correctImage = pygame.image.load("Images/correct.jpg").convert()
wrongImage = pygame.image.load("Images/wrong.jpg").convert()

myFont = pygame.font.SysFont('monospace', 15)
wrongAnsFont = pygame.font.SysFont("impact", 20)
myFontFinal = pygame.font.SysFont(None, 48)
myFontFinal2 = pygame.font.SysFont("impact", 24)
colorFinal = pygame.Color("darkslateblue")
colorFinal_Correct = pygame.Color(0,201,87)
colorFinal_Wrong = pygame.Color("firebrick1")

menu_font_selected = pygame.font.SysFont("impact", 28)
menu_font_not_selected = pygame.font.SysFont("impact", 24)
menu_color_selected = pygame.Color("deepskyblue4")
menu_color_not_selected = pygame.Color("deepskyblue1")

cntAcertos = 0
cntAtual = 1
cntTotal = 0

finished = False
fading = 0
cntFading = 0

contador = 0

inMenu = True
menuSelect = 1

while running:
    if(not inMenu):
        if(fading == 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif not finished and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                        if(input_box.getText() == current_image[1]):
                            fading = 1
                            cntAcertos += 1
                        else:
                            fading = 2
                if(not finished):
                    input_box.handle_event(event)

        if(not finished):
            if(fading != 0): cntFading += 1
            if(cntFading == TIME_FADING * FPS):
                fading = 0
                cntFading = 0

                input_box.setText("")

                current_image = getRandomImage(all_images)
                image = pygame.image.load(current_image[0])

                if(current_image[0][-3:] == 'jpg'):
                    finished = True
                    input_box.setActive(False)
                    input_box.update()
                    continue

                cntAtual += 1

            input_box.update()
            screen.fill(BACKGROUND_COLOR)
            input_box.draw(screen)
            screen.blit(image, (width / 2 - 35, height / 2 - 70))
            label = myFont.render(str(cntAtual) + "/" + str(cntTotal), 1, (0, 0, 0))
            screen.blit(label, (width / 2 - 20, height / 2 + 70))

            if(fading == CORRECT_ANS):
                correctImage.set_alpha(round(255 - 255 * (cntFading / float(TIME_FADING * FPS))))
                screen.blit(correctImage, (width / 2 + 30, height / 2 - 90))
            elif(fading == WRONG_ANS):
                wrongImage.set_alpha(round(255 - 255 * (cntFading / float(TIME_FADING * FPS))))
                screen.blit(wrongImage, (width / 2 + 30, height / 2 - 90))
                correctAns = wrongAnsFont.render("Correct: " + current_image[1], 1, (0, 0, 0))
                screen.blit(correctAns, (width - 80, height - 20))

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
            screen.blit(numCorrect, (130, 85))
            screen.blit(numWrong, (129, 155))
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif(event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    if(menuSelect == 4):
                        running = False
                        continue
                    inMenu = False
                    all_images = loadImages(switchers[0].on, switchers[1].on, switchers[2].on)
                    if(len(all_images) == 0):
                        finished = True
                    else:
                        cntTotal = len(all_images)
                        current_image = getRandomImage(all_images)
                        image = pygame.image.load(current_image[0])
                elif(event.key == pygame.K_UP):
                    menuSelect = max(1, menuSelect - 1)
                elif(event.key == pygame.K_DOWN):
                    menuSelect = min(4, menuSelect + 1)
                elif(event.key == pygame.K_RIGHT):
                    if(menuSelect <= 3):
                        switchers[menuSelect - 1].switch(False)
                elif(event.key == pygame.K_LEFT):
                    if(menuSelect <= 3):
                        switchers[menuSelect - 1].switch(True)
        screen.fill(BACKGROUND_COLOR)
        labelEst = myFontFinal.render("Menu '-'", 1, colorFinal)
        screen.blit(labelEst, (width / 2 - 50, height / 2 - 90))

        if(menuSelect == 1):
            label_hiragana = menu_font_selected.render("Hiragana", 1, menu_color_selected)
        else:
            label_hiragana = menu_font_not_selected.render("Hiragana", 1, menu_color_not_selected)

        if(menuSelect == 2):
            label_katakana = menu_font_selected.render("Katakana", 1, menu_color_selected)
        else:
            label_katakana = menu_font_not_selected.render("Katakana", 1, menu_color_not_selected)

        if(menuSelect == 3):
            label_kanji = menu_font_selected.render("Kanji", 1, menu_color_selected)
        else:
            label_kanji = menu_font_not_selected.render("Kanji", 1, menu_color_not_selected)

        if(menuSelect == 4):
            label_sair = menu_font_selected.render("Sair", 1, menu_color_selected)
        else:
            label_sair = menu_font_not_selected.render("Sair", 1, menu_color_not_selected)

        for switch in switchers:
            switch.draw(screen)

        screen.blit(label_hiragana, (40, height / 2 - 35))
        screen.blit(label_katakana, (40, height / 2))
        screen.blit(label_kanji, (40, height / 2 + 35))
        screen.blit(label_sair, (40, height / 2 + 70))

    pygame.display.flip()
    clock.tick(FPS)
