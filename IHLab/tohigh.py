import matlab
import matlab.engine
import os

# 将原音频调至高频
eng = matlab.engine.start_matlab()
h1 = eng.DolphinAttack(nargout=0)
print("finish chinese48000!\n")

# 将干扰调至高频
eng = matlab.engine.start_matlab()
h2 = eng.DolphinAttack_ganrao(nargout=0)
print("finish ganrao!\n")

# lsb加密
eng = matlab.engine.start_matlab()
h3 = eng.wavhide(nargout=0)
print("finish lsb!\n")

# 通过低通滤波器
os.system('python lowpass_filter.py')
print("finish low_pass_filter!\n")

# 叠加

os.system('python add.py')
print("finish add!\n")





