import requests
import numpy as np

from PIL import Image
from clip_interrogator import Config, Interrogator, LabelTable

# 1) LabelTable._load_cached 몽키패치
_orig_load_cached = LabelTable._load_cached
def _patched_load_cached(self, desc, hash, sanitized_name):
    # 원본 호출 (self.embeds가 여기서 채워지거나 빈 상태로 유지됨)
    result = _orig_load_cached(self, desc, hash, sanitized_name)
    # MPS에서도 self.embeds를 float32로 통일
    # (원본이 캐시를 성공해 self.embeds를 numpy array list로 채웠다면,
    # 혹은 후속에 이어서 float16으로 채워질 때도 모두 float32로 변환)
    if hasattr(self, "embeds") and isinstance(self.embeds, list):
        self.embeds = [e.astype(np.float32) for e in self.embeds]
    return result

LabelTable._load_cached = _patched_load_cached

image_url = 'http://images.cocodataset.org/val2014/COCO_val2014_000000159977.jpg'

response = requests.get(image_url, stream=True)
image = Image.open(response.raw).convert('RGB')

ci = Interrogator(Config(
    clip_model_name="ViT-L-14/openai",
    device="mps" # MPS 사용 - 빠름
))

caption = ci.interrogate(image)
print(caption)
