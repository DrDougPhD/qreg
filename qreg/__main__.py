import argparse
import pathlib

import pandas

from qreg.probability import cdf
from qreg.probability import quantile


def main():
    print('Hello world!')


def toy(args=None):
    data_file = pathlib.Path(__file__).parent.resolve() / 'toy' / 'czeged-weather.csv'
    dataframe = pandas.read_csv(data_file)

    predictor_columns = [
        'Humidity',
        'Wind Speed (km/h)',
        'Visibility (km)',
        'Loud Cover',  # probably should be 'Cloud Cover'
        'Pressure (millibars)',
    ]
    response_column = ['Apparent Temperature (C)']

    predictors = dataframe[predictor_columns]
    response = dataframe[response_column]  #.sort_values(by=response_column)

    quantiles = quantile.of(response)
    print(quantiles(.75))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute the `qreg` Python package.')
    parser.add_argument('subcommand',
                        nargs='?',
                        default=toy,
                        help='compute the quantile regression estimates on a toy example')

    args = parser.parse_args()
    args.subcommand(args)
