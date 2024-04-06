# bundesliga_analysed
Use of statistical method: T test and Mann Whitney U test
Methods:

Split the data into wins and loss using yes or no column, use stdev and mean of the passing_quote on the loss data and find the threshold for loss using mean_loss - 2 * stdev_loss. Use the threshold to split loss data into loss and draw. Perform SST, SSW and SSB on the data set.

Null hypothesis H1 - The winner of a match does not have a higher passing rate than the loser

Alternative hypothesis H0 - The winner of a match have a higher passing rate than the loser
 

The mean of the two data win and loss: 81.07894736842105
The variance of the two data win and loss: 78.84210526315789
N1 = 114
N2 = 190
Degrees of freedom: 302
Consider the significance level to be 0.05
T test: 2.741802595638678
P value: 0.006474765088259819

Therefore we cannot consider the hypothesis H0 that the winner of a match have a higher passing rate than the loser

Considering the alternate hypothesis it comes to the conclusion that passing rate affects the result of the match

Null hypothesis - The difference in the passing rate in games with a winner is not higher than the difference in games that ended in a draw

Alternative hypothesis - The difference in the passing rate in games with a winner is higher than the difference in games that ended in a draw

The loss data contains both loss and draw outcomes as it is represented by No in the winner column. Therefore, according to the previous hypothesis, that the passing rate affects the result of the match, the loss data is split into loss and draw using stdev and mean to find a threshold of differentiating loss and draw.

Stdev_loss: 6.074172557969795
Mean_loss: 78.84210526315789

Threshold Loss:  66.6937601472183
Threshold Draw 90.99045037909748

Therefore using the threshold values of passing rate, the loss data is split into loss and draw.

Stdev_win: 8.06406289574839
Stdev_draw: 5.463639020959507

As variance in win data is more than the draw data therefore we cannot consider the hypothesis H0 that the difference in the passing rate in games with a winner is not higher than the difference in games that ended in a draw.

Considering the alternate hypothesis we can conclude that the difference in the passing rate in games with a winner is higher than the difference in games that ended in a draw

