# This file is part production_timesheet module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .production import *


def register():
    Pool.register(
        Production,
        module='production_timesheet', type_='model')
