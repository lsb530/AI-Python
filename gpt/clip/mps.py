import torch
print(torch.backends.mps.is_available())  # MPS 사용 가능 여부
print(torch.backends.mps.is_built())      # MPS 지원 여부

if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

# Example tensor creation
x = torch.randn(1, device=device)
print(x)