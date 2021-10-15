import argparse
import pathlib

import pandas


def main():
    print('Hello world!')


def toy(args):
    data_file = pathlib.Path(__file__).parent.resolve() / 'toy' / 'czeged-weather.csv'
    dataframe = pandas.read_csv(data_file)

    predictor_columns = (
        'Humidity',
        'Wind Speed (km/h)',
        'Visibility (km)',
        'Loud Cover',  # probably should be 'Cloud Cover'
        'Pressure (millibars)',
    )
    response_column = 'Apparent Temperature (C)'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute the `qreg` Python package.')
    parser.add_argument('subcommand',
                        nargs='?',
                        default=toy,
                        help='compute the quantile regression estimates on a toy example')

    args = parser.parse_args()
    args.subcommand(args)
