import sys
import pygame

class BlueWindow:
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.set_caption("Blue Window")

		self.bg_color = (120, 120, 120)

	def run_window(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			pygame.display(self.screen)


if __name__ == '__main__':
	blue = BlueWindow()
	blue.run_window()