/*
##########################################################################################################################
#                                                    TS-HOMERICO-AVBOT                                                   #
##########################################################################################################################
#                                                                                                                        #
#                                                   AVB Whatsapp Bot                                                     #
#                                          Multi-language API for Whatsapp Bot                                           #
#                                 ---------------- Python3 -- NodeJS ----------------                                    #
#                                                * Under Development *                                                   #
#                                     https://github.com/anthony-freitas/ts-avbot                                        #
#                                                                                                                        #
##########################################################################################################################
#                                                        MAIN CODE                                                       #
##########################################################################################################################
*/

// Import Homerico
import HomericoConexao from 'ts-homerico'

// Imports
import express from 'express'

/*
##########################################################################################################################
#                                                          MAIN                                                          #
##########################################################################################################################
*/

// Instance Homerico
const homerico = new HomericoConexao()

// Homerico Authentication
homerico.validar(process.env.HOMERICO_GATEWAY)
homerico.login(
    process.env.HOMERICO_USER,
    process.env.HOMERICO_PASSWORD
)

/*
##########################################################################################################################
#                                                          END                                                           #
##########################################################################################################################
*/
