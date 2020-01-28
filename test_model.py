# YOUR BACKEND TESTS HERE
from PIL import Image
import model


def test_bar_chart():
    bio = model.matches_plot()
    bio.seek(0)
    Image.open(bio).show()
