"""
@Author : Saiful Islam
@Email : saifulbrur79@gmail.com
"""
import re
import os
import torch
import bangla
import base64
from IPython.display import Audio 
import soundfile as sf
from bnnumerizer import numerize
from bnunicodenormalizer import Normalizer
from modules.model_download import download_file
from modules.synthsizer import Synthesizer 
bnorm=Normalizer()
root_dir = os.getcwd()

use_cuda = True
DEBUG_SAVE = True

# set pretrain model female or male
DEBUG_GENDER = ["female", "male"]
GENDER = DEBUG_GENDER[1]

def model_loading(model_path=None, config_path=None):
    tts_bn_model=Synthesizer(
        model_path,
        config_path,
        use_cuda = use_cuda
    )
    return tts_bn_model

def normalize(sen):
    _words = [bnorm(word)['normalized']  for word in sen.split()]
    return " ".join([word for word in _words if word is not None])

def bangla_tts(model:object=None, text = "আমি বাংলা শিখেছি",is_male = True, is_e2e_vits = True, log_dir = "logs/unknown.wav"):
    '''
      params:
        text : input bangla text that needs to be synthesized.
        is_male : if True then uses cloned voice of male speaker,otherwise female speaker is used.
        is_e2e_vits : if True then uses vits model,otherwise glowtts gets used.

    '''
    if(text[-1] != '।'):
      text += '।'
    # english numbers to bangla conversion
    res = re.search('[0-9]', text)
    if res is not None:
      text = bangla.convert_english_digit_to_bangla_digit(text)
    
    #replace ':' in between two bangla numbers with ' এর '
    pattern=r"[০, ১, ২, ৩, ৪, ৫, ৬, ৭, ৮, ৯]:[০, ১, ২, ৩, ৪, ৫, ৬, ৭, ৮, ৯]"
    matches=re.findall(pattern,text)
    for m in matches:
        r=m.replace(":"," এর ")
        text=text.replace(m,r)
    try:
        text=numerize(text)
    except:
        pass
    text = normalize(text)
    sentenceEnders = re.compile('[।!?]')
    sentences = sentenceEnders.split(str(text))
    audio_list = []
    for i in range(len(sentences)):
      if(not sentences[i]):
        continue
      text = sentences[i]+'।'
      audio_list.append(torch.as_tensor(model.tts(text)))
    audio = torch.cat([k for k in audio_list])
    numpy_audio = audio.detach().cpu().numpy()
    return numpy_audio

if __name__ == "__main__":

  text = 'রওশন এরশাদের সঙ্গে দেখা করলেন জিএম কাদের।'
  fileName = 'logs/test_male.wav'
   
  print("Model Downloading : .......")
  model_path, config_path = download_file(
    root_dir=root_dir, 
    output_path="models", 
    gender=GENDER
    )
  print("Done")

  tts_bn_model = model_loading(
    model_path=model_path, 
    config_path=config_path
    )
  audio= bangla_tts(
     model= tts_bn_model, 
     text = text, 
     is_male = False, 
     is_e2e_vits = True
     )
  

  if DEBUG_SAVE:
    sf.write(fileName, audio, 22050)
  # 22050
  # Audio(fileName, autoplay=True)
