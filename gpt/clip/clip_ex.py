import requests
from PIL import Image
import matplotlib.pyplot as plt

def image_grid(imgs, cols):
    rows = (len(imgs) + cols - 1) // cols
    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols * w, rows * h))

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid

image_urls = [
    'http://images.cocodataset.org/val2014/COCO_val2014_000000159977.jpg', # 기린
    'http://images.cocodataset.org/val2014/COCO_val2014_000000311295.jpg', # 얼룩말
    'http://images.cocodataset.org/val2014/COCO_val2014_000000457834.jpg', # 코끼리
    'http://images.cocodataset.org/val2014/COCO_val2014_000000555472.jpg', # 코끼리
    'http://images.cocodataset.org/val2017/000000039769.jpg', # 고양이
    'http://images.cocodataset.org/val2017/000000001000.jpg', # 사람
]

images = [Image.open(requests.get(url, stream=True).raw) for url in image_urls]

# 2x2 그리드 생성
grid = image_grid(images, 2)

# 이미지 표시
plt.figure(figsize=(10, 10))
plt.imshow(grid)
plt.axis('off')
plt.show()