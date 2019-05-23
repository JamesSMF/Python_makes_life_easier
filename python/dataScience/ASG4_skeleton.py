import argparse


def parse_args():
    """
    parse_args takes no input and returns an Namespace dictionary describing the arguments selected
    by the user.  If invalid arguments are selected, the function will print an error message and quit.
    :return: Namespace with arguments to use
    """

    parser = argparse.ArgumentParser("Read CSV input about avocados and print total amount sold")
    parser.add_argument('--input', '-i', dest='input', required=True, type=str,
                       help='input CSV file')

    parser.add_argument('--group_by_region', '-r', dest='group_by_region', action='store_true', default=False,
                       help='Calculate results per region (default: calculate for all regions)')
    parser.add_argument('--organic', '-o', dest='organic', action='store_true', default=False,
                       help='Only calculate for organic avocados (default: calculate for conventional and organic)')

    return parser.parse_args()


def main():
    """
    The main body of the program.  It parses arguments, and performs calculations on a CSV
    """

    # get arguments entered by users
    args = parse_args()

    # TODO remove these print statements
    # This code is provided as an example for how to interpret the results of parse_args()
    print("Input file:      {}".format(args.input))
    print("Group by region: {}".format(args.group_by_region))
    print("Only organic:    {}".format(args.organic))


if __name__ == "__main__":
    main()