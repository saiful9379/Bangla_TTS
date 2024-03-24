
# Bangla TTS
The Bangla TTS was training mono(male) speakers using Vit TTS model. The paper is ViT-TTS: Visual Text-to-Speech with Scalable Diffusion Transformer, we used the coqui-ai🐸-toolkit for Bangla Text-to-Speech training as well as inference.

__N.B : This pipeline only for inference as well as end point API testing purposes.__

__Please check the faster test into [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ea_BVSinWFy_9W2AH7NI55Ur0XO4Tr-a?usp=sharing)

# Requiremnts
Create Environments
```
conda create -n bn_tts python==3.8
conda activate bn_tts
```
Install require modules

```
pip install -r requirements.txt
```
# Dataset

Bangla Speech corpus prepared by the Indic TTS Team of IIT Madras. I've downsampled the dataset down to 22050 and converted the raw iitm annotation format into ljspeech format for training several TTS models for bangla.
in this dataset, i am sharing the final processed dataset for Bangla TTS along with trained best models weight files. please cite this paper: https://aclanthology.org/2020.lrec-1.789.pdf if you are using the dataset in your research works.

Dataset link: https://www.kaggle.com/datasets/mobassir/comprehensive-bangla-tts



# Training

Training code [jupyter](train_bangla_vits.ipynb) 


# Single Test[Inference]

For the single testing run,

```
python inference.py
```
or

Inference on [jupyter notebook](inference.ipynb)

[huggingface](https://huggingface.co/bangla-speech-processing/bangla_tts_female)


# End Point API
 For the API testing,

### 1. Run the ```app.py``` script
```
python app.py

```
### 2. Testing using python request
Write a .py script and run this code the audio .wav file will save into logs directory,

```
import os
import request
import time

username = "saiful"
text = "আপনি কেমন আছেন।"
log_dir = "logs"
filename = "audio_file_"+str(time.strftime("%Y%m%d-%H%M%S"))+".wav"
os.makedirs(log_dir, exist_ok= True)

file_dir = os.path.join(log_dir, filename)
# here use your localhost machine api or localhost and post 
url = 'http://192.168.1.154:8009/tts'

payload = {
    "sender": username, 
    "message": text
    }

payload = {
    "text" : text,
    "sender" : username,
    "save_dir" : file_dir
}
headers = {'content-type': 'application/json'} 
result = requests.post(url, json=payload, headers=headers)
print(result)

```

### 3. if want to use Postman skip the procedure 2

![alt text](image/api_for_tts.png)


# Reference

1. https://aclanthology.org/2020.lrec-1.789.pdf
2. https://arxiv.org/pdf/2106.06103.pdf
3. https://arxiv.org/abs/2005.11129
4. https://aclanthology.org/2020.emnlp-main.207.pdf
5. https://github.com/mobassir94




