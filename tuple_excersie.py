#this is a program for calculate miden and avrage to tuple

def c_mid_avg(your_tuple):
    import numpy
    avg = sum(your_tuple)/len(your_tuple)
    median = numpy.median(numpy.array(your_tuple))
    return avg, median