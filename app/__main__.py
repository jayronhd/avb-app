
#################################################################################################################################################

# Imports
import os
import py_misc

# Modules
from . import homerico
from . import routes

#################################################################################################################################################

# Setup Homerico Connection
homerico.addr(os.getenv('HOMERICO_NETWORK_ADDR'))
homerico.auth(
    user=os.getenv('HOMERICO_NETWORK_USER'),
    password=os.getenv('HOMERICO_NETWORK_PASSWORD')
)

#################################################################################################################################################

# Declare HTTP API
app = py_misc.API().host('0.0.0.0')
app.port(os.getenv('AVB_APP_PORT'))

#################################################################################################################################################

# Load Routes
routes.__load__(app)

#################################################################################################################################################

# start server
app.start()

# keep main thread alive
py_misc.keepalive()

#################################################################################################################################################
