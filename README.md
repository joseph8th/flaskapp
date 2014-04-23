Flask Demo
==========

With MongoDB and Facebook GraphAPI. A simple, self-contained Flask app that simply gets a valid OAuth Facebook Access Token from the user, and adds them to a MongoDB, then displays all the user's names on the index.

Requires a running `mongod` daemon.

Installation
============

Designed to run in a Python 2.7 `virtualenv` named `flask`, which should be **inside the root directory** (next to this `README` file).

Usage
=====

    $ ./rundemo.py

Then navigate to the displayed `localhost` port.

Author
======

Joseph Edwards VIII
jedwards8th@gmail.com

April 23, 2014