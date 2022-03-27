def accum(s):
    res = []
    for i in s.upper():
      res.append(i)

    count = 0
    ans = []
    for j in res:
        ans.append(j+j.lower()*count)
        count += 1
    return '-'.join(ans)