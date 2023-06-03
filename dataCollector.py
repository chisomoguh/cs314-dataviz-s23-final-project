'''
    dataCollector.py
    Reads, traverses, cleans, and a returns a csv file for use

'''

import csv, sys, copy

regionList = {"west": ["west2016data.csv", "west2017data.csv", "west2018data.csv", "west2019data.csv", "west2020data.csv"], 
              "midwest": ["midwest2016data.csv", "midwest2017data.csv", "midwest2018data.csv", "midwest2019data.csv", "midwest2020data.csv"], 
              "south": ["south2016data.csv", "south2017data.csv", "south2018data.csv", "south2019data.csv", "south2020data.csv"], 
              "northeast": ["northeast2016data.csv", "northeast2017data.csv", "northeast2018data.csv", "northeast2019data.csv", "northeast2020data.csv"]}

years = ["2016", "2017", "2018", "2019", "2020"]

diagnosis = ["Trauma/stress-related", "Anxiety", "ADHD", "Conduct", "Delirium/dementia", "Bipolar", "Depressive", "Oppositional Defiant", 
             "Pervasive Developmental", "Personality", "Schizophrenia/Other Psychotic", "Alcohol/Substance Abuse", "Other"]

gender = ["Male", "Female"]

races = ["American Indian/Alaska Native", "Asian", "Black/African American",
         "Native Hawaiin/Pacific Islander", "White", "Other Races/Two or More Races"]

ages = ["0-11", "12-14", "15-17", "18-20", "21-24", "25-29", "30-34","35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65+"]\

years = ["2016", "2017", "2018", "2019", "2020"]

diagnosisDict = {"Trauma/stress-related": {"Male": 0, "Female": 0},
                 "Anxiety": {"Male": 0, "Female": 0},
                 "ADHD": {"Male": 0, "Female": 0},
                 "Conduct": {"Male": 0, "Female": 0}, 
                 "Delirium/dementia": {"Male": 0, "Female": 0}, 
                 "Bipolar": {"Male": 0, "Female": 0}, 
                 "Depressive": {"Male": 0, "Female": 0},
                 "Oppositional Defiant": {"Male": 0, "Female": 0}, 
                "Pervasive Developmental": {"Male": 0, "Female": 0},
                "Personality": {"Male": 0, "Female": 0}, 
                "Schizophrenia/Other Psychotic": {"Male": 0, "Female": 0},
                "Alcohol/Substance Abuse": {"Male": 0, "Female": 0}, 
                "Other": {"Male": 0, "Female": 0}}


'''
YEAR: 0     AGE: 1      ETHNIC: 3       RACE: 4     GENDER: 5
MH1: 11     SMI/SED: 16      STATEFIP: 36       REGION: 38

'''
                            # 0         1       2        3       4       5          6       7           8
    # filteredData.write({row[0]},{row[38]},{row[1]},{row[3]},{row[4]},{row[5]},{row[11]},{row[16]},{row[36]}')
                        # yr          reg        age      eth     race    gen     mh1        smised   state
    

########################## RANDOM ##############################


# goal: see the various ways that Hispanic/Latino origin is recorded in the datasets
def testing(reg):
    regionFiles = regionList[reg]

    for regFile in regionFiles:
        mainFile = open(f'./region/{reg}/{regFile}', "r")
        csv_reader = csv.reader(mainFile, delimiter=',')
        counter = 0
        for row in csv_reader:    
            if counter != 0 and row[6] != "Invalid" and ("Yes" in row[3]) and row[4] == "Invalid":
                print(row[3], row[4])
                print("oof...")
            elif counter != 0 and row[6] != "Invalid" and ("Yes" in row[3]) and row[4] == "Other Races/Two or More Races":
                print(row[3], row[4])
                print("god damn...")
            elif counter != 0 and row[6] != "Invalid" and ("Yes" in row[3]) and row[4] == "Black/African American":
                print(row[3], row[4])
                print("now wait a minute...")
            
            counter +=  1
        
        mainFile.close()
        print("finish reading through a file")


########################## RACE CSV ##############################

def developRaceDictionary():
    theDict = {}
    for diag in diagnosis:
        miniDict = {}
        for race in races:
            miniDict[race] = 0
        theDict[diag] = miniDict

    return theDict


def raceCSV(reg):
    regionFiles = regionList[reg]
    filteredData = []
    emptyDict = developRaceDictionary()

    for regFile in regionFiles:
        aCopy = copy.deepcopy(emptyDict)
        mainFile = open(f'./region/{reg}/{regFile}', "r")
        csv_reader = csv.reader(mainFile, delimiter=',')
        counter = 0
        for row in csv_reader:    
            if counter != 0 and row[6] != "Invalid" and row[4] != "Invalid":
                    aCopy[row[6]][row[4]] += 1
            
            counter +=  1
        
        filteredData.append(aCopy)
        mainFile.close()
    
    
    result = open(f'{reg}RaceData.csv', "w")
    index = 0

    result.write("YEAR,MH1,RACE,COUNT\n")
    for dictionary in filteredData: 
        for diag in dictionary:
            for data in dictionary[diag]:
                result.write(f'{years[index]},{diag},{data},{dictionary[diag][data]}\n')

        index += 1
    
    result.close()


########################## AGE CSV ##############################

def developAgeDictionary():
    theDict = {}
    for diag in diagnosis:
        miniDict = {}
        for age in ages:
            miniDict[age] = 0
        theDict[diag] = miniDict
    
    return theDict

def ageCSV(reg):
    regionFiles = regionList[reg]
    filteredData = []
    emptyDict = developAgeDictionary()

    for regFile in regionFiles:
        aCopy = copy.deepcopy(emptyDict)
        mainFile = open(f'./region/{reg}/{regFile}', "r")
        csv_reader = csv.reader(mainFile, delimiter=',')
        counter = 0
        for row in csv_reader:
            if counter != 0 and row[6] != "Invalid" and row[2] != "N/A" and row[2] != "Invalid":
                aCopy[row[6]][row[2]] += 1
            counter +=  1
        
        filteredData.append(aCopy)
        mainFile.close()
    
    
    result = open(f'{reg}AgeData.csv', "w")
    index = 0

    result.write("YEAR,MH1,AGE,COUNT\n")
    for dictionary in filteredData: 
        for diag in dictionary:
            for data in dictionary[diag]:
                result.write(f'{years[index]},{diag},{data},{dictionary[diag][data]}\n')

        index += 1
    
    result.close()

#################### GENDER CSV ###########################

def genderCSV(reg):

    regionFiles = regionList[reg]
    filteredData = []
    
    for regFile in regionFiles:
        aCopy = copy.deepcopy(diagnosisDict)
        mainFile = open(f'./region/{reg}/{regFile}', "r")
        csv_reader = csv.reader(mainFile, delimiter=',')
        counter = 0
        for row in csv_reader:
            if counter != 0 and row[5] != "Invalid" and row[6] != "Invalid" and row[5] != "N/A":
                aCopy[row[6]][row[5]] += 1
            counter +=  1
        
        filteredData.append(aCopy)
        mainFile.close()

    result = open(f'{reg}GenderData.csv', "w")
    index = 0

    result.write("YEAR,MH1,GENDER,COUNT\n")
    for dictionary in filteredData: 
        for diag in dictionary:
            for data in dictionary[diag]:
                result.write(f'{years[index]},{diag},{data},{dictionary[diag][data]}\n')

        index += 1
    
    result.close()

#####################     REGION FILES...?        #####################
def createRegCSV(reg):

    # print(regionList[reg])
    fileList = regionList[reg]

    result = open(f'{reg}.csv', "w")
    first_row = False
    total = 0;

    for file in fileList:
        genderCSV(file)
        f = open(file, "r")
        csv_reader = csv.reader(f, delimiter=',')
        counter = 0
        for row in csv_reader:
            if counter == 0:
                if not first_row:
                    result.write(f'{row[0]},{row[1]},{row[2]}\n')
                    first_row = True
                else:
                    counter += 1
                    continue
            else:
                result.write(f'{row[0]},{row[1]},{row[2]}\n')
            counter += 1
            total += 1
        f.close()
    
    result.close()
    print(total)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "gender":
            genderCSV(sys.argv[2])
        elif sys.argv[1] == "age":
            ageCSV(sys.argv[2])
        elif sys.argv[1] == "race":
            raceCSV(sys.argv[2])
        elif sys.argv[1] == "testing":
            testing(sys.argv[2])
        # if sys.argv[1] == "create":
        #     createRegCSV(sys.argv[2])
    
    # developAgeDictionary()
    # developRaceDictionary()
