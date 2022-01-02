PONCTUATION_SIGNS = ["!", '"', "'", ")", "(", ",", ".", ";", ":", "?", "-", "_", "«", "»", "..."]


def format_line(line, remove_ponctuation=True):
    line = line.rstrip().lower() 
    if remove_ponctuation:
        for p in PONCTUATION_SIGNS:
            line = line.replace(p, " ")
    return line.split()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'