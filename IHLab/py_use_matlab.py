import matlab
import matlab.engine

eng = matlab.engine.start_matlab()

t = eng.invDolphin(nargout=0)


print("finish")