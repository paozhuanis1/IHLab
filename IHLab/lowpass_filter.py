from matplotlib import pyplot
import thinkdsp
import thinkplot


# wave = thinkdsp.read_wave("lsb_high.wav")
# spectrum = wave.make_spectrum()
# spectrum.plot()
# thinkplot.show()

wave = thinkdsp.read_wave("Nxde.wav")
spectrum = wave.make_spectrum()
spectrum.low_pass(cutoff = 17000, factor = 0)
spectrum.plot()
thinkplot.show()
wave = spectrum.make_wave()
wave.write("pure_Nxde.wav")
# print("finish\n")
