import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
   # """Overall class to manage game assets and behavior."""
   def __init__(self):
      # """Initialize the game, and create game resources."""
      pygame.init()
      self.screen = pygame.display.set_mode((1200, 800))
      pygame.display.set_caption("Alien Invasion")
      self.clock = pygame.time.Clock()
      # Set the background color.
      self.bg_color = (230, 230, 230)
      self.settings = Settings()
      self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
      #displaying img of rocket
      self.ship = Ship(self)

   def run_game(self):
     """Start the main loop for the game."""
     while True:
        self._check_events()
        self._update_screen()
        self.ship.update()
        # Watch for keyboard and mouse events.
      #   for event in pygame.event.get():
         #   self.screen.fill(self.settings.bg_color)
           #ship img
         #   self.ship.blitme()
         #   if event.type == pygame.QUIT:
            #   sys.exit()
              # Make the most recently drawn screen visible.
            #   pygame.display.flip()
              #self.clock.tick(60)
      #   self.screen.fill(self.bg_color)
   def _update_screen(self):
      #Update images on the screen, and flip to the new screen
      self.screen.fill(self.settings.bg_color)
      self.ship.blitme()
      pygame.display.flip()
   def _check_events(self):
      """Respond to keypresses and mouse events."""
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
         elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               # Move the ship to the right.
               #self.ship.rect.x += 1
               self.ship.moving_right = True
         elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
               self.ship.moving_right = False

if __name__ == '__main__':
   # Make a game instance, and run the game.
   ai = AlienInvasion()
   ai.run_game()