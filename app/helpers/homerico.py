
#################################################################################################################################################

# Imports
import copy
import datetime

# Modules
from ..services import homerico as network
from . import functions

#################################################################################################################################################
#                                                       HOMERICO GETTERS                                                                        #
#################################################################################################################################################

# relatorio gerencial parser
def RelatorioGerencialReport(
    idReport: int,
    registros: dict[str, int] = {},
    data: str = None
):
    # get Inputs
    if data == None:
        data = datetime.date.today().strftime('%d/%m/%Y')
    _registros = copy.deepcopy(registros)

    # Private Map Function
    def _replace_reg(row):
        if row[0] in list(_registros.values()):
            for reg in _registros:
                row[0] = reg if (row[0] == _registros[reg]) else row[0]
            _registros.update({
                row[0]: {
                    'meta': functions.num(row[1], True),
                    'dia': functions.num(row[2], True),
                    'acumulado': functions.num(row[3], True)
                }
            })
        else: return None
        return row

    # Turn to String
    for i in _registros:
        _registros[i] = str(_registros[i])
    
    # Get Data
    csv = network.RelatorioGerencialReport(
        data=data,
        idReport=str(idReport)
    )
    list(map(_replace_reg, functions.matrix(csv)))

    # Fix Wrong Data
    for item in list(_registros):
        _registros[item] = (
            _registros[item]
            if isinstance(_registros[item], dict)
            else {
                'meta': None,
                'dia': None,
                'acumulado': None
            }
        )
    
    # Return Data
    return _registros

#################################################################################################################################################

# relatorio gerencial
def RelatorioGerencialTrimestre(
    idReport: int,
    registros: dict[str, int] = dict(),
    data: str = None
):
    if data == None:
        data = datetime.date.today().strftime('%d/%m/%Y')
    timed = datetime.datetime.strptime(data, '%d/%m/%Y')
    report = RelatorioGerencialReport(
        idReport=idReport,
        registros=registros,
        data=data
    )
    qt = (3 * (1 + ((timed.month - 1) // 3)))
    m = [qt-2, qt-1, qt]
    for i in m:
        last_day = functions.lastDayOfMonth(
            datetime.date(timed.year, i, 1)
        ).day
        if i == timed.month: last_day = timed.day
        _date = datetime.date(timed.year, i, last_day).strftime('%d/%m/%Y')
        e = RelatorioGerencialReport(
            idReport=idReport,
            registros=registros,
            data=_date
        )
        for item in report:
            mes = 'mes{}'.format(i-qt+3)
            report[item][mes] = e[item]['acumulado']
    return report

#################################################################################################################################################

# relatorio gerencial
def RelatorioGerencialRegistro(
    registro: int,
    data: str = None
):
    if data == None:
        data = datetime.date.today().strftime('%d/%m/%Y')
    homerico_csv = network.RelatorioGerencialRegistro(
        data=data,
        registro=str(registro)
    )
    return functions.matrix(homerico_csv)

#################################################################################################################################################

# producao lista
def ProducaoLista(
    lista: int,
    data: str = None
):
    if data == None:
        data = datetime.date.today()
    last_day = functions.lastDayOfMonth(data).strftime('%d/%m/%Y')
    homerico_csv = network.ProducaoLista(
        dataFinal=last_day,
        controle=str(lista)
    )
    dados = functions.matrix(homerico_csv)
    dados.pop(0)
    d = list()
    for item in dados:
        if len(item) != 3: dados.pop(dados.index(item))
    for item in dados:
        data = '{}{}'.format(item[0][:2].zfill(2), last_day[2:])
        d.append({
            'data': data,
            'peso': functions.num(item[2], True)
        })
    return d

#################################################################################################################################################
