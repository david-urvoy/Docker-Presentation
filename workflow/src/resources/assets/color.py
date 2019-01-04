HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def decorate(pattern, callback):
    global style
    if callback == None:
        return lambda *args: f"{pattern}{style(*args)}"
    return lambda *args: f"{pattern}{callback(*args)}"

def style(*args):
    global ENDC
    return f"{' '.join(args)}{ENDC}"

def bold(callback = None):
    global BOLD, decorate
    return decorate(BOLD, callback)

def underline(callback = None):
    global UNDERLINE, decorate
    return decorate(UNDERLINE, callback)

def color(color):
    global decorate
    return lambda callback=None: decorate(color, callback)

[red, blue, green, yellow, pink] = [color(color_pattern) for color_pattern in [FAIL, OKBLUE, OKGREEN, WARNING, HEADER]]

[redt, bluet, greent, yellowt, pinkt] = [bold(underline(color)) for color in [red(), blue(), green(), yellow(), pink()]]
