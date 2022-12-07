from itertools import groupby
def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

# input parsing
input_file = 'day7\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]


n_unique_dirs = len(set([line for line in lines if line.startswith('dir ')]))

dirs = {}
#dir_contents = create_chunks_by_separator(lines_filtered,'$ ls')

current_dir = []
subdirs = []
subfiles = []
dir_name =''
for i in range(len(lines)):

    if lines[i].startswith('$ cd ..'): 
        #move out one level
        current_dir = current_dir[:len(current_dir)-1]
    elif lines[i].startswith('$ cd'):
        #move in one level
        current_dir.append(lines[i].split('$ cd ')[1])

    elif lines[i].startswith('$ ls'):
        # read and save dir content
        subfiles = []
        subdirs = []
        for j in range(i+1,len(lines)+1,1):
            
            if j == len(lines): #end of file
                dirs["/".join(current_dir)] = {"dirs":subdirs,"files":subfiles}
                break

            if lines[j].startswith('$'): #end of list
                dirs["/".join(current_dir)] = {"dirs":subdirs,"files":subfiles}
                break
            
            if lines[j].startswith('dir '): # dir
                subdir = "/".join(current_dir+[lines[j].split('dir ')[1]])
                subdirs.append(subdir)

            elif not lines[j].startswith('dir '): # file
                filesize, filename = lines[j].split(' ')
                filename_path = "/".join(current_dir+[filename])
                subfiles.append((int(filesize),filename_path))


# calculate dir sizes
dir_sizes = {}
dir_names_checked = {}
while len(dir_names_checked) < len(list(dirs.keys())): 
    for dir_name,dir_contents in dirs.items():
        dir_size = 0
        try:
            for file in dir_contents["files"]:
                dir_size += file[0]
                
            for subdir in dir_contents["dirs"]:
                dir_size += dir_sizes[subdir]

            dir_sizes[dir_name] = dir_size
            dir_names_checked[dir_name] = True
        except:
            continue
    
print(sum([val for val in dir_sizes.values() if val<=100000]))

tot_size = 70000000
free_space = tot_size - dir_sizes['/']
target_size = 30000000 - free_space
dirsize_names = list(dir_sizes.keys())
dirsize_values = list(dir_sizes.values())
target_list = [int(sz) - target_size for sz in dirsize_values]
best_value = min([elem for elem in target_list if elem >= 0]) + target_size
print(best_value)
