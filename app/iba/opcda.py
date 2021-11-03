
#################################################################################################################################################

# Imports
import os
import json
import requests

#################################################################################################################################################

# Get Data From PDA Server
def tag(tagname: str | list[str]):
    # Check for input Variable
    if (not isinstance(tagname, str) and
        not isinstance(tagname, list)
        ): return dict(error='tagname missing')

    try: # Request PDA Server
        res = requests.post(
            url=os.getenv('AVB_IBA_OPC_DA_ADDR'),
            auth=(
                os.getenv('AVB_IBA_OPC_DA_USER'),
                os.getenv('AVB_IBA_OPC_DA_PASSWORD')
            ),
            json={ 'tagname': tagname }
        )
        res = json.loads(res.text)
    except: # If Server Not Responding
        res = dict(value=None, name=None, status='server down')

    # Return data
    return res

#################################################################################################################################################