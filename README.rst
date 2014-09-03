===============
beardo-registry
===============

Provides a simple private docker registry for use within the beardo platform.

.. note::
    beardo is very much a work in progress and shoult not be used in
    production. The platform is insecure and makes very rigid assumptions
    about your architecture. These issues should be resolved in time, but for
    now you've been warned.

* Free software: `MIT license <http://opensource.org/licenses/MIT>`_
* Documentation: http://beardo-project.rtfd.org.


Usage
=====

* Running locally is easy with docker::

    $ make run

* Deployment is just as easy with docker. First, provide an SSH key (in
``secrets/deploy.pem``) and fill in your credentials in
``secrets/deploy.conf``. Once your secrets are in place, deployment to a
CoreOS instance should be as simple as::

    $ make deploy
