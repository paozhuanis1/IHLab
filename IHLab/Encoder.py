import wave
import numpy as np
import struct
import scipy.io.wavfile
from tqdm import tqdm
import os


def Whale(infile, outfile):
    f = scipy.io.wavfile.read(infile)
    key = f[0] * 123
    nframes = len(f[1])
    waveData = np.frombuffer(f[1], dtype=np.int16)  # 将原始字符数据转换为整数
    # 音频数据归一化
    maxW = max(abs(waveData))
    waveData = waveData * 1.0 / maxW
    # f.close()

    outData = waveData
    outwave = wave.open(outfile, 'wb')
    nchannels = 1
    sampwidth = 2
    fs = 40
    data_size = len(outData)
    framerate = int(fs)
    nframes = data_size
    comptype = "NONE"
    compname = "nt compressed"
    outwave.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))

    print('正在对音频：', infile, '进行鲸鱼加密...')

    for v in tqdm(outData):
        outwave.writeframes(struct.pack('h', int(v * 64000 / 2)))

    outwave.close()
    print('加密结束！生成鲸鱼加密音频：', outfile)


def Dolphin():
    os.system('python ../toHigh/tohigh.py')


if __name__ == '__main__':
    infile = './Aorin.wav'  # 我们想要加密的音频信息
    outfile = './out_temp.wav'  # 输出的加密音频
    method = input('请输入调制方法：（1代表鲸鱼调制，2代表海豚调制）\n')

    if method == '1':
        Whale(infile, outfile)

    elif method == '2':
        Dolphin()
        # Dolphin(infile, outfile)
    else:
        print('识别错误，请输入“1”或者“2”！')
