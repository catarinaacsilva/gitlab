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
	- Ports: 5000, 6000/UDP, 9600

## Logstash Inputs

1. Syslog
	- Receives logs from Gitlab - through port 6000 (udp)
2. SNMP
	- Receives SNMP messages that indicate the state of the network
	- host: "udp:10.2.0.", community: "gicgirs", version: "2c" 
	- IOD's: ".1.3.6.1.2.1.1.4.0", ".1.3.6.1.2.1.1.5.0" (still to choose)

## Installing ELK Stack

[ELK Stack](https://appfleet.com/blog/docker-centralized-logging-with-elk-stack/)

## Other links

[SNMP](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-snmp.html)
[Syslog](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-syslog.html)


## Authors

* **Catarina Silva** - [catarinaacsilva](https://github.com/catarinaacsilva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details