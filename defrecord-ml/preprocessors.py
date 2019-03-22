import pandas as pd
from scipy import stats

# These are preprocessors and filters that apply only to cards with
# initial loading of the pivot against summary transactions

# Preprocessors:
class Preprocessor():
    def __init__(self, df):
        raise NotImplementedError

class RandomPreprocessor(Preprocessor):
    def __init__(self, df):
        raise NotImplementedError

class CreditZeroPreprocessor(Preprocessor):
    def __init__(self, df):
        return df[df.iloc[:,-1] < df.iloc[:,-1].mean()]

class FillnaPreprocessor(Preprocessor):
    def __init__(self, df):
        return df.fillna(0, inplace = True)

class Log10ZscorePreprocessor(Preprocessor):
    class __init__(self, df):
        return df_spend.apply(np.log10).apply(stats.zscore)

# Filters
class Filter():
    def __init__(self, df):
        raise NotImplementedError

class SampleFilter(Filter):
    def __init__(self, df):
        return df.sample()

class AllZeroFilter(Filter):
    def __init__(self, df):
        df_filtered = pd.DataFrame(df.apply(lambda x: len([i for i in x if i != 0]), axis = 1))
        df_filtered_months = df_filtered[df_filtered[0] != 0]
        df = df.loc[df_filtered_months.index]
        return df

class OutlierFilter(Filter):
    def __init__(self, df):
        std = df.std(axis=1)
        mean = df.mean(axis=1)
        df['mean'] = mean
        df['std'] = std
        zscore = pd.DataFrame(mean).apply(stats.zscore)
        df['zscore'] = zscore
        df = df[df['zscore'] < 3]
        del df['mean']
        del df['std']
        del df['zscore']
        return df

class GTMeanFilter(Filter):
    def __init__(self, df):
        std = df.std(axis=1)
        mean = df.mean(axis=1)
        df['mean'] = mean
        df['std'] = std
        zscore = pd.DataFrame(mean).apply(stats.zscore)
        df['zscore'] = zscore
        df = df[df['zscore'] < 0]
        del df['mean']
        del df['std']
        del df['zscore']
        return df
