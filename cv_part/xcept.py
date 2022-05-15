import urllib, os
from translate import Translator
from keras.applications.xception import Xception, preprocess_input, decode_predictions
from keras.preprocessing.image import load_img, img_to_array

translator= Translator(to_lang="en")
model = Xception()
dir_path = "D:/Пользователь/Артём Р/Downloads/info_search/info_srch/cv_part/images_cache"

def get_image_from_url(url):
    save_location = dir_path + '/{name}'.format(name=url.split('/')[-1])
    if(os.path.exists(save_location)):
        return save_location
    location, _ = urllib.request.urlretrieve(url, save_location)
    return location

def classify(url):
    try: 
        image = load_img(get_image_from_url(url), target_size=(299, 299))
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)
        prediction = decode_predictions(model.predict(image))
        most_probable_label = prediction[0][0][1]
        return translator.translate(most_probable_label.replace('_', ' '))
    except Exception as e:
        print(e)
        return ''
