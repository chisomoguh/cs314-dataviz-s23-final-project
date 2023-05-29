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

import csv, sys

def main():
    print("this is the main function")

# this can be expanded on...
states = {"1":"Alabama", "2":"Alaska", "4": "Arizona", "5": "Arkansas",
          "6": "California", "8": "Colorado", "9": "Connecticut",
          "10": "Delaware", "11": "District of Columbia", "12": "Florida", "13": "Georgia",
          "15": "Hawaii", "16": "Idaho", "17": "Illinois", "18": "Indiana",
          "19": "Iowa", "20": "Kansas", "21": "Kentucky", "22": "Louisiana", "23": "Maine",        
          "24": "Maryland", "25": "Massachusetts", "26": "Michigan", "27": "Minnesota",
          "28": "Mississippi", "29": "Missouri", "30": "Montana", "31": "Nebraska",
          "32": "Nevada", "34": "New Jersey", "35": "New Mexico", "36": "New York",
          "37": "North Carolina", "38": "North Dakota", "39": "Ohio", "40": "Oklahoma",
          "41": "Oregon", "42": "Pennsylvania", "44": "Rhode Island",
          "45": "South Carolina", "46": "South Dakota", "47": "Tennessee", "48": "Texas",
          "49": "Utah", "50": "Vermont", "51": "Virginia", "53": "Washington",
          "54": "West Virginia", "55": "Wisconsin", "56": "Wyoming", "72": "Puerto Rico", "99": "Other"}

region = {"0": "Other", "1": "Northeast", "2": "Midwest", "3": "South", "4": "West"}

sex = {"1": "Male", "2": "Female", "-9": "N/A"}

age = {"1": "0-11", "2": "12-14", "3": "15-17", "4": "18-20", "5": "21-24", "6": "25-29",
       "7":"30-34", "8": "35-39", "9": "40-44", "10": "45-49", "11": "50-54", "12": "55-59",
       "13": "60-64", "14": "65+", "-9": "Invalid"}

hisp = {"1": "Yes-Mexican", "2": "Yes-Puerto Rican", "3": "Yes-Other", "4": "No",
        "-9": "Invalid"}

race = {"1": "American Indian/Alaska Native", "2": "Asian", "3": "Black/African American",
        "4": "Native Hawaiin/Pacific Islander", "5": "White", "6": "Other Races/Two or More Races",
        "-9": "Invalid"}

smi = {"1": "SMI", "2": "SED", "3": "No", "-9": "Invalid"}

diagnosis = {"1": "Trauma/stress-related", "2": "Anxiety", "3": "ADHD", "4": "Conduct",
       "5": "Delirium/dementia", "6": "Bipolar", "7": "Depressive", "8": "Oppositional Defiant",
       "9": "Pervasive Developmental", "10": "Personality", "11": "Schizophrenia/Other Psychotic",
       "12": "Alcohol/Substance Abuse", "13": "Other", "-9": "Invalid"}

'''
YEAR: 0     AGE: 1      ETHNIC: 3       RACE: 4     GENDER: 5
MH1: 11     SMI/SED: 16      STATEFIP: 36       REGION: 38
'''
    
def creatingCSV(year):
    f = open(f'./raw_files/mhcld-puf-{year}-csv.csv', "r")
    filteredData = open(f'{year}data.csv', "w")

    csv_reader = csv.reader(f, delimiter=',')
    counter = 0

    for row in csv_reader:
        if counter == 0:
            filteredData.write(f'{row[0]},{row[38]},{row[1]},{row[3]},{row[4]},{row[5]},{row[11]},{row[16]},{row[36]}\n')
        else:
            filteredData.write(f'{row[0]},{region[row[38]]},{age[row[1]]},{hisp[row[3]]},{race[row[4]]},{sex[row[5]]},{diagnosis[row[11]]},{smi[row[16]]},{states[row[36]]}\n')
        counter += 1

    f.close()
    filteredData.close()

def divideByRegion(year):
    f = open(f'./{year}data.csv', "r")
    southFile = open(f'south{year}data.csv', "w")
    neFile = open(f'northeast{year}data.csv', "w")
    mdFile = open(f'midwest{year}data.csv', "w")
    westFile = open(f'west{year}data.csv', "w")
    otherFile = open(f'other{year}data.csv', "w")

    csv_reader = csv.reader(f, delimiter=',')
    counter = 0
    for row in csv_reader:
        if counter == 0:
            southFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
            mdFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
            neFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
            westFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
            otherFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
        
        if row[1] == "South":
            southFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
        elif row[1] == "Midwest":
            mdFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
        elif row[1] == "Northeast":
            neFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
        elif row[1] == "West":
            westFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
        elif row[1] == "Other":
            otherFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
        counter += 1

    f.close()
    southFile.close()
    neFile.close()
    mdFile.close()
    westFile.close()
    otherFile.close()

def divideBySex(fileName):
    file = open(fileName, "r")
    mFile = open(f'male-{fileName}', "w")
    fmFile = open(f'female-{fileName}', "w")
    oFile = open(f'other-{fileName}', "w")

    csv_reader = csv.reader(file, delimiter=',')
    counter = 0
    for row in csv_reader:
        if counter == 0:
            mFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
            fmFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
            oFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')

        if row[5] == "Male":
            mFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
        elif row[5] == "Female":
            fmFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')
        elif row[5] == "N/A":
            oFile.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}\n')

        counter += 1

    file.close()
    mFile.close()
    fmFile.close()
    oFile.close()
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "region":
            divideByRegion(int(sys.argv[2]))
        elif sys.argv[1] == "gender":
            divideBySex(sys.argv[2])
        elif sys.argv[1] == "create":
            creatingCSV(int(sys.argv[2]))