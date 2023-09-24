### Summary
The goal of this project is to identify key features that hold influence over the enjoyability of coffee.

### Data Explanation
The data used for this project is public domain and is hosted on Kaggle. Features pertaining to name, origin, price, rating. After attempting to isolate the correct origin name with code, it was decided that these changes would be made by hand within the CSV file. Dummy variables were created or all object data and the two origin columns were combined as to not dilute the presence of a specific origin that appeared in both features. Outliers with fewer than ten occurrences were removed.

### Analysis
Linear regression was used for this project. Initial analysis of the model’s accuracy concluded that this would be a poor prediction model due to it possessing a 15-30% accuracy depending of train/test split. The model was created and tested 1000 times in order to record features with the highest and lowest correlation coefficients. Of the eighty-six features, two were within the top five highest correlation coefficients 95% of the time and one was in the top five lowest correlation coefficients 93% of the time. 

### Conclusion
Coffee that originates from Valle De Cauca or Caicedonia has an increased likelihood of receiving a better rating. Coffee originating from Aceh appeared in the highest correlation coefficient in 73% of the epochs. Coffee originating from Kona as a decreased likelihood of receiving a better rating. Coffee from Columbia and Indonesia appeared in the lowest correlation coefficient in 77% of epochs.

### Ethical Assessment
All business decisions based on insights derived from data science have the potential to take possible business from a group or company. In this case, it could hurt the coffee production of Kona or any other origin that is not Valle De Cauca or Caicedonia. This exact ramifications of this are unknown but hurting the Kona coffee industry, for instance, could lead to turmoil for the workers of that industry.
