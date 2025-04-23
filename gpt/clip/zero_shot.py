from platform import processor
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

import torch
import requests
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

# 기린, 얼룩말, 코끼리
classes = ['giraffe', 'zebra', 'elephant']

# 모델과 프로세서 로드
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 텍스트와 이미지 전처리 & 모델 입력 형식 변환
inputs = processor(text=classes, images=images, return_tensors="pt", padding=True)

# 모델을 통해 이미지-텍스트 유사도 계산
outputs = model(**inputs)

# 이미지-텍스트 유사도 점수 추출
logits_per_image = outputs.logits_per_image

# 소프트맥스로 확률 분포 변환
probs = logits_per_image.softmax(dim=1)

# 확률을 소수점 2자리로 반올림하여 출력
print(torch.round(probs, decimals=2))