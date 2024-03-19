import configparser
import os

#print('hello world')

# Read the config file
gizmoCommand = [[]]


def parseCommandString(iStr):
    partsToSplit = iStr.strip().split()
    userAction = int(partsToSplit[0])
    userLookingAtGizmo = int(partsToSplit[1])
    gizmoAction = partsToSplit[2]
    return userAction, userLookingAtGizmo, gizmoAction

def read_file_instructions():
    # open and read the file
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configFile.ini')
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Retrieve keys from a specific section (e.g., Section1)
    section_name = "DEFAULT"
    keys = list(config[section_name].keys())

    #print("Keys in the", section_name, "section:")
    #print(keys)
    #print('Fruits List: ', fruits)
    for key in keys:
        value= config[section_name][key]
        #print("type of value: ", type(value))
        #print(f"Values: {value}")
        userAction, userLookingAtGizmo, gizmoAction = parseCommandString(value)
        print(f"{userAction} {userLookingAtGizmo} : {gizmoAction}")
        gizmoCommand[userAction][userLookingAtGizmo] = gizmoAction
        print(f"gizmo action: ", gizmoAction)
    # create local arrays to store values
    '''actionPerformedByPatient = []
    patientLookingAtGizmo = []
    gizmoMovements = []
    # iterate loop till the length of items in the section
    for key, value in config['DEFAULT'].items():
        values = values.split()
        for i, val in enumerate(values):
            actionPerformedByPatient[i].append(val)
            patientLookingAtGizmo[i].append(val)
            gizmoMovements[i].append(val)
    # append local arrays into a global array
    newArray.append(actionPerformedByPatient, patientLookingAtGizmo, gizmoMovements)
    print("new values: ", newArray)'''
if __name__ == '__main__':
    read_file_instructions()
