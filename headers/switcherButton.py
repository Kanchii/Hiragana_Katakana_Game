class Switcher:
    def __init__(self, x, y, width, height):
        import pygame
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.on = False
        self.colorOffBorder = pygame.Color("gray2")
        self.colorOff = pygame.Color("gray43")
        self.colorOnBorder = pygame.Color("green4")
        self.colorOn = pygame.Color("green2")

    def switch(self, state):
        self.on = state

    def getState(self):
        return self.on

    def draw(self, screen):
        import pygame

        if(not self.on):
            rectOff = pygame.Rect(self.x + self.width / 2, self.y + 2, self.width / 2 - 2, self.height - 4)
            rect = pygame.Rect(self.x, self.y, self.width, self.height)

            pygame.draw.rect(screen, self.colorOffBorder, rect, 3)
            pygame.draw.rect(screen, self.colorOff, rectOff, 0)
            # pygame.draw.circle(screen, self.colorOffBorder, (int(self.x + self.width // 2 + self.width // 4), int(self.y + 10)), 5, 0)
        else:
            rectOn = pygame.Rect(self.x + 2, self.y + 2, self.width / 2 - 2, self.height - 4)
            rect = pygame.Rect(self.x, self.y, self.width, self.height)

            pygame.draw.rect(screen, self.colorOnBorder, rect, 3)
            pygame.draw.rect(screen, self.colorOn, rectOn, 0)
            # pygame.draw.circle(screen, self.colorOnBorder, (int(self.x + self.width // 4), int(self.y + 10)), 5, 0)
