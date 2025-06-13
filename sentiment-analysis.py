# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset (make sure 'twitter_training.csv' is in the same folder)
df = pd.read_csv("twitter_training.csv", header=None)

# Naming the columns for easier understanding
df.columns = ['ID', 'Topic', 'Sentiment', 'Text']

# Showing the first few rows of data
print("Sample data:")
print(df.head())

# ------------------------------
# Sentiment Distribution Overall
# ------------------------------
sentiment_counts = df['Sentiment'].value_counts()

# Plotting sentiment distribution
plt.figure(figsize=(6, 4))
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'red', 'gray'])
plt.title("Overall Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.grid(True)
plt.show()

# ------------------------------
# Sentiment by Topic/Brand
# ------------------------------
# Counting how many positive/negative/neutral tweets each topic has
topic_sentiment = df.groupby(['Topic', 'Sentiment']).size().unstack().fillna(0)

# Plotting the grouped sentiment
topic_sentiment.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title("Sentiment Distribution by Topic or Brand")
plt.xlabel("Topic or Brand")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=45)
plt.legend(title="Sentiment")
plt.tight_layout()
plt.grid(axis='y')
plt.show()
