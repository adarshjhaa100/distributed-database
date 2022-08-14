import json


with open("experiments/sampledata/lipsum-20word.txt",\
    mode = 'rb') as f:

    read_n_chars: str = f.read(10) # read n characters

    print(read_n_chars, len(read_n_chars))
    # gc.collect()

    # Fast, memory efficient iteration over each line
    for line in f:
        print(line)
        print(f.tell()) # pull in the correct position
    print("This will actually reach end of the line",f.tell())   
    # print(f.seekable())
    # seek to nth posn from the current one , second param is whence 
    # which requires file to be open in binary mode
    
    print(f.seek(8)) # seek from the beginning (whence = 0)

    # f.read, reads one character and moves the line forward
    for i in range(10):
        print(f.read(1), f.tell())

    print(f.tell())
    print(f.seek(-3,1)) # seek from the current
    print(f.seek(0, 2)) # seek 0 chars from the end (to the end), length of file
    print(f.seek(-3, 2)) # seek from the end
    print(f.tell())

    
    myobj = {"name":"Heisenberg", 
             "org":"WW Inc.", 
              "age":60}

    print(json.dumps(myobj))

    f.close()

