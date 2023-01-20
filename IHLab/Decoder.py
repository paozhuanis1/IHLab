# -*- coding: utf-8 -*-
import wave
import requests
import base64
import numpy as np
import struct
import scipy.io.wavfile
from tqdm import tqdm
import os

framerate = 16000  # 采样率
num_samples = 2000  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
FILEPATH = './音频2/secret1.wav'

base_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
# 百度语音识别API需申请，将所得密钥替换APIKey和SecretKey
APIKey = "*******"
SecretKey = "*******"

HOST = base_url % (APIKey, SecretKey)


def getToken(host):
    res = requests.post(host)
    return res.json()['access_token']


def save_wave_file(filepath, data):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()


def get_audio(file):
    with open(file, 'rb') as f:
        data = f.read()
    return data


def speech2text(speech_data, token, dev_pid=1537):
    FORMAT = 'wav'
    RATE = '16000'
    CHANNEL = 1
    CUID = '*******'
    SPEECH = base64.b64encode(speech_data).decode('utf-8')

    data = {
        'format': FORMAT,
        'rate': RATE,
        'channel': CHANNEL,
        'cuid': CUID,
        'len': len(speech_data),
        'speech': SPEECH,
        'token': token,
        'dev_pid': dev_pid
    }
    url = 'https://vop.baidu.com/server_api'
    headers = {'Content-Type': 'application/json'}
    # r=requests.post(url,data=json.dumps(data),headers=headers)
    print('正在识别...')
    r = requests.post(url, json=data, headers=headers)
    Result = r.json()
    if 'result' in Result:
        return Result['result'][0]
    else:
        return Result


def key_to_sampling_frequency(key):
    key = int(float(key))
    fs = key / 123
    fs = str(fs)
    return fs


def decoder(infile, outfile, key):  # 音频预处理模块，放在整个SR模型最前面\
    print("正在解码音频：", infile)
    f = scipy.io.wavfile.read(infile)
    waveData = np.frombuffer(f[1], dtype=np.int16)  # 将原始字符数据转换为整数

    # 音频数据归一化
    maxW = max(abs(waveData))
    waveData = waveData * 1.0 / maxW
    outData = waveData

    outwave = wave.open(outfile, 'wb')
    nchannels = 1
    sampwidth = 2
    fs = key_to_sampling_frequency(key)
    data_size = len(outData)
    framerate = int(float(fs))
    nframes = data_size
    comptype = "NONE"
    compname = "nt compressed"
    outwave.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))

    for v in tqdm(outData):
        outwave.writeframes(struct.pack('h', int(v * 64000 / 2)))

    outwave.close()

1
def dolphin_decode():
    os.system('python restore.py')


if __name__ == '__main__':
    infile = './out_temp.wav'
    method = input('请输入预处理方法：（1代表低频预处理，2代表高频预处理）\n')
    if method == '2':
        dolphin_decode()
        infile = './get_secret2.wav'
    elif method == '1':
        # infile = './out_temp.wav'
        infile = './get_secret2.wav'
    # outfile = './音频2/temp.wav'
    # key = input('请输入解码密钥：\n')
    # decoder(infile, outfile, key) # 音频预处理模块

    devpid = 1536
    TOKEN = getToken(HOST)
    speech = get_audio(infile)
    result = speech2text(speech, TOKEN, int(devpid))
    print('秘密信息为：', result)
    # os.remove(outfile)
