#!/usr/bin/env python
import os
import sys

# local imports
from libdeploy import load_config


def main():
    """Run a few pre-deploy checks to make sure config is set.
    """

    # validate that an ssh key is present in the 'secrets' directory
    dk_path = '/app/secrets/deploy.pem'
    if not os.path.exists(dk_path):
        print 'Deploy key missing: secrets/deploy.pem'
        sys.exit(1)

    # validate that a config file is present in the 'secrets' directory
    dc_path = '/app/secrets/deploy.conf'
    if not os.path.exists(dc_path):
        print 'Deploy configuration missing: secrets/deploy.conf'
        sys.exit(1)

    config = load_config()
    if not config['USERNAME'] or not config['HOSTNAME']:
        print 'Invalid configuration.'
        sys.exit(1)


if __name__ == '__main__':
    main()
