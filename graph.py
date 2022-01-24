from matplotlib import pyplot as plt
players =['jhon', 'Ronaldo','messi','virat']
score =[51,87,45,67]
plt.bar(players, score,color='green')
plt.title('score card')
plt.xlabel(players)
plt.ylabel('Runs')
plt.show()