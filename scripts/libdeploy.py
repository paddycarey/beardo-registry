# stdlib imports
import re


def load_config():
    """Pulled from Honcho code with minor updates, reads local default
    environment variables from a local file.
    """
    try:
        with open('/app/secrets/deploy.conf') as f:
            content = f.read()
    except IOError:
        content = ''

    config = {}
    for line in content.splitlines():
        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))
            config[key] = val
    return config
