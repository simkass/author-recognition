PONCTUATION_SIGNS = ["!", '"', "'", ")", "(", ",", ".", ";", ":", "?", "-", "_", "«", "»", "..."]


def format_line(line, remove_ponctuation=True):
    line = line.rstrip().lower() 
    if remove_ponctuation:
        for p in PONCTUATION_SIGNS:
            line = line.replace(p, " ")
    return line.split()