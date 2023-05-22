'''
cleaningScript.py
    Reads, traverses, cleans, and a returns a csv file for use to use
'''

"""
Questions to ask when date cleansing:
What are the features?
What are the expected types (int, float, string, boolean)?
Is there obvious missing data?
Is there other types of missing data that's not so obvious?
"""

import csv

# this can be expanded on...
states = {"1":"Alabama", "2":"Alaska"}

def main():
    creatingCSV()
    
def creatingCSV():
    f = open('./raw_files/mhcld-puf-2019-csv.csv')
    csv_reader = csv.reader(f, delimiter=',')
    counter = 0
    for row in csv_reader:
        if counter == 0:
            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}')
        # elif counter == 100:
        #     break
        elif counter != 0 and row[36] == "1":
            print(f'{states[row[36]]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}')
        counter += 1

    f.close()

if __name__ == "__main__":
    main()