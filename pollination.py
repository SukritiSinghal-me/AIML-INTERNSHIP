import requests
import io
from PIL import image
import random


def generate_image(prompt) :
    seed = random.randint(1,10000)

url = f""