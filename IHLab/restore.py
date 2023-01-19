import matlab
import matlab.engine
import os

# 通过高通滤波器
os.system('python highpass_filter.py')
print("finish high pass filter!\n")

# 解密
eng = matlab.engine.start_matlab()
h1 = eng.wavget(nargout=0)
print("finish wavget!\n")

# 调至低频
eng = matlab.engine.start_matlab()
h1 = eng.invDolphin(nargout=0)
print("finish to low\n")





