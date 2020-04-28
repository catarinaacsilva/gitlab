# gitlab.rb

external_url 'http://gitlab.local'
registry_external_url 'http://registry.gitlab.local'

# Disable bundle services
postgresql['enable'] = false
redis['enable'] = false
prometheus['enable'] = false
postgres_exporter['enable'] = false
redis_exporter['enable'] = false
grafana['enable'] = false

# Postgres settings
gitlab_rails['db_adapter'] = "postgresql"
gitlab_rails['db_encoding'] = "unicode"

# database service will be named "postgres" in the stack
gitlab_rails['db_host'] = "postgres" 
gitlab_rails['db_database'] = "gitlab"
gitlab_rails['db_username'] = "gitlab"
gitlab_rails['db_password'] = "gitlab"

# Redis settings
# redis service will be named "redis" in the stack
gitlab_rails['redis_host'] = "redis"

# Prometheus exporters
#node_exporter['listen_address'] = '0.0.0.0:9100'
#gitlab_exporter['listen_address'] = '0.0.0.0'
#gitaly['prometheus_listen_addr'] = "0.0.0.0:9236"
#gitlab_workhorse['prometheus_listen_addr'] = "0.0.0.0:9229"
#sidekiq['listen_address'] = '0.0.0.0'
#gitlab_exporter['listen_port'] = '9168'

node_exporter['listen_address'] = '0.0.0.0:9100'
gitlab_monitor['listen_address'] = '0.0.0.0'
gitaly['prometheus_listen_addr'] = "0.0.0.0:9236"
gitlab_workhorse['prometheus_listen_addr'] = "0.0.0.0:9229"
