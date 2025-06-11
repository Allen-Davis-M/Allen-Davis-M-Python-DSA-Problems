def is_even(k: int) -> bool:
    if k == 0:
        return True
    current_k = k
    if current_k < 0:
        current_k = 0 - current_k  
    while current_k >= 2:
        current_k = current_k - 2

    if current_k == 0:
        return True
    else:  
        return False

is_even(7)
