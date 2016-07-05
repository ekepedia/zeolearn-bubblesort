def bubblesort( array ):
    for limit in range( len( array ) - 1, 0, -1):
        swapped = False

        for i in range( 0, limit):
            if array[i] > array[i+1]:
                array = swap( i, i+1, array )
                swapped = True

        if not swapped:
            break

    return array

def swap( i, j, array ):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array
