from wordcloud import WordCloud
import numpy as npy
from PIL import Image

def main():
    dataset = read_words_file()

    generate_word_cloud(dataset)

def read_words_file():
    words_list = open("./resources/wordsList.txt", "r").read()
    words_list_lowercase = words_list.lower()

    return words_list_lowercase

def generate_word_cloud(words_list):
    cloud_mold = npy.array(Image.open("./resources/cloud.jpg"))
    
    cloud = WordCloud(background_color = "white", mask = cloud_mold)
    cloud.generate(words_list)
    cloud.to_file("./results/word_cloud.png")


main()