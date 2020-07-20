import preprocessing
import matplotlib.pyplot as plt
from model import GAN
import pickle

with open('animelist', 'rb') as f:
    images = pickle.load(f)


gan = GAN()
gan.train(images, epochs=15001, batch_size=256, save_images=1000, save_model=15000)

