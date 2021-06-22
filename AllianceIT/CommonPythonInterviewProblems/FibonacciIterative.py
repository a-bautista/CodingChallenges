def solve(n):
    res = []
    if n == 0:
      res.append("' '")
    elif n == 1:
      res.append(0)
    elif n > 1:
      fn  = 0
      fn1 = 1
      fn2 = 2
      res.append(fn)
      res.append(fn1)
      res.append(fn2)
      for i in range(3,n):
        fn  = fn1+fn2
        fn1 = fn2
        fn2 = fn
        res.append(fn)
    return ' '.join(map(str, res))

def main():
  res = solve(0)
  print(res)

main()