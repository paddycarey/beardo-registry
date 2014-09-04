Beardo Registry
===============


Provides a simple private docker registry for use within the beardo platform.

**NOTE: Beardo is very much a work in progress and should not be used in production. The platform is insecure and makes very rigid assumptions about your architecture. These issues should be resolved in time, but for now you've been warned.**


Usage
=====

#### Running locally

Presuming that you already have docker installed, running locally should be as simple as checking out the repository `git clone git@github.com:beardo-project/beardo-registry.git` and using the included `Makefile` from the repository root:

```bash
$ make run
```

#### Deployment

Likewise, deployment happens via the included `Makefile`. First, you'll need to satisy a few prerequisites. At present these are quite strict and inflexible, but that'll be resolved with time:

- You must have an existing CoreOS instance deployed on Google Compute Engine (etcd and fleet are not required).
- A user must exist on the server that is able to use `sudo` and can be logged in as via SSH.
- The registry server is not locked down in any way, so it is essential that it is not exposed over a public interface (use a firewall/private network).
- A valid `hostname` and `username` should be configured in ``secrets/deploy.conf``.
- A valid SSH key is required for the configured user (in ``secrets/deploy.pem``)

Once the prerequisites are satisifed, you can deploy with:

```bash
$ make deploy
```
