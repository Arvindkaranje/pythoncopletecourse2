# 91
# difference between python 2.x and 3.x
# print function is changed little if u compare 2.x and 3.x
# 92
# exercise solution
# 93
# command line utility
# we can perform this operation in windows power shel which is different than gui like
# pycharm and some other, IDLE
# we can perform any operations with command line utility using power shel and cmd

import argparse
import sys

def calc(args):
    if args.o=="add":
        return args.x+args.y
    elif args.o=="mul":
        return args.x*args.y
    elif args.o=="sub":
        return args.x-args.y
    elif args.o=="div":
        return args.x/args.y
    else:
        print("something went wrong")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--x', type=float,default=1.0,
                        help="enter first number ,this is the utility for calculations")

    parser.add_argument('--y', type=float,default=3.0,
                        help="enter second number ,this is the utility once again")
    parser.add_argument('--o',type=str, default="add",
                       help="this is the utility for calculation" )

    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))


# fualty calculater
# use faulty calculator file in power shell with command line
