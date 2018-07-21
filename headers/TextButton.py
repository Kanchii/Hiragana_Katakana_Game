class TextButton:
    def __init__(self, x, y, w, h, btn_Color, font, txt_Color, text):
        import pygame
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.btn_Color = btn_Color
        self.font = font
        self.txt_Color = txt_Color
        self.text = text
        self.text_surface = self.font.render(self.text, 1, self.txt_Color)

        self.btn_Border_Color = None
        self.btn_Over_Color = None
        self.btn_Over_Font = None

    def draw(self, screen):
        import pygame

        # Desenhando o retangulo do botão
        button_rect = pygame.Rect(self.x, self.y, max(self.w, self.text_surface.get_width() + 10), max(self.h, self.text_surface.get_height() + 10))
        pygame.draw.rect(screen, self.btn_Color, button_rect, 0)

        # Verificando se o botão tem borda
        if(self.btn_Border_Color != None):
            button_rect = pygame.Rect(self.x, self.y, max(self.w, self.text_surface.get_width() + 10), max(self.h, self.text_surface.get_height() + 10))
            pygame.draw.rect(screen, self.btn_Border_Color, button_rect, 3)

        ''' Deixando o texto centralizado '''
        b = (self.w - self.text_surface.get_width()) // 2
        if(b >= 5):
            screen.blit(self.text_surface, (self.x + b, self.y + 5))
        else:
            screen.blit(self.text_surface, (self.x + 5, self.y + 5))

    def setBorder(self, btn_Border_Color):
        self.btn_Border_Color = btn_Border_Color

    def setInteractive(self, font, color):
        self.btn_Over_Color = color
        self.btn_Over_Font = font

    def eventHandler(self, event):
        import pygame
        if(event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            if(self.btn_Over_Color != None and pos[0] >= self.x and pos[0] <= self.x + self.w and pos[1] >= self.y and pos[1] <= self.y + self.h):
                self.text_surface = self.btn_Over_Font.render(self.text, 1, self.btn_Over_Color)
            else:
                self.text_surface = self.font.render(self.text, 1, self.txt_Color)
            return 0
        elif(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_btn_pressed = pygame.mouse.get_pressed()
            if(mouse_btn_pressed[0] == 1):
                pos = pygame.mouse.get_pos()
                if(pos[0] >= self.x and pos[0] <= self.x + self.w and pos[1] >= self.y and pos[1] <= self.y + self.h):
                    return 1
            return 0
