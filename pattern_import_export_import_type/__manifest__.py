# Copyright 2023 Akretion (https://www.akretion.com).
# @author Kévin Roche <kevin.roche@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Pattern Import Export Import Type",
    "summary": "Import Type (only update, create or both)",
    "version": "18.0.1.0.0",
    "category": "Extra Tools",
    "website": "https://github.com/akretion/pattern-import-export",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["Kev-Roche"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "pattern_import_export",
    ],
    "data": [
        "views/pattern_config.xml",
    ],
}
