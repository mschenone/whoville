# coding: utf-8

"""
A set of defaults and parameters used elsewhere in the project.
Also provides a handy link to the low-level client SDK configuration singleton
objects.
"""

from __future__ import absolute_import
import logging
import sys
import os
import urllib3
from ruamel.yaml import safe_load
from whoville.cloudbreak import configuration as cb_config
from cloudera.director.common.configuration import Configuration as cdConfig


MIN_PYTHON = (3, 6)
# Param unpacking from Python3.5
# Secrets for security.py in Python3.6
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

# --- Profile File Name ------
profile_loc = os.environ.get("PROFILE")
if not profile_loc:
    profile_loc = 'profile.yml'


# --- Project Root -----
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# --- Profile Versioning ------
min_profile_ver = 3

# --- Logging ------
logging.basicConfig(level=logging.INFO)


# --- Cloudera Director Version
cad_ver = 'd6.1'

# --- Cloudera Director Configuration explicit import
cd_config = cdConfig()

# --- Default Host URL -----
# Set Default Host for Cloudbreak
cb_config.host = 'https://localhost/cb/api'
# The Altus Director client appends the api endpoint itself
cd_config.host = 'https://localhost'


# --- Task wait delays ------
# Set how fast to recheck for completion of a short running task in seconds
short_retry_delay = 0.5
# Set the max wait time for a short running task to complete in seconds
short_max_wait = 3
# Long running task delay
long_retry_delay = 5
# and long max wait
long_max_wait = 120


# --- Cloudbreak Security
cb_config.verify_ssl = False
cd_config.verify_ssl = False
if not cb_config.verify_ssl:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Resolve Configuration overrides from local profile
try:
    with open(str(profile_loc), 'r') as f:
        profile = safe_load(f.read())
except IOError as e:
    raise IOError("profile.yml not found - Have you set your Profile up?")
