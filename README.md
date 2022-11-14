# Guides on Profiling and Performance

## Goal

1. Give an overview with examples on how to benchmark the performance of research software
1. Provide a list of tools and approaches to increase the performance of research software


A high level introduction to performance optimization; when should you do it? How to proceed in a step by step manner?, etc. 
See ideas from relevant courses for this introduction text.


### Requirements analysis 

Discussing the following questions at the start can help you understand which performance optimization tools can be a better fit for your program.

- What is the type of the problem? Is it CPU bound or I/O bound?
- Do you expect users to be able to run the code on laptops? , or the software is meant to be run only on a supercomputer?


## Profiling

- Introduction paragraph on profiling as a first step in performance optimization of the code.
- When would you use profiling?
- Finding the limits: algorithm, software performance, hardware
- Use cases
- IDE specific tools (Jupyter, VS Code)
- Graphical output


### Resources

[Medium blog - Python profiling](https://medium.com/@antoniomdk1/hpc-with-python-part-1-profiling-1dda4d172cdf)

**CProfile**
- [Blog on Python profiling](https://medium.com/pragmatic-programmers/profiling-python-code-with-cprofile-87cd73875172)
- [Python Profilers](https://docs.python.org/3/library/profile.html)
- [cProfile example usage video](https://www.futurelearn.com/courses/python-in-hpc/3/steps/897734) 

[New Zealand eScience Infrastructure - Training on Performance and Profiling](https://nesi.github.io/perf-training/python-scatter)
[Real Python - Timer functions](https://realpython.com/python-timer/)
[Profiling with iPython magic commands](https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html)
[Dask profiling](https://docs.dask.org/en/stable/diagnostics-local.html)



### Examples to include

- Profile Python code implemented in the form of scripts from the command line using cProfile, timeit, timers, etc.
- Profile Python code in Jupyter notebook. 
- Example codes: calculation of pi, mandlebrot set, julia-set, MC simulation, Machie Learning, 
- GitHub Actions
- 

### Benchmarking
- [AirSpeedVelocity](https://asv.readthedocs.io/en/stable/index.html)
- [Numpy asv benchmarking example](https://numpy.org/devdocs/benchmarking.html)



### Training materials

[eScience Center - Parallel Programming in Python](https://carpentries-incubator.github.io/lesson-parallel-python/)
[Delft Blue Crash Course](https://doc.dhpc.tudelft.nl/delftblue/crash-course/)
[Aalto University - Parallel Computing](https://aaltoscicomp.github.io/python-for-scicomp/parallel/)

## Performance optimization

### Topics
- Introduction to optimizing research software
- When would you want to optimize the performance?
- Requirement analysis/Expectations
- Vectorization
- JIT with numba
- Compiling to C (Cython), interfacing with C/C++
- Parallel computing (Dask, MPI, OpenMP, multithreading)
- GPU acceleration (CuPy, Pycuda)
- DHPC


### Resources
- [eScience Center blog on Paralle programming](https://blog.esciencecenter.nl/parallel-programming-in-python-7fd62c90217d)


