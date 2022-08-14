
import tracemalloc
from array import array

tracemalloc.start()

with open("experiments/sampledata/lipsum-20word.txt", encoding='utf-8') as f:
    read_n_chars: str = f.read(10) # read n characters

    # print(read_n_chars, len(read_n_chars))
    # gc.collect()
    # Fast, memory efficient iteration over each line
    for line in f:
        s:str = line.strip()

    a = [float(i) for i in range(100000)]
    b = array('f', [float(i) for i in range(100000)])
    
    # gc.collect()
    # print("size of file obj: ", sys.getsizeof(f))

    

    # print(f.closed)
    f.close()
    # print(f.closed)




# take snapshot and print out the top ten lines
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
