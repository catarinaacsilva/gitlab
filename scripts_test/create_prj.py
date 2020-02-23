import gitlab

gl = gitlab.Gitlab('http://localhost:8000', private_token='e7NNphfyD6HKTbsBPygx')

# create a new project
for u in range(5):
    usr = 'usr0'
    user = gl.users.list(username=usr)[0]
    user_project = user.projects.create({'name': 'project_' + usr + '_' + str(u)})
    print(user_project)