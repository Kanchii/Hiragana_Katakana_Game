def loadImages(hiragana, katakana, kanji):
    import os
    all_images = []
    if(hiragana):
        all_images += [("Images/Hiragana/" + x, x[:-4]) for x in os.listdir("Images/Hiragana/")
            if os.path.isfile(os.path.join("Images/Hiragana/", x))]
    if(katakana):
        all_images += [("Images/Katakana/" + x, x[:-4]) for x in os.listdir("Images/Katakana/")
            if os.path.isfile(os.path.join("Images/Katakana/", x))]
    if(kanji):
        all_images += [("Images/Kanji/" + x, x[:-4]) for x in os.listdir("Images/Kanji/")
            if os.path.isfile(os.path.join("Images/Kanji/", x))]
    return all_images

def getRandomImage(all_images):
    import random
    if(len(all_images) == 0):
        return ("Images/completed.jpg", "completed")
    select_image = random.choice(all_images)
    all_images.remove(select_image)
    return select_image
