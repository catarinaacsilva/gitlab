'''
---------------------------------------------------------------------------------------------------
-- Gitlab Simulation
-- Authors: Catarina Silva, 76399; Duarte Dias, 80214
-- Emails: c.alexandracorreia@ua.pt; duarterochadias@ua.pt 

-- Version 2.0
---------------------------------------------------------------------------------------------------
'''

# coding=utf-8

import argparse
import threading
import random
import time
import json
from gitlab_user import GitlabUser


# Global Variable
jsonFile = {}               # JSON File
pathFile = 'file.txt'       # Path to File


# Execute Operation
def execute(usr, n):
    print(usr[0].get_name())
    if(n == 1):             # Create Project
        print("Create Project")
        numProj = len(usr.get_all_projects())
        usr.create_prj("proj"+str(numProj))
    elif(n == 2):           # Create File
        print("Create File")
        prj = usr.get_rand_project()
        nFiles = usr.get_nFC_project(prj)
        usr.commit(prj, 'create', 'file' + str(nFiles) + '.txt', pathFile)
    elif(n == 3):           # Update File
        print("Update File")
        prj = usr.get_rand_project()
        fName = usr.get_fileN_project(prj)
        if fName != 'FNF':
            usr.commit(prj, 'update', fName, pathFile)
        else:
            print('File Not Found!')
    elif(n == 4):           # Delete File 
        print("Delete File")
        prj = usr.get_rand_project()
        fName = usr.get_fileN_project(prj)
        if fName != 'FNF':
            usr.commit(prj, 'delete', fName)
        else:
            print('File Not Found!')


# Life Cycle  
def cyle(usrs):             # list of users
    global json
    while 1:
        for usr in usrs:    # Iterate over users
            # Finds the current_state -> returns state where state = current_state
            state = list(filter(lambda state: state['state'] == usr[1], jsonFile["state"]))[0]
            execute(usr, int(state['action']))
            usrs[usrs.index(usr)][1] = nextState(state['next_state'])   # Update State of User
            time.sleep(int(jsonFile['operation_delay']))                # Operation Delay


# Calculate Next State
def nextState(states):
    s = []      # Names
    p = []      # Probabilities
    for st in states:
        s.append(st["state"])       # State Name
        p.append(st["prob"])        # State Probability
    return random.choices(s, p)[0]      # Returns State taking into account the probabilities


# Divide List into lists of max size n
def divList(listUser, n):
    final = []          # Final list
    tmpList = []        # Temporary list
    i = 0
    while len(listUser) != 0:
        if (i != n):
            tmpList.append(listUser.pop())      # Add User to sublist
            i = i+1
        else:
            final.append(tmpList)               # Sublist added to Final List
            tmpList = []                        # Creation of new Sublist
            i=0
    final.append(tmpList)
    return final                                # Returns a list of sublists with max size n


# Main Function
def main(args):
    global jsonFile
    global pathFile

    # Main Variable
    users = []              # All Users -> [GitlabUser, current_state]
    threads = []            # All threads
    pathFile = args.f

    # read file
    with open('gitlab.json', 'r') as myfile: 
        jsonFile = json.loads(myfile.read())
    
    # Create Users -> [GitlabUser, current_state]
    for i in range(int(jsonFile["n_users"])):
        users.append([GitlabUser('user'+str(i), args.u, args.t), "create_project"])

    # Execute All Users (Threads)
    for x in divList(users, 3):                 # Number of threads (Configurable)
        thread = threading.Thread(target=cyle, args=(x,))
        thread.start()
        threads.append(thread)
    
    # Wait until all threads are done
    for t in threads:
        t.join()

    return 0
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gitlab user simulation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', type=str, default='http://localhost:8000', help='Gitlab address')
    parser.add_argument('-t', type=str, default='dLzcm6MGPyV5FbykEtQ3', help='Gitlab private token')
    parser.add_argument('-f', type=str, default='file.txt', help='Path to file')
    args = parser.parse_args()
    main(args)
