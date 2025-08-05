from tensorflow.keras.preprocessing import image # type: ignore
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input # type: ignore
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input# type: ignore
from tensorflow.keras.models import Model # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from helpers import word_for_id

def extract_features(img_path):
    model = MobileNetV2(weights='imagenet')
    model = Model(model.input, model.layers[-2].output)
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    features = model.predict(img, verbose=0)
    return features

def generate_caption(model, tokenizer, photo, max_length):
    in_text = 'startseq'
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = word_for_id(yhat, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'endseq':
            break
    final_caption = in_text.replace('startseq', '').replace('endseq', '').strip()
    return final_caption
