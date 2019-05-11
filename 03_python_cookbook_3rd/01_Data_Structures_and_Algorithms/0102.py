#Case 1 
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

