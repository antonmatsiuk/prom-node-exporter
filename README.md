Role Name
=========

Ansible role to install prometheus node_exporter on CentOS/RHEL7

Requirements
------------

CentOS7 /RHEL7 Linux Distribution

Role Variables
--------------
Available variables with default values (see defaults/main.yml):

IP and Port on which node_exporter listens. Change IP to an appropriate value e.g. `{{ ansible_eth0.ipv4.address }}` 
to listen on a specific interface:

    node_exporter_port: 9100
    node_exporter_ip: "0.0.0.0"


Dependencies
------------
none 

Example Playbook
----------------
    - hosts: servers
      roles:
         - antonmatsiuk.prom_node_exporter

License
-------

MIT / BSD

Author Information
------------------

DevOps / SRE / Cloud Engineer [Anton Matsiuk](https://github.com/antonmatsiuk)