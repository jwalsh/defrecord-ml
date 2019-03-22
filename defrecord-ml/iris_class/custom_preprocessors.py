class Filter():
    def __init__(self, df):
        raise NotImplementedError

class Extractor():
    def __init__(self, df):
        raise NotImplementedError

class Transformer():
    def __init__(self, df):
        raise NotImplementedError

    def fit(self, df):
        raise NotImplementedError

    def transform(self, df):
        raise NotImplementedError

class Scaler():
    def __init__(self, df):
        raise NotImplementedError

class ColumnExtractor(Extractor):
    def __init__(self, df):
        raise NotImplementedError

class DummyTransformer(Transformer):
    def __init__(self, df):
        return NotImplementedError

class ZeroFillTransformer(Transformer):
    def transform(self, df):
        return df

class Log1pTransformer(Transformer):
    def transform(self, df):
        return df
