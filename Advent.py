# group lines into chunks / sublists
from itertools import groupby

def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

def create_chunks_by_count(list_of_lines,n:int):
    '''
    create chunks from a list of lines based on the number lines in each chunk
    '''
    chunks = [list_of_lines[i * n:(i + 1) * n] for i in range((len(list_of_lines) + n - 1) // n )]
    return chunks
