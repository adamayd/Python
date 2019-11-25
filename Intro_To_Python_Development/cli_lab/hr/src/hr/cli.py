import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='the path to the export file')
    parser.add_argument('-f', '--format', 
            help='export to either JSON or CSV',
            default='json', 
            choices=['json', 'csv'], 
            type=str.lower)
    return parser

def main():
    import sys
    from hr import export, users

    args = create_parser().parse_args()
    userslist = users.get_users()

    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout

    if args.format == 'json':
        export.to_json(file, userslist)
    else:
        export.to_csv(file, userslist)
