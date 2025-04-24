from IPython.display import Image, display

from gpt.get_client import client

image = open("dog01.png", "rb")
n = 2
size = "1024x1024"

kwargs = {
    "image": image,
    "n": n,
    "size": size,
}

response = client.images.create_variation(**kwargs)
urls = response.data

for i in range(n):
    img_url = urls[i].url
    print(img_url)
    display(Image(url=img_url))
