import pdb
start = None
end = None
_dict = {}
def pick_peaks(arr):
    _dict.update({"pos": solve(arr, start, end)[1], "peaks": solve(arr, start, end)[0]})
    return _dict

def solve(arr, start, end):
    pdb.set_trace()
    res = []
    pos = []
    for x in range(len(arr) - 1):
        if end == arr[x]:
            continue
        if start == None:
            start = arr[x]
            continue
        elif start != None:
            if arr[x] > start and arr[x] > arr[x + 1]:
                res.append(arr[x])
                pos.append(x)
                try:
                    start = arr[x + 2]
                except:
                    pass
                end = arr[x + 1]
            elif arr[x] == arr[x+1]:
                 starter = arr[x]
                 for y in range(len(arr[x:])):
                    print(arr[y])
                    if arr[y] > starter:
                        if arr[y] != arr[-1]:
                            res.append(arr[y])
                            pos.append(arr.index(arr[y]))
                            break
                        else:
                            res.append(arr[y+1])
                            pos.append(y+1)
                            break
            else:            
                continue
    return res,pos
pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])
