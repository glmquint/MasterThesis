from itertools import product
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Splatter')
    parser.add_argument('--fs', type=str, help='Field Separator', default=',')
    parser.add_argument('--rs', type=str, help='Record Separator', default='<br>')
    args = parser.parse_args()
    while True:
        try:
            in_str = input()
        except EOFError:
            break
        if args.rs not in in_str:
            print(in_str)
        else:
            versions_per_field = [field.split(args.rs) for field in in_str.split(args.fs)]
            arr = [args.fs.join(x) for x in product(*versions_per_field)]
            for res in arr:
                print(res)
