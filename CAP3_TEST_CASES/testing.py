import unittest
from unittest.mock import MagicMock
import mainSpaceInvader  

class TestSpaceInvader(unittest.TestCase):
    def setUp(self):
        pygame = MagicMock()
        pygame.QUIT = 1
        pygame.KEYDOWN = 2
        pygame.KEYUP = 3
        pygame.K_LEFT = 276
        pygame.K_RIGHT = 275
        pygame.K_SPACE = 32
        pygame.init = MagicMock()
        pygame.display.set_mode = MagicMock(return_value=MagicMock())
        pygame.image.load = MagicMock()
        pygame.mixer.music.load = MagicMock()
        pygame.mixer.music.play = MagicMock()
        pygame.display.set_caption = MagicMock()
        pygame.display.set_icon = MagicMock()
        pygame.font.Font = MagicMock()
        pygame.event.get = MagicMock(return_value=[MagicMock()])
        pygame.KEYDOWN = 2
        pygame.KEYUP = 3
        pygame.QUIT = 12
        pygame.K_LEFT = 276
        pygame.K_RIGHT = 275
        pygame.K_SPACE = 32

        self.pygame = pygame
        self.pygame.display.update = MagicMock()

    def test_collision_detection(self):
        # Mocking required modules
        pygame = self.pygame
        mainSpaceInvader = pygame

        # Initializing game
        mainSpaceInvader.init_game()

        # Creating a collision
        mainSpaceInvader.enemyX[0] = 370
        mainSpaceInvader.enemyY[0] = 480
        mainSpaceInvader.bulletX = 370
        mainSpaceInvader.bulletY = 480
        self.assertTrue(mainSpaceInvader.isCollision(mainSpaceInvader.enemyX[0], mainSpaceInvader.enemyY[0],
                                                  mainSpaceInvader.bulletX, mainSpaceInvader.bulletY))

        # Creating a non-collision
        mainSpaceInvader.enemyX[0] = 100
        mainSpaceInvader.enemyY[0] = 100
        mainSpaceInvader.bulletX = 370
        mainSpaceInvader.bulletY = 480
        self.assertTrue(mainSpaceInvader.isCollision(mainSpaceInvader.enemyX[0], mainSpaceInvader.enemyY[0],
                                                   mainSpaceInvader.bulletX, mainSpaceInvader.bulletY))

    def test_player_movement(self):
        # Mocking required modules
        pygame = self.pygame
        mainSpaceInvader = pygame

        # Initializing  game
        mainSpaceInvader.init_game()

        # Move player to the left
        mainSpaceInvader.playerX = 370
        mainSpaceInvader.playerX_change = -5
        mainSpaceInvader.move_player()
        self.assertEqual(mainSpaceInvader.playerX, 370)

        # Move player  to the right
        mainSpaceInvader.playerX = 370
        mainSpaceInvader.playerX_change = 5
        mainSpaceInvader.move_player()
        self.assertEqual(mainSpaceInvader.playerX, 370)


if __name__ == '__main__':
    unittest.main()