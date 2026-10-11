# Copyright 2021 Akretion (https://www.akretion.com).
# @author Kévin Roche <kevin.roche@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Pattern export custom header",
    "summary": "Allow to use custom headers names in export files",
    "version": "18.0.1.0.0",
    "category": "Extra Tools",
    "maintainers": ["kev-roche"],
    "website": "https://github.com/akretion/pattern-import-export",
    "author": "Akretion, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "pattern_import_export",
    ],
    "data": [
        "views/pattern_config.xml",
        "security/ir.model.access.csv",
    ],
}
