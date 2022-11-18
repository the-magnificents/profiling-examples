cProfile generates statistics of the entire program listing the time spent in different fucntions in the program. This is useful to get an overview of the mos time consuming sections of the program.


### Profile the mandelbrot set program using cProfile

Python -m cprofile -o mandel.dat mandel_main.py