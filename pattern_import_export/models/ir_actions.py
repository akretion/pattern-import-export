# Copyright 2020 Akretion France (http://www.akretion.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class IrActions(models.Model):
    _inherit = "ir.actions.actions"

    @api.model
    def get_bindings(self, model_name):
        """
        Add actions to Import/Export into "more" menu of each object
        @param model_name:
        @return: dict
        """
        res = super().get_bindings(model_name)
        if not self.env.user.has_group("pattern_import_export.group_pattern_user"):
            return res
        actions = res.setdefault("action", [])
        action_ids = [action.get("id") for action in actions]
        for xml_id in [
            "pattern_import_export.action_export_with_pattern",
            "pattern_import_export.import_pattern_wizard_action",
        ]:
            action = self.env.ref(xml_id).sudo()
            if action.id not in action_ids:
                actions.append(action.read(["name", "binding_view_types"])[0])
        return res
