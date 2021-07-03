# def fill(coll, value, begin=0, end='1'):
#     if end == '1':
#         end = len(coll)
#     elif end > len(coll):
#         end = len(coll)
#     for i in range(begin, end):
#         coll[i] = value


def fill(coll, value, begin=0, end=None):
    chunk = [value for _ in coll[begin:end]]
    coll[begin:end] = chunk
