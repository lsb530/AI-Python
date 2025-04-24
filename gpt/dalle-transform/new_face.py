from gpt.get_client import client

image = open("ori_face_image.png", "rb")
n = 3
size = "1024x1024"

kwargs = {
    "image": image,
    "n": n,
    "size": size,
}

response = client.images.create_variation(**kwargs)
print(response)
