# Social Media Sentiment Analysis

This project analyzes and visualizes **sentiment patterns** in social media data (Twitter) to understand public opinion towards specific topics or brands.

#Objective

To perform **exploratory analysis** of tweet sentiments (Positive, Negative, Neutral) and visualize how different topics/brands are perceived.

#Files Included

- `sentiment_analysis.py`: Python script for analysis and visualization
- `twitter_training.csv`: Raw Twitter sentiment dataset
- `README.md`: Project overview and usage guide

#Data Preparation

- Read and labeled the dataset columns: `ID`, `Topic`, `Sentiment`, `Text`
- Cleaned and grouped data by sentiment
- Analyzed sentiment by **topic or brand**

#Visualizations

1. **Bar Chart** – Overall sentiment distribution across tweets
2. **Stacked Bar Chart** – Sentiment per topic/brand

#How to Run

1. Install required libraries:
   ```bash
   pip install pandas matplotlib
