# http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap09.htm

def sort_scores(scores, HPS):
    if len(scores) < 2:
        return scores
    else:
    

unsorted_scores = [37, 89]
# unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

#89, 37
# Returns [91, 89, 65, 53, 41, 37]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
