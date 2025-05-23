#!/usr/bin/env python3

def output_func(inp_file, out_file):
    if inp_file is None or out_file is None:
        print("Need Valid File")
        pass
    with open(inp_file, 'r') as fi, open(out_file, 'w') as fo:
        for i, baris in enumerate(fi):
            fo.write(f"{i+1}. {baris}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 2:
        print("need 2 params!")
    else:
        output_func(inp_file=sys.argv[1], out_file=sys.argv[2])