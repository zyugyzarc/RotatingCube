# ROTATING CUBE
made this while i was bored.

# Setup
1. `$ git clone https://github.com/zyugyzarc/RotatingCube && cd RotatingCube`
2. `$ pip3 install cython numpy`
3. `$ python3 compile.py build_ext --inplace`
4. `$ python3 cube.py`

runing cube.py shows a cube. (make sure your terminal's size is atleast 155 lines and 50 chars wide)


# info (what is going on with all these files?)

main.py contains the main framework for drawing images (using points and lines) onto a terminal screen

render.pyx contains the cython code for making point() and line() faster.

compile.py compiles render.pyx into render.\*.so (on \*NIX) or render.\*.pyd (on windows)
