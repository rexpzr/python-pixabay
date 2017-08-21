from unittest import TestCase
from python_pixabay import Pixabay

import os

pix = Pixabay(os.environ["PIXABAY_KEY"])

class python_pixabay_testcase(TestCase):
    def test_image_search(self):
        self.assertIn("hits", pix.image_search())

    def test_video_search(self):
        self.assertIn("hits", pix.video_search())

    def test_custom_image_search(self):
        self.assertIn("hits", pix.image_search(q="water"))

    def test_custom_video_search(self):
        self.assertIn("hits", pix.video_search(q="water"))
    
