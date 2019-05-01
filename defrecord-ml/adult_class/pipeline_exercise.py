from sklearn.pipeline import Pipeline
from sklearn.transform import ColumnTransformer

preprocess = make_column_transformer(
    (StandardScaler(), ~categorical),
    (OneHotEncoder(), categorical))

pipe = make_pipeline(preprocess, )

# grid
