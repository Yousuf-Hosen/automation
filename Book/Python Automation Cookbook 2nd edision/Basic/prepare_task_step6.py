import argparse
import sys
import configparser
def main(number, other_number, output):
    result = number * other_number
    print(f'The result is {result}', file=output)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='A number', default=1)
    parser.add_argument('-n2', type=int, help='Another number', default=1)
    parser.add_argument('--config', '-c', type=argparse.FileType('r'),
                        help='config file')
    parser.add_argument('-o', dest='output', type=argparse.FileType('a'),
                        help='output file',
                        default=sys.stdout)
    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        # Transforming values into integers
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])
    main(args.n1, args.n2, args.output)