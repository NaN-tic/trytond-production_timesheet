# This file is part production_timesheet module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from decimal import Decimal
import datetime

from trytond.model import fields
from trytond.pyson import Eval
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta
from trytond.tools import reduce_ids

__all__ = ['Production']
__metaclass__ = PoolMeta


class Production:
    __name__ = "production"
    work = fields.Many2One('timesheet.work', 'Work')
    timesheet_cost = fields.Function(fields.Numeric('Timesheet Cost',
            digits=(16, Eval('currency_digits', 2)),
            depends=['currency_digits']),
        'on_change_with_timesheet_cost')
    total_cost = fields.Function(fields.Numeric('Total Cost',
            digits=(16, Eval('currency_digits', 2)),
            depends=['currency_digits']),
        'on_change_with_total_cost')
    currency_digits = fields.Function(fields.Integer('Currency Digits'),
        'on_change_with_currency_digits')

    @classmethod
    def default_currency_digits(cls):
        return 2

    @fields.depends('work')
    def on_change_with_timesheet_cost(self, name=None):
        return self.work.cost if self.work else 0

    @fields.depends('cost', 'timesheet_cost')
    def on_change_with_total_cost(self, name=None):
        return self.cost + self.timesheet_cost

    @fields.depends('company')
    def on_change_with_currency_digits(self, name=None):
        if self.company:
            return self.company.currency.digits
        return 2
