import pandas as pd


def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df


def generate_kpis(df):
    numeric_cols = df.select_dtypes(include='number')

    kpis = {}

    for col in numeric_cols.columns:
        kpis[col] = {
            "mean": numeric_cols[col].mean(),
            "std": numeric_cols[col].std(),
            "max": numeric_cols[col].max(),
            "min": numeric_cols[col].min(),
            "sum": numeric_cols[col].sum()
        }

    return kpis


def correlation_matrix(df):
    numeric_cols = df.select_dtypes(include='number')
    return numeric_cols.corr()