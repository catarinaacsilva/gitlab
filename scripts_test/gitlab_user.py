# coding=utf-8

import gitlab
import logging


class GitlabUser:

    def __init__(self, name: str, url: str, token: str):
        self.name = name
        self.gl = gitlab.Gitlab(url, token)
        # make an API request to create the gl.user object. This is mandatory if you
        # use the username/password authentication.
        # self.gl.auth()

    # create a new user
    def create_user(self):
        user_data = {'email':  self.name + '@girs.com', 'username': self.name,
                     'name': self.name, 'password': self.name + self.name}
        self.user = self.gl.users.create(user_data)

    # create a new project
    def create_prj(self, project_name: str):
        self.user.projects.create({'name': project_name})

    # list all projects
    def get_all_projects(self):
        return self.user.projects.list()

    # TODO: Mudar o nome do caminho do ficheiro base
    def commit(self, project_name: str):
        project = None
        for p in self.user.projects.list():
            if p.name == project_name:
                project = p
        # See https://docs.gitlab.com/ce/api/commits.html#create-a-commit-with-multiple-files-and-actions
        # for actions detail
        data = {
            'branch': 'master',
            'commit_message': 'blah blah blah',
            'actions': [
                {
                    'action': 'create',
                    'file_path': 'README.rst',
                    'content': open('path/to/file.rst').read(),
                }
            ]
        }
        commit = project.commits.create(data)
        # print(commit) -- Opcional
