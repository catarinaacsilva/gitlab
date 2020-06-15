# Gitlab - Monitoring with ELK

Monitoring Gitlab logs and network status (SNMP)

## General Information

1. VM
	- Server IP: 10.5.0.7
	- Username: gitlab
	- Password: gitlab

## Accessing Server 5

1. Through SSH
	- ssh gitlab@10.5.0.7
	- usr: gitlab, pass: gitlab
	- Needs to be connected via UA VPN and GIRS VPN 
2. Through Web
	- URL: https://srv5-deti.ua.pt:8006/
	- usr: gicgirs, pass: gicgirs
	- Virtual Machine (VM) number 106 (gitlab)
	- Needs to be connected via UA VPN

## Accessing Kibana

1. Through Web
	- URL: http://10.5.0.7:5601
	- usr: elastic, pass: gitlab
	- Needs to be connected via UA VPN and GIRS VPN 

## ELK Ports

1. Kibana
	- Port: 5601
2. Elasticsearch
	- Ports: 9200, 9300
3. Logstash
	- Ports: 5000, 5114, 9600

## Logstash Inputs

1. Syslog
	- Receives logs from Gitlab - through port 5114 (tcp)
2. SNMP
	- Receives SNMP messages that indicate the state of the devices
	- host: "udp:10.2.0.", community: "gicgirs", version: "2c" 
	- IOD's: ".1.3.6.1.4.1.2021.11.10.0", ".1.3.6.1.4.1.2021.11.11.0", ".1.3.6.1.4.1.2021.9.1.9.9", ".1.3.6.1.4.1.2021.4.5.0", ".1.3.6.1.4.1.2021.4.6.0"

## Installing ELK Stack

[ELK Stack](https://appfleet.com/blog/docker-centralized-logging-with-elk-stack/)

## Other links

[SNMP](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-snmp.html)
[Syslog](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-syslog.html)

## Authors

- **Catarina Silva**
- **Duarte Dias**