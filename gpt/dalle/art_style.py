from IPython.display import Image, display

from gpt.dalle.select_artist import apply_custom
from gpt.get_client import client

# style = apply_custom('art_style.txt')
style = apply_custom('other_style.txt')

prompt = f"fighting two heroes which have supernatural power with {style}."
kwargs = { "prompt": prompt }

im = client.images.generate(**kwargs)
print(im.data[0].url)
display(Image(url=im.data[0].url))