import collections
import heapq
import re

class Solution(object):
    def topKFrequentMentionedKeywords(self, keywords, reviews, k):
        """
        :type keywords: List[str]
        :type reviews: List[str]
        :type k: int
        :rtype: List[str]
        """

        data_value_dict = collections.Counter()
        key_value_dict = set(keywords)
        #res = []

        for review in reviews:
            # the sentence is converted to lower case and split by spaces
            temp_list = review.lower().split(' ')

            for value in temp_list:
                # only consider the word, do not take into account weird characters
                value = re.sub('[^a-z]', '', value)

                # verify if each word exists in the set and if True then count the word and its frequency
                if value in key_value_dict:
                    # verify if h
                    data_value_dict[value] += 1

        # instead of displaying the Counter({'anacell':3,'betacellular':3,...}) I display the empty Counter with the
        # values that appeared more frequently.
        res = heapq.nsmallest(k, data_value_dict, key=lambda x: (-data_value_dict[x], x))

        return res

def main():
    k = 2
    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
        "I love anacell Best services; Best services provided by anacell",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than anacell",
        "Betacellular is better than deltacellular."]
    solution = Solution()
    res = solution.topKFrequentMentionedKeywords(keywords, reviews, k)
    print(res)

if __name__ == "__main__":
    main()

'''
   Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to 
   least frequently mentioned. The comparison of strings is case-insensitive. If keywords are mentioned an equal number 
   of times in reviews, sort alphabetically.
'''