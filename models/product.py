# -*- coding: utf-8 -*-
from openerp.models import Model
from openerp.fields import Char


class product(Model):
    _name = "product_manual_variants.product"

    name = Char()
