import base64
from io import BytesIO

from IPython.display import Image, display

from gpt.get_client import client

image = open("without_mask.png", "rb")
mask = open("mask.png", "rb")

prompt = "A group of people hiking in green forest between trees"
# prompt = "A cute girl smiling in green forest between trees. vivid human face"
n = 1
size = "1024x1024"

kwargs = {
    "image": image,
    "mask": mask,
    "prompt": prompt,
    "n": n,
    "size": size,
}

response = client.images.edit(**kwargs)
image_url = response.data[0].url
print(image_url)
display(Image(url=image_url))

### 아래는 파일 저장
# kwargs = {
#     "image": image,
#     "mask": mask,
#     "prompt": prompt,
#     "n": n,
#     "size": size,
#     "response_format": "b64_json"
# }
#
# response = client.images.edit(**kwargs)
# b64_json = response.data[0].b64_json
# img_bytes = base64.b64decode(b64_json)
#
# with open('edited.png', 'wb') as f:
#     f.write(img_bytes)