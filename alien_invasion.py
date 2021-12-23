import sys
import pygame
from settings import Settings

class AlienInvasion:
    #管理整个游戏的类
    def __init__(self):
        #初始化整个游戏
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        #开始循环
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
if __name__=='__main__':
    ai = AlienInvasion()
    ai.run_game()