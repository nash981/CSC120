def update_output(out_string, encoded_tuple):
    return_str = ""
    offset = encoded_tuple[0]
    word_length = encoded_tuple[1]
    assert len(out_string) >=  offset
    if offset > word_length:
        offset_index = len(out_string) - offset
        return_str = out_string[offset_index:offset_index+word_length]
    elif offset == word_length:
        offset_index = len(out_string) - offset
        return_str = out_string[offset_index:]
    else:
        iters = int(word_length / offset)
        excess = word_length % offset
        return_str = out_string[len(out_string)-offset:]*iters + \
                     out_string[len(out_string)-offset:\
                                len(out_string)-offset+excess]
    return return_str
def unzip(input_stream):
    out_string = ""
    for i in range(len(input_stream)):
        assert type(input_stream[i]) is tuple or type(input_stream[i]) is str
        if type(input_stream[i]) is str:
            assert len(input_stream[i]) > 0
            out_string += input_stream[i]
        elif type(input_stream[i]) is tuple:
            assert len(input_stream[i]) == 2
            assert type(input_stream[i][0]) is int and input_stream[i][0] > 0
            assert type(input_stream[i][1]) is int and input_stream[i][1] > 0
            out_string += update_output(out_string, input_stream[i])
    return out_string

