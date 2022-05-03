import time


def merge(in1, in2, output):
    """merges two input arrays into an output array
       in1,in2 - input arrays, we assume both are sorted
       output  - output array, contents are junk
    """
    start = time.time()
    assert len(output) == len(in1) + len(in2)
    pos1 = 0
    pos2 = 0
    while pos1 < len(in1) and pos2 < len(in2):
        if in1[pos1] <= in2[pos2]:
            output[pos1 + pos2] = in1[pos1]
            pos1 += 1
        else:
            output[pos1 + pos2] = in2[pos2]
            pos2 += 1
    while pos1 < len(in1):
        output[pos1 + pos2] = in1[pos1]
        pos1 += 1
    while pos2 < len(in2):
        output[pos1 + pos2] = in2[pos2]
        pos2 += 1
    end = time.time()
    print(end-start)
    assert pos1 + pos2 == len(output)

in1 = []
in2 = []
out =[]

for i in range(1000000000):
    in1.append(i)
    in2.append(i)
output = in1+in2

merge(in1, in2, output)