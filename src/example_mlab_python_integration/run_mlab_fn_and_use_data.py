import matlab.engine
import os, inspect

eng = matlab.engine.start_matlab()

# NOTE: You'll have to use this to get the directory of the currently executing file
curdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory

# Then change into the directory of this file in order to access matlab functions located in the same directory
eng.cd(curdir)

a = eng.triarea(2, 3)

# Matlab types are exported by default, but there are built in castes to use including to numpy.
# I imagine that we would sooner trigger matlab to write out image files rather than try to pass data directly,
# but it is both possible and well documented.
# https://www.mathworks.com/help/matlab/matlab_external/handle-data-returned-from-matlab-to-python.html
a = int(a)

print a

# Make sure to clean up after yourself lest you have dangling headless matlab processes
eng.quit()
