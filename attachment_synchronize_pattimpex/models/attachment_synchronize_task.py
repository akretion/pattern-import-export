# Copyright 2020 Akretion (http://www.akretion.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import fields, models
from odoo.tools import safe_eval

_logger = logging.getLogger(__name__)


class AttachmentSynchronizeTask(models.Model):
    _inherit = "attachment.synchronize.task"
    domain_pattimpex_export = fields.Char(
        string="Domain for filtering records to export", default="[]"
    )
    export_id = fields.Many2one("ir.exports", string="Import/Export pattern")
    file_type = fields.Selection(
        selection_add=[
            ("import_pattern", "Import using Patterns"),
            ("export", "Import using Patterns"),
        ]
    )
    # Export part

    def _get_records_to_export(self):
        model_name = self.export_id.resource
        domain = safe_eval(self.domain_pattimpex_export)
        return self.env[model_name].search(domain)

    def service_trigger_exports(self):
        records = self._get_records_to_export()
        records.with_context(
            self.env.context, export_patterned_attachment_queue=self.id
        )._generate_export_with_pattern_job(self.export_id)

    # Import part

    def _prepare_attachment_vals(self, data, filename):
        vals = super()._prepare_attachment_vals(data, filename)
        if self.export_id:
            vals["export_id"] = self.export_id.id
        return vals
