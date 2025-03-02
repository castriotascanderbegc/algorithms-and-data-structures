"""
Given a list of scores of different students, 
return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  
The average score is calculated using integer division.
"""
from collections import defaultdict
def top5_scores(scores):
    # create a map for each student's id
    scores_map = defaultdict(list)
    for id, score in scores:
        scores_map[id].append(score)
    avg_scores = []
    scores_sorted = sorted(scores_map.items(), key=lambda kv: kv[0])
    
    for id, score in scores_sorted:
        top_5 = sorted(score, reverse=True)
        avg_scores.append((id, int(sum(top_5[:5])/5)))
    
    return avg_scores

scores = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

print(top5_scores(scores))