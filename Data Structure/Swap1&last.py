def swap(lst):
  l = len(lst) - 1
  a = lst[0]
  b = lst[l]
  ar = a
  br = b
  c = ar
  ar = br
  br = c
  lst.remove(a)
  lst.remove(b)
  lst.insert(0,ar)
  lst.insert(l,br)
  return lst

size = int(input("Enter size of list "))
listy = []
for s in range(size):
  num = input("Enter the input one by one :")
  listy.append(num)
print(swap(listy))
