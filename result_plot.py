import matplotlib.pyplot as plt

actual = ['yoga', 'water plants', 'check email']
predicted = ['yoga', 'water plants', 'check messages']

correct = sum(1 for a, b in zip(actual, predicted) if a == b)

plt.bar(['Actual', 'Predicted'], [len(actual), len(predicted)], color=['blue', 'orange'])
plt.title(f'Actual vs Predicted Task Count\nAccuracy: {correct/len(actual)*100:.2f}%')
plt.ylabel('No. of Tasks')
plt.show()
