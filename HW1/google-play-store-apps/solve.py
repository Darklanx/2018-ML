import sys
sys.path.append("../iris/Forest")
from data_processing import Forest

forest = Forest('new_googleplaystore.csv')
data, target, test_data, test_target = forest.create_data()

scores, avg_score = forest.KFold(5, tree_cnt=20)
print(scores)
print(avg_score)
