'''
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number 
    could represent. Return the answer in any order.

    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does 
    not map to any letters.

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Input: digits = "2"
    Output: ["a","b","c"]

    Input: digits = ""
    Output: []

    "2"
     ^
    Output: ["a","b","c"]

    res = []



    for d in phone[digits[:1]]:
        res.append(d)
        
        # backtrack


'''

def solve(digits):
    phone = {
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]
    }
    res = []
    
    def dfs(currentDigit, combination):
        if len(combination)==0:
            res.append(list(combination))
        else:
            for letter in phone[digits[:1]]:
                combination+=letter
                dfs()

    dfs(digits, "")



def main():
    digits = "23"

