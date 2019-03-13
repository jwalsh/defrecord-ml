# defrecord-ml

This illustrates the machine learning pipeline process used when
supporting multiple generators looking for predictions.

## Setup

The following should work even with a default Python 2 setup:

``` shell
pip install --upgrade virtualenv
virtualenv -p python3.6 --no-site-packages --distribute .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Testing

``` shell
.venv/bin/python3.6 -m defrecord-ml
```

# Projects

For the scaffolding associated with some of the projects it's likely
easiest to just use the files stored in

https://github.com/jwalsh/aws-ml-bootcamp

and upload using the `./s3-upload.sh` script.

```shell
aws machinelearning describe-ml-models | jq '.Results[] | .Name, .Status'
```

For each of the following confirm that the prediction end-point is
available for each of the following:

- "ML model: Iris_class.csv"
- "ML model: Building_heating-load.csv"
- "ML model: Wine_quality.csv"
- "ML model: Car_price.csv"
- "ML model: Banking-customer_target.csv"

## banking-customers/banking-customer_target.csv

http://archive.ics.uci.edu/ml/datasets/Bank+Marketing

"The data is related with direct marketing campaigns (phone calls) of a
Portuguese banking institution. The classification goal is to predict
if the client will subscribe a term deposit (variable y)."

s3://aws-ml-bootcamp-jwalsh/banking-customers/banking-customer_target.csv

## buildings/building_heating-load.csv

https://docs.microsoft.com/en-us/learn/modules/create-an-experiment-in-ml-studio/2-create-an-experiment-in-ml-studio

"[A] dataset that relates to building energy considerations."

s3://aws-ml-bootcamp-jwalsh/buildings/building_heating-load.csv

## cars/car_price.csv

http://archive.ics.uci.edu/ml/datasets/Automobile?ref=datanews.io

s3://aws-ml-bootcamp-jwalsh/cars/car_price.csv

## irises/iris_class.csv

https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

"The iris data published by Fisher (1936)..."

s3://aws-ml-bootcamp-jwalsh/irises/iris_class.csv

## titanic-passengers/titanic-passenger_survived.csv

https://www.kaggle.com/c/titanic

"...what sorts of people were likely to survive."

s3://aws-ml-bootcamp-jwalsh/titanic-passengers/titanic-passenger_survived.csv

## wines/wine_quality.csv

https://www.sciencedirect.com/science/article/pii/S0167923609001377

"Modeling wine preferences by data mining from physicochemical properties."

s3://aws-ml-bootcamp-jwalsh/wines/wine_quality.csv
