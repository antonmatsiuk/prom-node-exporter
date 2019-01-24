import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_node_exporter_running_and_enabled(host):
    node_exporter = host.service('node_exporter')
    assert node_exporter.is_enabled


def test_node_exporter_enabled(host):
    ansible_vars = \
        host.ansible("include_vars",
                     "file=../../defaults/main.yml")["ansible_facts"]
    node_exporter_port = ansible_vars["node_exporter_port"]
    node_exporter_ip = ansible_vars["node_exporter_ip"]
    socket = host.socket('tcp://%s:%s' % (node_exporter_ip, node_exporter_port))
    assert socket.is_listening
