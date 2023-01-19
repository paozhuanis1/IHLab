DolphinAttack.m 将原音频调至高频
DolphinAttack_ganrao.m  将干扰调至高频
invDolphin.m  将音频调至低频
wavget.m  lsb解密
wavhide.m  lsb加密


add.py  叠加秘密音频和载体音频
Decoder.py  SR模型decode部分：根据不同的调制方法选择不同的预处理方式得到文本秘密信息
Encoder.py  SR模型encode部分：选择不同的调制方式生成加密音频
highpass_filter.py  高通滤波器
lowpass_filter.py  低通滤波器
Noise.py  叠加高斯噪音
py_use_matlab.py  python调用invDolphin.m还原高频音频，便于封装到SR模型Decoder部分
restore.py 封装高频解密部分，通过高通滤波器，lsb解密，调至低频
thinkdsp.py  开源音频处理库
thinkplot.py  开源音频处理库
tohigh.py  封装高频加密部分，将原音频和干扰调至高频，lsb加密，通过低通滤波器后叠加