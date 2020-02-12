#external_url 'https://gitlab.example.com'

# Prevent GitLab from starting if NFS data mounts are not available
high_availability['mountpoint'] = '/var/opt/gitlab/git-data'

# Disable components that will not be on the GitLab application server
roles ['application_role']
nginx['enable'] = true

#TODO: Confirm details about postgres: db_host and adapter
# PostgreSQL connection details 
gitlab_rails['db_adapter'] = 'postgresql'
gitlab_rails['db_encoding'] = 'unicode'
#gitlab_rails['db_host'] = '10.1.0.5' # IP/hostname of database server  
gitlab_rails['db_port'] = 5432
gitlab_rails['db_password'] = 'passworddb'

# Redis connection details
gitlab_rails['redis_port'] = '6379'
#gitlab_rails['redis_host'] = '10.1.0.6' # IP/hostname of Redis server
gitlab_rails['redis_password'] = 'passwordredis'

# Ensure UIDs and GIDs match between servers for permissions via NFS
user['uid'] = 9000
user['gid'] = 9000
web_server['uid'] = 9001
web_server['gid'] = 9001
registry['uid'] = 9002
registry['gid'] = 9002