from memory_profiler import profile
import gc
import array


@profile(precision=8)
def readfilemisc():
    with open("experiments/sampledata/lipsum-20word.txt", encoding='utf-8') as f:
        read_n_chars: str = f.read(10) # read n characters

        for line in f:
            s:str = line.strip() 
        a = [i for i in range(100000)]
        # print("size of file obj: ", sys.getsizeof(f))
        b = array.array('i', [i for i in range(100000)])
        
        
        # print(f.closed)
        f.close()
        # print(f.closed)


readfilemisc()