import argparse


def main():
    print('Hello world!')


def toy(args):
    print('A toy example!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute the `qreg` Python package.')
    parser.add_argument('subcommand',
                        nargs='?',
                        default=toy,
                        help='compute the quantile regression estimates on a toy example')

    args = parser.parse_args()
    args.subcommand(args)
