from itertools import zip_longest

def cmd(arr, *args):
    return f''' >>> {" ".join([x.__str__() for x in join(arr, *args)])}
    '''

def join(arr, *args):
    return arr[:-1] + list(args) + arr[-1:]

def merge(*args):
    merged = list(zip_longest(*args, fillvalue=""))
    return '\n'.join([''.join(l) for l in merged])

def container(style, template):
    '''
    style: style functions that can be found in color.py
    template: multiline string that represents the container
    '''
    return [style(line) for line in template.splitlines()]
