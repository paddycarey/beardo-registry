# stdlib imports
import os

# third-party imports
from fabric.api import env
from fabric.api import put
from fabric.api import sudo

# local imports
from libdeploy import load_config


def with_config():
    """Load configuration from file
    """
    config = load_config()

    env.user = config['USERNAME']
    env.key_filename = '/app/secrets/deploy.pem'
    env.hosts = [config['HOSTNAME']]


def enable_and_start_service(service_path):

    # upload the service file
    service_name = os.path.split(service_path)[1]
    put(service_path, '/etc/systemd/system/{0}'.format(service_name), use_sudo=True)

    # enable and (re)start the service
    sudo('systemctl enable {0}'.format('/etc/systemd/system/{0}'.format(service_name)))
    sudo('systemctl restart {0}'.format(service_name))


def deploy():
    """Deploy current working tree to server
    """

    # deploy a private registry
    enable_and_start_service('/app/assets/registry.service')
