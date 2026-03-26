import pandas as pd
import statsmodels.api as sm


def run_regression(df: pd.DataFrame, y_col: str, x_col: str):
    X = sm.add_constant(df[x_col])
    y = df[y_col]

    model = sm.OLS(y, X).fit()
    return model