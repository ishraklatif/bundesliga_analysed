import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"/Users/ishraklatif/PycharmProjects/Uni_assignment/passes.csv", sep=';')
data = data.dropna()
print("Columns Names", data.columns)

winners = data[data['winner'] == 'Yes']
losers = data[data['winner'] == 'No']





# Calculate average passing rates for winning and losing teams
avg_passing_rate_winners = winners['passing_quote'].mean()
avg_passing_rate_losers = losers['passing_quote'].mean()
print("Mean passing rate wins: " , avg_passing_rate_winners)
print("Mean passing rate loss: " , avg_passing_rate_losers)
std_dev_win = winners['passing_quote'].std()
std_dev_losers = losers['passing_quote'].std()


winners_sample_size = len(winners)
losers_sample_size = len(losers)
DOF = winners_sample_size + losers_sample_size - 2
print("Degrees of freedom" , DOF)



# Perform a t-test to determine if the difference in passing rates is statistically significant
t_stat, p_value = stats.ttest_ind(winners['passing_quote'], losers['passing_quote'])
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

std_dev_loss = losers['passing_quote'].std()
mean_loss = losers['passing_quote'].mean()

print("Stdev_loss" , std_dev_loss)
print("Mean_loss" , mean_loss)

threshold_loss = mean_loss - 2 * std_dev_loss
threshold_draw = mean_loss + 2 * std_dev_loss

print("Threshold Loss: ", threshold_loss)
print("Threshold Draw", threshold_draw)

loss_data = losers[losers['passing_quote'] < threshold_loss]
draw_data = losers[losers['passing_quote'] > threshold_loss]

std_dev_draw = draw_data['passing_quote'].std()
print("Stdev draw", std_dev_draw)
print("Stdev win", std_dev_win)


#
# print("Loss Data:", loss_data)
# print("Draw Data", draw_data)
# print('Win Data', winners)





# Visualize passing rate distribution for winners, loss_data, and draw_data
plt.figure(figsize=(12, 8))

# Histogram for winners
plt.subplot(3, 1, 1)
sns.histplot(data=winners, x='passing_quote', bins=20, kde=True, color='green')
plt.title('Passing Rate Distribution for Winners')
plt.xlabel('Passing Rate')
plt.ylabel('Frequency')

# Histogram for loss_data
plt.subplot(3, 1, 2)
sns.histplot(data=loss_data, x='passing_quote', bins=20, kde=True, color='red')
plt.title('Passing Rate Distribution for Losses (Outliers)')
plt.xlabel('Passing Rate')
plt.ylabel('Frequency')

# Histogram for draw_data
plt.subplot(3, 1, 3)
sns.histplot(data=draw_data, x='passing_quote', bins=20, kde=True, color='blue')
plt.title('Passing Rate Distribution for Draws (Non-Outliers)')
plt.xlabel('Passing Rate')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
# Visualize passing rate distribution for winners, loss_data, and draw_data in one histogram
plt.figure(figsize=(10, 6))

# Plot histogram for winners
sns.histplot(data=winners, x='passing_quote', bins=20, kde=True, color='green', label='Winners')

# Plot histogram for loss_data
sns.histplot(data=loss_data, x='passing_quote', bins=20, kde=True, color='red', label='Losses (Outliers)')

# Plot histogram for draw_data
sns.histplot(data=draw_data, x='passing_quote', bins=20, kde=True, color='blue', label='Draws (Non-Outliers)')

# Set title and labels
plt.title('Passing Rate Distribution by Game Outcome')
plt.xlabel('Passing Rate')
plt.ylabel('Frequency')

# Add legend
plt.legend()

plt.grid(True)
plt.show()
#


