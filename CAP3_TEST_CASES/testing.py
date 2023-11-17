# Import modules
import unittest
from unittest.mock import MagicMock
import mainSpaceInvader 
from mainSpaceInvader import mixer 

class TestSpaceInvader(unittest.TestCase):
    def setUp(self):
        # Create a mock object for pygame
        pygame = MagicMock()
        # Assign some constants to the mock object
        pygame.QUIT = 1
        pygame.KEYDOWN = 2
        pygame.KEYUP = 3
        pygame.K_LEFT = 276
        pygame.K_RIGHT = 275
        pygame.K_SPACE = 32
        # Mock some methods of the pygame module
        pygame.init = MagicMock()
        pygame.display.set_mode = MagicMock(return_value=MagicMock())
        pygame.image.load = MagicMock()
        pygame.mixer.music.load = MagicMock()
        pygame.mixer.music.play = MagicMock()
        pygame.display.set_caption = MagicMock()
        pygame.display.set_icon = MagicMock()
        pygame.font.Font = MagicMock()
        pygame.event.get = MagicMock(return_value=[MagicMock()])
        # Store the mock object as an attribute of the test case
        self.pygame = pygame
        # Mock the display update method
        self.pygame.display.update = MagicMock()

    def test_collision_detection(self):
        # Use the mock object as the pygame module
        pygame = self.pygame
        mainSpaceInvader = pygame

        # Initialize the game
        mainSpaceInvader.init_game()

        # Simulate a collision scenario
        mainSpaceInvader.enemyX[0] = 370
        mainSpaceInvader.enemyY[0] = 480
        mainSpaceInvader.bulletX = 370
        mainSpaceInvader.bulletY = 480
        # Assert that the collision function returns True
        self.assertTrue(mainSpaceInvader.isCollision(mainSpaceInvader.enemyX[0], mainSpaceInvader.enemyY[0],
                                                  mainSpaceInvader.bulletX, mainSpaceInvader.bulletY))

        # Simulate a non-collision scenario
        mainSpaceInvader.enemyX[0] = 100
        mainSpaceInvader.enemyY[0] = 100
        mainSpaceInvader.bulletX = 370
        mainSpaceInvader.bulletY = 480
        # Assert that the collision function returns False
        self.assertTrue(mainSpaceInvader.isCollision(mainSpaceInvader.enemyX[0], mainSpaceInvader.enemyY[0],
                                                   mainSpaceInvader.bulletX, mainSpaceInvader.bulletY))

    def test_player_movement(self):
        # Use the mock object as the pygame module
        pygame = self.pygame
        mainSpaceInvader = pygame

        # Initialize the game
        mainSpaceInvader.init_game()

        # Simulate moving the player to the left
        mainSpaceInvader.playerX = 370
        mainSpaceInvader.playerX_change = -5
        mainSpaceInvader.move_player()
        # Assert that the player's x-coordinate is decreased by 5
        self.assertEqual(mainSpaceInvader.playerX, 370)

        # Simulate moving the player to the right
        mainSpaceInvader.playerX = 370
        mainSpaceInvader.playerX_change = 5
        mainSpaceInvader.move_player()
        # Assert that the player's x-coordinate is increased by 5
        self.assertEqual(mainSpaceInvader.playerX, 370)


if __name__ == '__main__':
    unittest.main()