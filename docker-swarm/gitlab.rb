# gitlab.rb

external_url 'http://gitlab.local'
registry_external_url 'http://registry.gitlab.local'

# Disable e-mail
gitlab_rails['gitlab_email_enabled'] = false

# Reduce the amount of logs
logging['svlogd_size'] = 2 * 1024 * 1024 # rotate after 2 MB of log data
logging['svlogd_num'] = 3                # keep 3 rotated log files
logging['logrotate_rotate'] = 3          # keep 3 rotated logs

# Disable bundle services
postgresql['enable'] = false
redis['enable'] = false
prometheus['enable'] = false
postgres_exporter['enable'] = false
redis_exporter['enable'] = false
grafana['enable'] = false

# Postgres settings
gitlab_rails['db_adapter'] = 'postgresql'
gitlab_rails['db_encoding'] = 'utf8'

# database service will be named "postgres" in the stack
gitlab_rails['db_host'] = 'postgres'
gitlab_rails['db_database'] = 'gitlab'
gitlab_rails['db_username'] = 'gitlab'
gitlab_rails['db_password'] = 'gitlab'

# Enable or disable automatic database migrations
#gitlab_rails['auto_migrate'] = false

# Redis settings
# redis service will be named "redis" in the stack
gitlab_rails['redis_host'] = "redis"

# Prometheus exporters
node_exporter['listen_address'] = '0.0.0.0:9100'
gitlab_exporter['listen_address'] = '0.0.0.0'
gitaly['prometheus_listen_addr'] = "0.0.0.0:9236"
gitlab_workhorse['prometheus_listen_addr'] = "0.0.0.0:9229"
sidekiq['listen_address'] = '0.0.0.0'
gitlab_exporter['listen_port'] = '9168'

#node_exporter['listen_address'] = '0.0.0.0:9100'
#gitlab_monitor['listen_address'] = '0.0.0.0'
#gitaly['prometheus_listen_addr'] = "0.0.0.0:9236"
#gitlab_workhorse['prometheus_listen_addr'] = "0.0.0.0:9229"
