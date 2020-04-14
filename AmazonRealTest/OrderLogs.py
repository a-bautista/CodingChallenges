

def orderBoxes(numberOfBoxes, boxList):
    new_format_box =  []
    old_format_box =  []
    for box in boxList:
        if box.split(" ")[1].isdigit():
          new_format_box.append(box)
        else:
          other_strings = ' '.join(box.split(" ")[1:]) + " "+box.split(" ")[0]
          old_format_box.append(other_strings)

    old_format_box.sort(key=str.lower)
    for index, box in enumerate(old_format_box):
      length = len(box.split(" "))
      old_format_box[index] = box.split(" ")[length - 1] + " " + ' '.join(box.split(" ")[0:length-1])

    return old_format_box + new_format_box



boxList = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
boxList2 = ["t2 13 121 98","r1 box are bit", "b4 xi me nu", "br8 eat nim did", "w1 has uni gry", "f3 52 54 31"]

result = orderBoxes(6,boxList2)
print(result)

"""
 For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

    We will call these two varieties of logs letter-logs and digit-logs. 
    It is guaranteed that each log has at least one word after its identifier.
    
    Reorder the logs so that all of the letter-logs come before any digit-log.  
    The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
    The digit-logs should be put in their original order.
    Return the final order of the logs.
"""