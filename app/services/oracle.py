
#################################################################################################################################################

# Imports
import os
import requests

#################################################################################################################################################

# Get Address
remote = os.getenv('ORACLE_SERVICE_ADDRESS')

#################################################################################################################################################

# Furnace
class furnace:

    def gusaapp():
        res = requests.get(
            url=f'{remote}/furnace/gusaapp/',
        )
        res.raise_for_status()
        return res.json()

#################################################################################################################################################
