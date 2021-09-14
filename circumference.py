#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program calculate circumference

import constants


def main():
    # This function calculate circumference

    # input
    radius = int(input("enter radius of the circle(mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference = τr = {} mm".format(circumference))
    print("\nDone")


if __name__ == "__main__":
    main()
