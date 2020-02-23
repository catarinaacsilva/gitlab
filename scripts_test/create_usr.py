import gitlab

gl = gitlab.Gitlab('http://localhost:8000', private_token='e7NNphfyD6HKTbsBPygx')

# create a new user
for u in range(5):
    usr = 'usr'+ str(u)
    user_data = {'email':  usr +'@girs.com', 'username': usr, 'name': usr,'password': usr + usr}
    user = gl.users.create(user_data)
    print(user)