
#################################################################################################################################################

import py_misc

#################################################################################################################################################

# Get Data From PDA Server
def tag(tagname: str | list[str]):
    # Check for input Variable
    if (not isinstance(tagname, str) and
        not isinstance(tagname, list)
        ): return dict(error='tagname missing')

    try: # Request PDA Server
        res = py_misc.requests.post(
            'http://avbsrvssta:3001/api/ip21/',
            json=dict(tagname=tagname),
            auth=('client', '123456')
        )
        res = py_misc.json.loads(res.text)
    except: # If Server Not Responding
        res = dict(value=None, name=None, status='server down')

    # Return data
    return res

#################################################################################################################################################