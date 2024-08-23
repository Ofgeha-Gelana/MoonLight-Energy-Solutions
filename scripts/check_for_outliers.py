# Define a function to detect outliers using IQR
def detect_outliers(dataframe1, column):
    Q1 = dataframe1[column].quantile(0.25)
    Q3 = dataframe1[column].quantile(0.75)
    IQR = Q3 - Q1
    outliers = dataframe1[(dataframe1[column] < (Q1 - 1.5 * IQR)) | (dataframe1[column] > (Q3 + 1.5 * IQR))]
    return outliers