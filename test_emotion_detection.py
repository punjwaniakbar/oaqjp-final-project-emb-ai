import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_dominant_emotion_joy(self):
        emotions = emotion_detector("I am glad this happened")
        self.assertEqual(emotions["dominant_emotion"], "joy")

    def test_dominant_emotion_anger(self):
        emotions = emotion_detector("I am really mad about this")
        self.assertEqual(emotions["dominant_emotion"], "anger")

    def test_dominant_emotion_disgust(self):
        emotions = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotions["dominant_emotion"], "disgust")

    def test_dominant_emotion_sadness(self):
        emotions = emotion_detector("I am so sad about this")
        self.assertEqual(emotions["dominant_emotion"], "sadness")

    def test_dominant_emotion_fear(self):
        """ Test dominant emotion: fear """
        emotions = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotions["dominant_emotion"], "fear")

if __name__ == '__main__':
    unittest.main()