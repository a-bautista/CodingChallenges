'''
    Netflix maintains a popularity score for each of its titles. 
    This popularity score is derived from customer feedback, likes, dislikes, etc. This score is updated weekly and added 
    to the end of the list containing previous scores for the same title. This score list helps Netflix identify titles that
    may be increasing or decreasing in popularity over time. Some titles may be steady in popularity, increasing, decreasing,
     and fluctuating. We want to identify and separate a title if it is gaining or losing popularity.

    We’ll be provided with a list of integers representing the popularity scores of a movie collected over a number of weeks. 
    We need to identify only those titles that are either increasing or decreasing in popularity, so we can separate them 
    from the fluctuating ones for better analysis.

'''

def identify_titles(scores):
    increase = decrease = True

    for i in range(len(scores)-1):
        if scores[i] < scores[i+1]:
            decrease = False
        elif scores[i]> scores[i+1]:
            increase = False        
    return increase or decrease
            
def main():
    # Driver code
    movie_ratings = [
        [1,2,2,3],
        [4,5,6,3,4],
        [8,8,7,6,5,4,4,1]
    ]

    for movie_rating in movie_ratings:
        if identify_titles(movie_rating):
            print("Title Identified and Separated")
        else:
            print("Title Score Fluctuating")

main()

