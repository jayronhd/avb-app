
##########################################################################################################################

# Imports
import os
import json
import flask
import py_misc

# Modules
from .modules import laminador
from .modules import aciaria
from .modules import sap
from .modules import iba

##########################################################################################################################

# Declare HTTP API
app = py_misc.Express()

# Set API Port
app.port(
    int(os.getenv('ODBC_SERVICE_PORT'))
)

#################################################################################################################################################

Request = flask.Request
Response = flask.Response

##########################################################################################################################

@app.route('/odbc/sap/preditivas/')
def sapPreditivas(req: Request, res: Response):
    try:
        kwargs = req.json
        data = sap.preditivas(kwargs['equip'])
        return res(
            json.dumps(data),
            mimetype='application/json',
            status=200
        )
    except Exception as e:
        return res(
            json.dumps({ 'error': str(e) }),
            mimetype='application/json',
            status=200
        )

##########################################################################################################################

@app.route('/odbc/aciaria/ld/espectrometro/')
def aciariaLDEspectrometro(req: Request, res: Response):
    data = aciaria.ld.espectrometro()
    return res(
        json.dumps(data),
        mimetype='application/json',
        status=200
    )

##########################################################################################################################

@app.route('/odbc/aciaria/fp/espectrometro/')
def aciariaFPEspectrometro(req: Request, res: Response):
    data = aciaria.fp.espectrometro()
    return res(
        json.dumps(data),
        mimetype='application/json',
        status=200
    )

##########################################################################################################################

@app.route('/odbc/laminador/produto/')
def laminadorRFAL2(req: Request, res: Response):
    data = laminador.produto()
    return res(
        json.dumps(data),
        mimetype='application/json',
        status=200
    )

##########################################################################################################################

@app.route('/odbc/laminador/blbp/')
def laminadorRFAL2(req: Request, res: Response):
    data = laminador.blbp()
    return res(
        json.dumps(data),
        mimetype='application/json',
        status=200
    )

##########################################################################################################################

@app.route('/odbc/laminador/rfa/')
def laminadorRFA(req: Request, res: Response):
    data = laminador.rfa()
    return res(
        json.dumps(data),
        mimetype='application/json',
        status=200
    )

##########################################################################################################################

@app.route('/odbc/laminador/rfal2/')
def laminadorRFAL2(req: Request, res: Response):
    data = laminador.rfal2()
    return res(
        json.dumps(data),
        mimetype='application/json',
        status=200
    )

##########################################################################################################################

# Scheduled Actions
@py_misc.schedule.each.one.hour.do.at('00:00')
def each_one_hour():
    iba.clear()

##########################################################################################################################

# Start Server
app.start()

# Keep Main Thread Alive
py_misc.keepalive()

##########################################################################################################################
