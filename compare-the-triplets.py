"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
"""


def compareTriplets(a, b):
    # Write your code here
    score_a,score_b = 0,0
    for i in range(len(a)):
        if a[i] > b[i]:
            score_a +=1
        elif b[i] > a[i]:
            score_b +=1
        
    return (score_a,score_b)




if __name__ == '__main__':
    

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)