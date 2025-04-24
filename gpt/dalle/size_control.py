from IPython.display import Image, display
from gpt.get_client import client

prompt = "A beautiful landscape."
n = 1
size = "256x256"

kwargs = {
    "prompt": prompt,
    "n": n,
    "size": size
}

im = client.images.generate(**kwargs)

for i in range(n):
    print(im.data[i].url)
    display(Image(url=im.data[i].url))
