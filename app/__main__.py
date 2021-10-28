
#################################################################################################################################################

# Imports
import py_misc

# Modules
from . import homerico
from . import routes

#################################################################################################################################################

# Setup Homerico Connection
homerico.Validar('homerico.avb')
homerico.Login('CH1200', 'bhn860')

#################################################################################################################################################

# Declare HTTP API
app = py_misc.API().host('0.0.0.0').port(3000)

#################################################################################################################################################

# Load Routes
routes.__load__(app)

#################################################################################################################################################

# start server
app.start()

# keep main thread alive
py_misc.keepalive()

#################################################################################################################################################
