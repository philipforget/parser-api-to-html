#!/usr/bin/python
import os
import requests
import sys



def parser(url, token, readability_root=None):
    readability_root = readability_root or 'http://www.readability.com'

    parser_path = '%s/api/content/v1/parser?' % readability_root

    response = requests.get(parser_path, params={'token': token, 'url':url })

    if response.ok:
        return response.json()
    
    else:
        raise ValueError('Unable to parse url for content')



if __name__ == '__main__':
    import argparse

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('-t', '--token',
        help = 'Supply a Parser API token to use, if not set looks for $RDB_PARSER_TOKEN',
        action = 'store')

    arg_parser.add_argument('-o', '--output-file',
        help = 'Supply a filepath to save output to',
        action = 'store')

    arg_parser.add_argument('-v', '--verbose',
        help = 'Increase output verbosity, good for debugging',
        action = 'store_true')

    arg_parser.add_argument('-r', '--readability-root',
        help = 'Change the root path of the parser domain from http://www.readability.com',
        action = 'store')

    arg_parser.add_argument('url',
        help = 'The url to parse')

    args = arg_parser.parse_args()

    token = args.token
    if token is None:
        try:
            token = os.environ['RDB_PARSER_TOKEN']
        except KeyError:
            sys.stderr.write('No token provided or token not set in $RDB_PARSER_TOKEN\n')
            sys.exit(1)

    try:
        parsed = parser(args.url, token, args.readability_root)
    except Exception as e:
        sys.stderr.write("Unable to parse url for content\n")
        sys.exit(1)

    output_file = args.output_file
    if output_file is not None:
        # Expand filepaths with tildes
        if output_file.find('~') > -1:
            output_file = os.path.expanduser(output_file)
        # Else expand from cwd if not absolute
        elif output_file[0] != '/':
            output_file = os.path.join(os.getcwd(), output_file)

        with open(output_file, 'w') as f:
            f.write(parsed['content'].encode('utf-8'))

    else:
        # Write to stdout
        sys.stdout.write(parsed['content'].encode('utf-8'))
