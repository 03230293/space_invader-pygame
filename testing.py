import unittest
import pygame
# from pygame import Spaceship
# from pygame import Alien_Bullets
# from pygame import Explosion

class TestSpaceInvader(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Space Invader')

    def test_window_creation(self):
        self.assertEqual(self.screen.get_width(), 800)
        self.assertEqual(self.screen.get_height(), 600)

    def test_window_caption(self):
        self.assertEqual(pygame.display.get_caption()[0], 'Space Invader')


class TestSoundLoading(unittest.TestCase):
    def setUp(self):
        pygame.mixer.init()
        self.explosion_fx = pygame.mixer.Sound("explosion.wav")
        self.explosion_fx.set_volume(1)
        self.laser_fx = pygame.mixer.Sound("laser.wav")
        self.laser_fx.set_volume(1)

    def test_sound_loading(self):
        self.assertIsNotNone(self.explosion_fx)
        self.assertIsNotNone(self.laser_fx)

    def test_sound_playing(self):
        self.explosion_fx.play()
        self.assertTrue(pygame.mixer.get_busy())
        pygame.time.wait(1000)  #awaits for a sound to end

        self.laser_fx.play()
        self.assertTrue(pygame.mixer.get_busy())
        pygame.time.wait(1000)   ##awaits for a sound to end
        
if __name__ == '__main__':
    unittest.main()