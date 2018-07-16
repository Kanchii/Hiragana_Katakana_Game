def loadImages(IMAGE_PATH):
    import os
    all_images = [(IMAGE_PATH + x) for x in os.listdir(IMAGE_PATH)
        if os.path.isfile(os.path.join(IMAGE_PATH, x)) and x[-3:] != 'jpg']
    return all_images

def getRandomImage(all_images, IMAGE_PATH):
    import random
    if(len(all_images) == 0):
        return IMAGE_PATH + "completed.jpg"
    select_image = random.choice(all_images)
    all_images.remove(select_image)
    return select_image
