def fact_re(num):
    return 1 if num==0 or num==1 else num*fact_re(num-1)

def main():
    
    print(fact_re(5))

main()