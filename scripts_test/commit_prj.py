import gitlab

gl = gitlab.Gitlab('http://localhost:8000', private_token='e7NNphfyD6HKTbsBPygx')

usr = 'usr0'
user = gl.users.list(username=usr)[0]
project = user.projects.list()[0]

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
print(commit)