from gpt.get_client import client

kwargs = {
    "prompt": "A beautiful landscape."
}

im = client.images.generate(**kwargs)
print(im)