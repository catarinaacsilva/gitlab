'''
---------------------------------------------------------------------------------------------------
-- Gitlab User
-- Authors: Catarina Silva, 76399; Duarte Dias, 80214
-- Emails: c.alexandracorreia@ua.pt; duarterochadias@ua.pt 

-- Version 2.0 
---------------------------------------------------------------------------------------------------
'''

# coding=utf-8

import gitlab
import logging
import random


class GitlabUser:

    def __init__(self, name: str, url: str, token: str):
        self.name = str(name)
        self.gl = gitlab.Gitlab(url, token)

        # check if the user already exists
        if self.user_exists():
            # retrieves the user
            self.user = self.gl.users.list(username=self.name)[0]
        else:
            # create a new user
            user_data = {'email':  self.name + '@girs.com', 'username': self.name,
                     'name': self.name, 'password': self.name + self.name}
            self.user = self.gl.users.create(user_data)

    # User name
    def get_name(self):
        return self.name

    # check if the user already exists
    def user_exists(self):
        user = self.gl.users.list(username=self.name)
        if user != []:
            return True
        return False
    
    # list all users
    def get_all_users(self):
        return self.gl.user.list()

    # delete user
    def delete_user(self):
        self.user.delete()

    # create a new project
    def create_prj(self, project_name: str):
        self.user.projects.create({'name': project_name})

    # delete a project
    def delete_prj(self, project_name: str):
        project = self.gl.projects.list(search=project_name)
        project.delete()

    # list all projects id
    def get_all_projects(self):
        return self.user.projects.list()

    # random project 
    def get_rand_project(self):
        return gl.projects.get(random.choice(self.user.projects.list()).id)

    # commit (create/update/delete)
    def commit(self, project, action: str, file_path: str, content: str):
        if action == 'create' or action == 'update':
            data = {
            'branch': 'master',
            'commit_message': file_path + ' ' + action + 'd',
            'actions': [
                {
                    'action': action,
                    'file_path': file_path,
                    'content': open(content).read(),
                }
            ]
        }
        else:           # If action == delete
            data = {
            'branch': 'master',
            'commit_message': file_path + ' ' + action + 'd',
            'actions': [
                {
                    'action': action,
                    'file_path': file_path,
                }
            ]
        }
        project.commits.update(data)
        
    # Number Files created
    def get_nFC_project(self, project):
        listC = project.commits.list()
        cnt = 0
        for c in listC:
            if (str(project.commits.get(c.id).title).split())[1] == 'created':
                cnt = cnt + 1
        return cnt

    # File Name to update/delete
    def get_fileN_project(self, project):
        listC = project.commits.list()      # List of All commits for that project
        listC.reverse()                     # Reverse order to chronological order
        d = {}                              # Status of every Files of project
    
        for c in listC:
            tmp = str(project.commits.get(c.id).title).split()
            d[tmp[0]] = tmp[1]              # Assignment State of each file (created/updated/deleted)

        filt = {k : v for k,v in d.items() if v == 'created' or v == 'updated'}     # Select only files with state (created/updated)
        listN = list(filt.keys())
        if len(listN) == 0:                 # No files Found
            return 'FNF'
        else:                               # Returns Random File Name
            return random.choice(listN)      