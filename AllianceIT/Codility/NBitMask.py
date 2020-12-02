def generate_args(N, K):  # let's say N=3

    if N==1 and K==0:

        return ["0"]

    elif N==1 and K==1:

        return ["1"]

    elif (K>N):

        return []

    else:

      return (["0"+x for x in generate_args(N-1,K)] +

            ["1"+x for x in generate_args(N-1,K-1)])

def main():

  print(generate_args(4,3))

main()