import os

# Parent Directory path
parent_dir = "C:/Users/46703/Documents/Programming/AdventOfCode-2022/"

days_to_build = range(4,24+1)
for day in days_to_build:
    # create folder
    directory = f'day{day}'
    path = os.path.join(parent_dir, directory)
    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory '% s' created" % directory)

    # create empty input file
    dir_input = f'day{day}/input.txt'
    path = os.path.join(parent_dir, dir_input)
    if not os.path.exists(path):
        with open(path,'w') as outfile:
            print("input file '% s' created" % dir_input)

    # create step 1 python file
    dir_pyfile = f'day{day}/part_1.py'
    path = os.path.join(parent_dir, dir_pyfile)
    if not os.path.exists(path):
        with open(path,'w') as outfile:
            file_content = f"# input parsing\ninput_file = 'day{day}\input.txt'\nwith open(input_file) as infile:\n    lines = [line.strip() for line in infile]"
            outfile.write(file_content)
            print("python file '% s' created" % dir_pyfile)

    # create step 2 python file
    dir_pyfile = f'day{day}/part_2.py'
    path = os.path.join(parent_dir, dir_pyfile)
    if not os.path.exists(path):
        with open(path,'w') as outfile:
            file_content = f"# input parsing\ninput_file = 'day{day}\input.txt'\nwith open(input_file) as infile:\n    lines = [line.strip() for line in infile]"
            outfile.write(file_content)
            print("python file '% s' created" % dir_pyfile)

