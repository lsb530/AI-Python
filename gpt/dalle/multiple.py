from IPython.display import Image, display
from gpt.get_client import client

prompt = "A beautiful landscape."
n = 3

kwargs = {
    "prompt": prompt,
    "n": n
}

im = client.images.generate(**kwargs)
print(im)

for i in range(n):
    print(im.data[i].url)
    display(Image(url=im.data[i].url))
