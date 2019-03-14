import pandas as pd

class Preprocessor():
    def __init__(self, df):
        raise NotImplementedError

class Filter():
    def __init__(self, df):
        raise NotImplementedError

class RandomPreprocessor(Preprocessor):
    def __init__(self, df):
        raise NotImplementedError


class FillnaPreprocessor(Preprocessor):
    def __init__(self, df):
        return df.fillna(0, inplace = True)

class SampleFilter(Filter):
    def __init__(self, df):
        return df.sample()
