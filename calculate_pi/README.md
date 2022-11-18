Measuring execution times of small programs such as pi calculation can be done 
using the timeit module.

### Using timeit in jupyter notebook

Use the %timeit magic command


### Using timeit from the command line

python -m timeit -s "from claculate_pi import calculate_pi" "calculate_pi(100000)"