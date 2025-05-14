from sklearn.preprocessing import LabelEncoder

def encode_categories(df, cols):
    encoders = {}
    for col in cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
    return df, encoders
