# End-to-end NLP project for Spam Detection with model comparison and performance evaluation
## Project Overview
This project focuses on developing a Machine Learning-based spam detection system to classify SMS/email messages as Spam or Ham (Legitimate). Traditional rule-based filtering systems are increasingly ineffective due to evolving spam tactics. Therefore, this project implements and compares multiple machine learning models to build a robust and scalable spam detection solution.
The system was developed and evaluated using real-world labelled SMS data.

## Objectives

- Collect and prepare labelled spam/ham dataset
- Perform text cleaning and preprocessing
- Apply feature engineering using TF-IDF vectorization
- Train and compare multiple ML models
- Evaluate models using advanced performance metrics
- Consider ethical aspects such as bias and privacy

## Dataset

- Total messages: 5,574
- Ham messages: 4,825 (86.5%)
- Spam messages: 749 (13.5%)
- Data format: CSV with labelled categories
  
The dataset was imbalanced, requiring careful evaluation beyond simple accuracy metrics.

## Data Preprocessing

The following preprocessing steps were applied:
- Text normalization (lowercasing)
- Removal of URLs, special characters, email addresses
- Tokenization
- Stopword removal
- Lemmatization
- TF-IDF vectorization for feature extraction
  
TF-IDF was chosen over Bag-of-Words to give more importance to informative spam-related terms such as “lottery”, “winner”, and “offer”.

## Models Implemented

Three machine learning models were developed and compared:
### Multinomial Naïve Bayes
- Fast and efficient
- Suitable for text classification

### Random Forest Classifier
- Ensemble-based model
- Reduces overfitting
- Achieved zero false positives

### Support Vector Machine (SVM)
- Best overall performer
- High precision and recall
- Highest F1-score and AUC

## Model Performance

| Model         | Accuracy  | AUC      |
|---------------|-----------|----------|
| Naïve Bayes   | ~98%      | 0.98     |
| Random Forest | 98.1%     | 0.989    |
| SVM           | **98.4%** | **0.99** |

### Key Findings:
- SVM achieved the highest F1-score (93.9%)
- Random Forest produced 0 false positives
- All models demonstrated strong real-world applicability

## Evaluation Metrics Used
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC Curve
  
The ROC curves showed excellent discriminative ability, with AUC values close to 1.

## Ethical Considerations
- Addressed class imbalance
- Considered privacy implications (GDPR awareness)
- Highlighted need for explainable AI in spam filtering

## Tools & Technologies
- Python
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorization
- Google Colab

## Summary
This project demonstrates that machine learning techniques can effectively detect spam with high accuracy and reliability. Among the tested models, Support Vector Machine (SVM) performed best overall, offering a strong balance between precision and recall.

The results show that automated spam detection systems can significantly reduce false positives while maintaining strong spam identification performance.
