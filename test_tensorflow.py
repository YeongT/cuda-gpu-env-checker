import tensorflow as tf

print("TensorFlow version:", tf.__version__)

gpus = tf.config.list_physical_devices('GPU')
print("Available GPUs:", gpus)

# GPU 사용 가능 여부 및 이름 출력
if gpus:
    print("GPU detected:", gpus)
else:
    print("GPU를 사용할 수 없습니다.")