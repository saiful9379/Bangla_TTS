"""
@ Author : Saiful, Sagor
@ Email : saifulbrur79@gmail.com
"""
import os
import wget
root_dir = os.getcwd()

model_dict = {
    "male" : {
        "model_path" : "https://huggingface.co/bangla-speech-processing/bangla_tts_male/resolve/main/pytorch_model.pth",
        "config"     : "https://huggingface.co/bangla-speech-processing/bangla_tts_male/resolve/main/config.json"
        },
    "female" : {
        "model_path" : 'https://huggingface.co/bangla-speech-processing/bangla_tts_female/resolve/main/pytorch_model.pth',
        "config"     : "https://huggingface.co/bangla-speech-processing/bangla_tts_female/resolve/main/config.json"
    } 
}

def download_file(root_dir = "./", output_path="models", gender = "female"):
    path_dir = os.path.join(root_dir, output_path, gender)

    model_dir = os.path.join(path_dir, "pytorch_model.pth")
    config_dir = os.path.join(path_dir, "config.json")



    # print(model_dir)
    os.makedirs(path_dir, exist_ok=True)

    if os.path.exists(model_dir) and  os.path.exists(config_dir):
       print("model and config already exits")
    else:
        wget.download(model_dict[gender]["config"], out=path_dir)
        wget.download(model_dict[gender]["model_path"], out=path_dir)
    
    return model_dir, config_dir


if __name__ == "__main__":
  model_dir, config_dir = download_file(root_dir=root_dir)
