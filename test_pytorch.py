import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("CUDA device count:", torch.cuda.device_count())
    print("Current CUDA device:", torch.cuda.current_device())
    print("CUDA device name:", torch.cuda.get_device_name(torch.cuda.current_device()))
    print("GPU name:", torch.cuda.get_device_name(0))
    # 실제로 텐서를 GPU에 올려서 연산 테스트
    x = torch.rand(3, 3).cuda()
    y = torch.rand(3, 3).cuda()
    z = x + y
    print("Tensor on GPU:", z)
else:
    print("GPU를 사용할 수 없습니다.")