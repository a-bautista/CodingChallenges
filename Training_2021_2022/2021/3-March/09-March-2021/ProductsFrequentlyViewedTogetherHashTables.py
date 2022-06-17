from collections import Counter
def findSimilarity(products, candidates):
    prod_n = len(products)
    cand_n = len(candidates)
    res = []

    cand_count = Counter(candidates)
    prod_count = Counter(products[:cand_n - 1])

    for i in range(cand_n - 1, prod_n):
        # You increase the size of the window by 1 and check if prod_count is the same as the 
        # cand_n window
        prod_count[products[i]] += 1 
        # if the current window is equal to the existing counter then add the index where this happened
        if prod_count == cand_count:     
            res.append(i - cand_n + 1)

        # decrease the size of the window and if the value is 0 then delete the entry
        prod_count[products[i - cand_n + 1]] -= 1  
        if prod_count[products[i - cand_n + 1]] == 0:
            del prod_count[products[i - cand_n + 1]]   

    return res

def main():
    product = [3, 2, 1, 5, 2, 1, 2, 1, 3, 4]
    candidate = [1, 2, 3]
    print(findSimilarity(product, candidate))

main()