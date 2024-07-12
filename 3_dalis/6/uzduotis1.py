from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


train_df = pd.read_csv('C:\\Python_ca\\3_dalis\\6\\train.csv')

numeric_cols = train_df.select_dtypes(include=['float64', 'int64']).columns

categorical_cols = ['Id']
continuous_cols = [col for col in numeric_cols if col not in categorical_cols]

summary_list = []

for col in continuous_cols:
    feature_data = train_df[col]
    count = feature_data.count()
    missing = feature_data.isna().sum()
    percent_missing = (missing / len(train_df)) * 100
    cardinality = feature_data.nunique()
    minimum = feature_data.min()
    q1 = feature_data.quantile(0.25)
    mean = feature_data.mean()
    median = feature_data.median()
    q3 = feature_data.quantile(0.75)
    maximum = feature_data.max()
    std_dev = feature_data.std()
    
    summary_list.append([
        col, count, percent_missing, cardinality, minimum, q1, mean, median, q3, maximum, std_dev
    ])

summary_df = pd.DataFrame(summary_list, columns=['feature', 'count', '%miss', 'card.', 'min', 'q1', 'mean', 'median', 'q3', 'max', 'std. dev'])

print(summary_df)

summary_df.to_csv('continuous_features_summary.csv', index=False)






categorical_cols = train_df.select_dtypes(include=['object', 'category']).columns

summary_list = []

for col in categorical_cols:
    feature_data = train_df[col]
    count = feature_data.count()
    missing = feature_data.isna().sum()
    percent_missing = (missing / len(train_df)) * 100
    cardinality = feature_data.nunique()
    mode = feature_data.mode()[0]
    mode_freq = feature_data.value_counts().max()
    mode_perc = (mode_freq / len(train_df)) * 100

    value_counts = feature_data.value_counts()
    if len(value_counts) > 1:
        second_mode = value_counts.index[1]
        second_mode_freq = value_counts.iloc[1]
        second_mode_perc = (second_mode_freq / len(train_df)) * 100
    else:
        second_mode = None
        second_mode_freq = 0
        second_mode_perc = 0.0
    
    summary_list.append([
        col, count, percent_missing, cardinality, mode, mode_freq, mode_perc,
        second_mode, second_mode_freq, second_mode_perc
    ])

summary_df = pd.DataFrame(summary_list, columns=[
    'feature', 'count', 'miss%', 'card.', 'mode', 'mode freq', 'mode%',
    '2nd mode', '2nd mode freq', '2nd mode%'
])

print(summary_df)

summary_df.to_csv('categorical_features_summary.csv', index=False)