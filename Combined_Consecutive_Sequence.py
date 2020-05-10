def consec(lst1, lst2):
  lst1.extend(lst2)
  slist = sorted(lst1)
  slen = len(slist)
  diff_t = 0
  for i in range(1, slen):
     diff_t = diff_t + (slist[i] - slist[i-1])
  if diff_t + 1 == slen:
    return True
  return False 
  

ta = [[0,2,1], [3,6,5,4,7]]
fa = [[0,2,3], [3,6,5,4,7]]

print(*ta, '->', consec(*ta))
print(*fa, '->', consec(*ta))
