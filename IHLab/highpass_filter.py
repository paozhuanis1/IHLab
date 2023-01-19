from matplotlib import pyplot
import thinkdsp
import thinkplot


# wave = thinkdsp.read_wave("output.wav")
# spectrum = wave.make_spectrum()
# spectrum.plot()
# thinkplot.show()

wave = thinkdsp.read_wave("mix.wav")
spectrum = wave.make_spectrum()
spectrum.high_pass(cutoff = 17000, factor = 0)
spectrum.plot()
thinkplot.show()
wave = spectrum.make_wave()
wave.write("high_mix.wav")

