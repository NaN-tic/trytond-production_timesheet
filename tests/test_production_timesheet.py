# This file is part of the production_timesheet module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductionTimesheetTestCase(ModuleTestCase):
    'Test Production Timesheet module'
    module = 'production_timesheet'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductionTimesheetTestCase))
    return suite
