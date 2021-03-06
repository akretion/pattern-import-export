# Copyright 2020 Akretion France (http://www.akretion.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, api, fields, models


class ExportPatternWizard(models.Model):
    _name = "export.pattern.wizard"
    _description = "Export pattern wizard"

    model = fields.Char(
        string="Model to export",
        default=lambda s: s.env.context.get("active_model", False),
    )
    ir_exports_id = fields.Many2one("ir.exports", string="Export Pattern")
    no_export_pattern = fields.Boolean(
        string="No Export Pattern", compute="_compute_no_export_pattern"
    )

    @api.depends("model")
    @api.multi
    def _compute_no_export_pattern(self):
        for wiz in self:
            ir_exports = wiz.env["ir.exports"].search_count(
                [("resource", "=", wiz.model)]
            )
            if not ir_exports:
                wiz.no_export_pattern = True

    @api.multi
    def run(self):
        """
        Launch the export
        @return: dict
        """
        for wiz in self:
            description = _(
                "Generate export '{model}' with export pattern "
                "'{export_name}' using format {format}"
            ).format(
                model=wiz.model,
                export_name=wiz.ir_exports_id.name,
                format=wiz.ir_exports_id.export_format,
            )
            records = self.env[wiz.model].browse(
                self.env.context.get("active_ids", False)
            )
            records.with_delay(
                description=description
            )._generate_export_with_pattern_job(wiz.ir_exports_id)
        return {}
