from pydub import AudioSegment

sound1 = AudioSegment.from_wav(r'./lsb_high.wav')
sound2 = AudioSegment.from_wav(r'./pure_Nxde.wav')

output = sound1.overlay(sound2)  # 把sound2叠加到sound1上面
# output = sound1.overlay(sound2,position=5000)  # 把sound2叠加到sound1上面，从第5秒开始叠加
output.export("mix.wav", format = "wav")  # 保存文件