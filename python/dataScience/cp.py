import argparse
import sys
import re

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

    #  print("Input file:      {}".format(args.input))
    #  print("Group by region: {}".format(args.group_by_region))
    #  print("Only organic:    {}".format(args.organic))

    #######################################################

    Sum = 0
    mult = 0           # this is a variable for the multiplication result on each row
    organic = list()   # sum of organic shits
    checkValid = False
    regionFlg = False
    orgFlg = False
    region = dict()
    for i in range(len(sys.argv)):    # iterate through argv list
        if sys.argv[i]=="-i" or sys.argv[i]=="--input":     # if has -i flag
            checkValid = True                               # it is valid
        if re.search(".csv",sys.argv[i]) and checkValid==True:    # look for the input file
            with open(sys.argv[i], "r") as inFile:                # open the file
                cnt = 0                          # count of lines
                for line in inFile:              # read one line at a time
                    if cnt > 0:
                        lineList = line.split(",")     # split the content by ','
                        mult = float(lineList[2]) * float(lineList[3])    # calculate the result on that line

                        ############## Group by city ##############

                        lineList[-1] = re.sub('\n', ': ', lineList[-1])   # strip newline char
                        if lineList[-1] not in region:              # if this city did not appear before
                            region[lineList[-1]] = mult             # add it to the dict
                        else:
                            region[lineList[-1]] += mult            # update the sale of that city

                        ###########################################

                        ############## Organic Check ##############

                        if lineList[-3]=="organic":
                            if organic[lineList[-1]] not in organic:
                                organic[lineList[-1]] = mult
                            else:
                                organic[lineList[-1]] += mult

                        ###########################################

                    cnt += 1          # increment the line count
                    Sum += mult       # update the sum

            inFile.close()
            checkValid = False            # set this shit back to False to avoid confusion

        if sys.argv[i]=="--group_by_region":
            regionFlg = True

        if sys.argv[i]=='--organic':
            orgFlg = True



    if regionFlg==True and orgFlg==True:
        for k,v in organic.items():
            print(str(k) + str(v))
    elif regionFlg==True:
        for k,v in region.items():
            print(str(k)+str(v))
    elif orgFlg==True:
        print("Total Sales: " + str(sum(organic.values())))
        exit

    print("Total Sales: " + str(Sum))


if __name__ == "__main__":
    main()
