
def str_to_codes(text, mapping):
    encoding_list = []
    char_list = list(text)
    for characters in char_list:
        encoding_list.append(mapping[characters])
    encoding_list.append(mapping["<END>"])
    return encoding_list


def codes_to_chunks(codes):
    chunk_list = []
    code_string = "".join(codes)
    code_string += (8 - len(code_string) % 8)*"0"
    for i in range(int(len(code_string)/8)):
        chunk_list.append(code_string[i*8:(i+1)*8])
    return chunk_list


def print_chunks_as_decimal(chunks):
    for i in range(len(chunks)):
        chunks[i] = str(int(chunks[i], 2))
    print_str = " ".join(chunks)
    print(print_str)


def ints_to_bits(vals):
    for i in range(len(vals)):
        vals[i] = str(bin(vals[i]))
        vals[i] = vals[i][2:]
        if len(vals[i]) != 8:
            vals[i] = (8 - len(vals[i]) % 8)*"0" + vals[i]
    print_str = "".join(vals)
    return print_str


def bits_to_str(bits, root):
    out_str = []
    curr = root
    type(bits)
    for i in range(len(bits)):
        if bits[i] == "0":
            if type(curr.left) is str:
                out_str.append(curr.left)
                curr = root
            else:
                curr = curr.left
        elif bits[i] == "1":
            if type(curr.right) is str:
                out_str.append(curr.right)
                curr = root
            else:
                curr = curr.right
        if out_str != [] and out_str[-1] == "<END>":
            out_str = out_str[:-1]
            return "".join(out_str)




