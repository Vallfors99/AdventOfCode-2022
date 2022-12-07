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

subdirs = []
subfiles = []
dir_name =''
for i in range(len(lines)):
    if lines[i].startswith('$ ls'):
        dir_name = lines[i-1].split('$ cd ')[1]

        subdirs = []
        subfiles = []

        for j in range(i+1,len(lines),1):
            if lines[j].startswith('dir'):
                subdirs.append(lines[j].split('dir ')[1])
            elif not lines[j].startswith('$'):
                subfiles.append(lines[j])
            else:
                break
            
        if dir_name in dirs:
            print(f'dir name: {dir_name}')
            print(f'content: {dirs[dir_name]}')
            new_content =  {"subdirs":subdirs, "subfiles":subfiles}
            print(f'new content: {new_content}')
        dirs[dir_name] = {"subdirs":subdirs, "subfiles":subfiles}

# add last dir
if len(subdirs) or len(subfiles):
    dirs[dir_name] = {"subdirs":subdirs, "subfiles":subfiles}
# sort dir from most inner to most outer    
dirs = dict(sorted(dirs.items(), key=lambda item: len(item[1]["subdirs"])))

# calculate dir sizes
dir_sizes = {}
dir_names_checked = {}
while len(dir_names_checked) < len(list(dirs.keys())): 
    for dir_name,dir_contents in dirs.items():
        dir_size = 0
        if dir_name not in dir_names_checked:
            try:
                for file in dir_contents["subfiles"]:
                    dir_size += int(file.split(' ')[0])
                for subdir in dir_contents["subdirs"]:
                    dir_size += dir_sizes[subdir]
                dir_sizes[dir_name] = dir_size
                dir_names_checked[dir_name] = True
            except:
                continue
print(sum([val for val in dir_sizes.values() if val<=100000]))