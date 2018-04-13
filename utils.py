
def remap(value, start1, stop1, start2, stop2):
    '''
    Re-maps a number from one range to another.
    '''
    return (stop2 - start2) * (value - start1) / (stop1 - start1) + start2


def constrain(n, low, high):
    ''' Constrains a value between a minimum and maximum value.'''

    return min(high, max(low, n))
