def isISBN(value):
    """"""
    result = 0
    num_to_check = list(str(value).replace('-', ''))
    nums = range(1, 11)
    nums = nums[::-1]

    for index, item in zip(num_to_check, nums[::-1]):
        l = int(index) * int(item)
        result += l

    if result % 11 == 0:
        return True
    else:
        return False