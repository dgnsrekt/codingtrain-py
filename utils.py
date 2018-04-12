
def remap(value, start1, stop1, start2, stop2):
    '''
    Re-maps a number from one range to another.
    '''
    return (stop2 - start2) * (value - start1) / (stop1 - start1) + start2
