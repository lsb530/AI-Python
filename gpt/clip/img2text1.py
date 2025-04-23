import requests
from PIL import Image
from clip_interrogator import Config, Interrogator

image_url = 'http://images.cocodataset.org/val2014/COCO_val2014_000000159977.jpg'

image_path = 'image01.jpg'
response = requests.get(image_url, stream=True)
image = Image.open(response.raw).convert('RGB')

ci = Interrogator(Config(
    clip_model_name="ViT-L-14/openai",
    device="cpu" # CPU 사용 - 느림
))

print(ci.interrogate(image))