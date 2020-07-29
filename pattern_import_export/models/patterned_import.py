#  Copyright (c) Akretion 2020
#  License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo import models, fields


class PatternedImport(models.Model):
    _name = "patterned.import"
    _inherits = {"ir.attachment": "attachment_id"}

    attachment_id = fields.Many2one("ir.attachment")
    status = fields.Char()
    errors = fields.Char()
    info = fields.Char()
