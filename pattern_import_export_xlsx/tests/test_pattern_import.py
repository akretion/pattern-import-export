# Copyright 2020 Akretion France (http://www.akretion.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=missing-manifest-dependency

from odoo.tests.common import SavepointCase

from .common import ExportPatternXlsxCommon, CELL_VALUE_EMPTY


class TestPatternImport(ExportPatternXlsxCommon, SavepointCase):
    def test_import_xlsx(self):
        main_sheet = self.import_workbook_from_vals(self.excel_data_correct)
        self.assertEqual(self.partner_1.street, "updated street for Wood Corner")
        self.assertEqual(self.partner_2.country_id, self.country_be)
        expected_headers = [
            "id",
            "name",
            "street",
            "country_id|code",
            "parent_id|country_id|code",
            CELL_VALUE_EMPTY,
            CELL_VALUE_EMPTY,
        ]
        self._helper_check_headers(main_sheet, expected_headers)

    def test_import_xlsx_errors(self):
        main_sheet = self.import_workbook_from_vals(self.excel_data_incorrect)
        expected_headers = [
            "id",
            "name",
            "street",
            "country_id|code",
            "parent_id|country_id|code",
            "Errors",
            "Warnings",
        ]
        self._helper_check_headers(main_sheet, expected_headers)

    # def test_import_xlsx_m2m(self):
    #
    #
    # def test_import_xlsx_o2m(self):
