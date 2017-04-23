from unittest import TestCase
from python_pixabay import Pixabay

import os

pix = Pixabay(os.environ["PIXABAY_KEY"])

class python_pixabay_testcase(TestCase):
    def test_image_search(self):
        self.assertTrue(pix.image_search())

    def test_video_search(self):
        self.assertTrue(pix.video_search())
    
