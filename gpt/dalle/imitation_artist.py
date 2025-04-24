from IPython.display import Image, display

from gpt.dalle.select_artist import apply_custom
from gpt.get_client import client

artist = apply_custom('artist_painters_photographers.txt')

prompt = f"A beautiful landscape by {artist}."
kwargs = { "prompt": prompt }

im1 = client.images.generate(**kwargs)
print(im1.data[0].url)
display(Image(url=im1.data[0].url))

prompt = f"A cute smile dog by {artist}."
kwargs = { "prompt": prompt }

im2 = client.images.generate(**kwargs)
print(im2.data[0].url)
display(Image(url=im2.data[0].url))