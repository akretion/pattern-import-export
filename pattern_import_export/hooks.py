# Copyright (C) 2025 Akretion (<http://www.akretion.com>).
# @author Kévin Roche <kevin.roche@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    all_export_lines = env["ir.exports.line"].search([])
    line_to_process = all_export_lines.filtered(lambda x: ".id" in x.name)
    line_to_delete = env["ir.exports.line"]
    for line in line_to_process:
        new_name = line.name.replace(".id", "id")
        lines_from_export = env["ir.exports.line"].search(
            [("export_id", "=", line.export_id.id)]
        )
        if not any(
            [
                new_name in line_from_export.name
                for line_from_export in lines_from_export
            ]
        ):
            line.write({"name": new_name})
        else:
            line_to_delete += line
    line_to_delete.unlink()
