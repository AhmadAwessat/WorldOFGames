#add the score to the txt file
def add_score(difficulty):

    POINTS_OF_WINNING = (difficulty * 3) + 5

    add_scores = open('Scores.txt', 'a')
    add_scores.write('current_score='+str(POINTS_OF_WINNING) + '\n')
    add_scores.close()


