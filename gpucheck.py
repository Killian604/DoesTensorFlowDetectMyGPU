from tensorflow import test
from tensorflow.python.client import device_lib

print("\nGPU is available:", test.is_gpu_available())
print()
print(device_lib.list_local_devices())
