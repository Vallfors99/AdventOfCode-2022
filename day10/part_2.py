def add_pixel_to_crt(pixel_idx,row_idx,crt_rows):
    '''
    adds a pixel to the crt rows
    '''
    crt_rows[row_idx][pixel_idx] = '#'
    print("".join(crt_rows[row_idx]))

input_file = "input.txt"
with open(input_file) as infile:
    lines = [line.strip() for line in infile]
lines = [l.split(' ') for l in lines]
register_val = [1]
crt_rows = [["." for i in range(40)] for j in range(6)]

# create crt output
crt_row_idx = 0
for command_val in lines:

    if len(command_val) ==1 and command_val[0] == "noop": #1 cycle, no change in register val
        # first and only cycle
        pixel_idx = ((len(register_val)-1)%len(crt_rows[0]))
        row_idx = len(register_val)//len(crt_rows[0])

        print(f'pixel idx: {pixel_idx}, sprite value: {register_val[-1]}')
        if abs(register_val[-1] - pixel_idx) <=1:
            add_pixel_to_crt(pixel_idx,row_idx,crt_rows)
        register_val.append(register_val[-1])

    else: # two cycles
        command,val = command_val
        val = int(val)

        # first cycle
        pixel_idx = ((len(register_val)-1)%len(crt_rows[0]))
        row_idx = len(register_val)//len(crt_rows[0])
        print(f'pixel idx: {pixel_idx}, sprite value: {register_val[-1]}')
        if abs(register_val[-1] - pixel_idx) <=1:
            add_pixel_to_crt(pixel_idx,row_idx,crt_rows)
        register_val.append(register_val[-1])

        # second cycle
        pixel_idx = ((len(register_val)-1)%len(crt_rows[0]))
        row_idx = len(register_val)//len(crt_rows[0])
        print(f'pixel idx: {pixel_idx}, sprite value: {register_val[-1]}')
        if abs(register_val[-1] - pixel_idx) <=1:
            add_pixel_to_crt(pixel_idx,row_idx,crt_rows)
        register_val.append(register_val[-1]+val)

# print results
print("")
for row in crt_rows:
    print("".join(row))
