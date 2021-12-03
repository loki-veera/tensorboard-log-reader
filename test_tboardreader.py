import argparse

from src.tboardreader import tensorboardReader


def parse_cmd():
    """
    Method to create argument parser
    Args:
        None
    """
    parser = argparse.ArgumentParser(description='Tensorboard log reader')
    parser.add_argument(
        '--path',
        default=None,
        required=True,
        help='Path of the tensorboard log file'
    )
    parser.add_argument(
        '--tag',
        default='all',
        help='Required tag in log file, Default to read all tags'
    )
    parser.add_argument(
        '--save',
        action='store_true',
        default=True,
        help='For saving the values as a csv file'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        default=True,
        help='Print the steps'
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_cmd()
    reader = tensorboardReader()
    reader.run(args)
