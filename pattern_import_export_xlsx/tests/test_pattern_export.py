# Copyright 2020 Akretion France (http://www.akretion.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=missing-manifest-dependency

import base64
from xlrd import open_workbook

from odoo.tests.common import SavepointCase

# pylint: disable=odoo-addons-relative-import
from odoo.addons.pattern_import_export.tests.common import ExportPatternCommon

class TestPatternExport(ExportPatternCommon, SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for el in cls.ir_exports, cls.ir_exports_m2m, cls.ir_exports_o2m:
            el.export_format = "xlsx"

    # def test_generate_pattern_with_basic_fields(self):
    #     self.ir_exports.pattern_last_generation_date = False
    #     self.ir_exports.pattern_file = False
    #     self.ir_exports.export_fields[0].unlink()
    #     self.ir_exports.export_fields[2:].unlink()
    #     res = self.ir_exports.generate_pattern()
    #     self.assertEqual(res, True)
    #     self.assertNotEqual(self.ir_exports.pattern_file, False)
    #     self.assertNotEqual(self.ir_exports.pattern_last_generation_date, False)
    #     decoded_data = base64.b64decode(self.ir_exports.pattern_file)
    #     wb = open_workbook(file_contents=decoded_data)
    #     sheet1 = wb.sheet_by_index(0)
    #     self.assertEqual(sheet1.name, "Partner list")
    #     self.assertEqual(sheet1.cell_value(0, 0), "Name")
    #     self.assertEqual(sheet1.cell_value(0, 1), "Street")
    #
    # def test_generate_pattern_with_many2one_fields(self):
    #     self.ir_exports.export_fields[0:3].unlink()
    #     self.ir_exports.export_fields[1].unlink()
    #     self.ir_exports.generate_pattern()
    #     decoded_data = base64.b64decode(self.ir_exports.pattern_file)
    #     wb = open_workbook(file_contents=decoded_data)
    #     self.assertEqual(len(wb.sheets()), 2)
    #     sheet1 = wb.sheet_by_index(0)
    #     self.assertEqual(sheet1.cell_value(0, 0), "Country|Country Code")
    #     sheet2 = wb.sheet_by_index(1)
    #     self.assertEqual(sheet2.name, "Country list (code)")
    #     self.assertEqual(sheet2.cell_value(1, 0), "BE")
    #     self.assertEqual(sheet2.cell_value(2, 0), "FR")
    #     self.assertEqual(sheet2.cell_value(3, 0), "US")
    #
    # def _check_is_many2many(self, export_lines):
    #     """
    #     Ensure the is_many2many is correct for given export lines.
    #     """
    #     for export_line in export_lines:
    #         expected_result = False
    #         if (
    #             export_line.is_many2x
    #             and export_line.export_id.resource
    #             and export_line.name
    #         ):
    #             field, model = export_line._get_last_field(
    #                 export_line.export_id.resource, export_line.name
    #             )
    #             if self.env[model]._fields[field].type == "many2many":
    #                 expected_result = True
    #         if expected_result:
    #             self.assertTrue(export_line.is_many2many)
    #         else:
    #             self.assertFalse(export_line.is_many2many)
    #
    # def test_generate_pattern_is_many2many(self):
    #     """
    #     Ensure the is_many2many boolean field on the ir.exports.line
    #     is correctly set.
    #     """
    #     self._check_is_many2many(self.ir_exports.export_fields)
    #     self._check_is_many2many(self.ir_exports_m2m.export_fields)
    #
    # def test_generate_pattern_with_many2many_select_tab(self):
    #     """
    #     Ensure there is a second tab about companies and ensure the content
    #     is correct.
    #     """
    #     for export_line in self.ir_exports_m2m.export_fields:
    #         if not export_line.is_many2many:
    #             export_line.unlink()
    #     # Ensure still at least 1 line!
    #     self.assertTrue(self.ir_exports_m2m.export_fields)
    #     self.ir_exports_m2m.generate_pattern()
    #     decoded_data = base64.b64decode(self.ir_exports_m2m.pattern_file)
    #     wb = open_workbook(file_contents=decoded_data)
    #     self.assertEqual(len(wb.sheets()), 2)
    #     sheet2 = wb.sheet_by_index(1)
    #     companies = self.env["res.company"].search([])
    #     expected_sheet_name = "{name} ({field})".format(
    #         name=self.select_tab_company.name, field="name"
    #     )
    #     self.assertEquals(expected_sheet_name, sheet2.name)
    #     # Start at 1 because 0 is the header
    #     for ind, company in enumerate(companies, start=1):
    #         self.assertEquals(company.name, sheet2.cell_value(ind, 0))
    #
    # def test_generate_pattern_with_many2many_fields1(self):
    #     """
    #     Test the excel generation for M2M fields with 1 occurence.
    #     Only header part
    #     """
    #     for export_line in self.ir_exports_m2m.export_fields:
    #         if not export_line.is_many2many:
    #             export_line.unlink()
    #     # Ensure still at least 1 line!
    #     self.assertTrue(self.ir_exports_m2m.export_fields)
    #     self.ir_exports_m2m.generate_pattern()
    #     decoded_data = base64.b64decode(self.ir_exports_m2m.pattern_file)
    #     wb = open_workbook(file_contents=decoded_data)
    #     self.assertEqual(len(wb.sheets()), 2)
    #     sheet1 = wb.sheet_by_index(0)
    #     column_name = "{name}{sep}{nb}{sep}{f_name}".format(
    #         name="Companies", sep=self.separator, nb=1, f_name="Company Name"
    #     )
    #     self.assertEquals(column_name, sheet1.cell_value(0, 0))
    #
    # def test_generate_pattern_with_many2many_fields2(self):
    #     """
    #     Test the excel generation for M2M fields with more than 1 occurence.
    #     Only header part!
    #     """
    #     for export_line in self.ir_exports_m2m.export_fields:
    #         if not export_line.is_many2many:
    #             export_line.unlink()
    #     # Ensure still at least 1 line!
    #     self.assertTrue(self.ir_exports_m2m.export_fields)
    #     self.ir_exports_m2m.export_fields.write({"number_occurence": 5})
    #     self.ir_exports_m2m.generate_pattern()
    #     decoded_data = base64.b64decode(self.ir_exports_m2m.pattern_file)
    #     wb = open_workbook(file_contents=decoded_data)
    #     self.assertEqual(len(wb.sheets()), 2)
    #     sheet1 = wb.sheet_by_index(0)
    #     for nb in range(self.ir_exports_m2m.export_fields.number_occurence):
    #         column_name = "{name}{sep}{nb}{sep}{f_name}".format(
    #             name="Companies", sep=self.separator, nb=nb + 1, f_name="Company Name"
    #         )
    #         self.assertEquals(column_name, sheet1.cell_value(0, nb))
    #
    # def test_generate_pattern_with_many2many_fields3(self):
    #     """
    #     Test the excel generation for M2M fields with more than 1 occurence.
    #     Test only the content part
    #     """
    #     # Ensure still at least 1 line!
    #     nb_occurence = 4
    #     export_fields_m2m = self.ir_exports_m2m.export_fields.filtered(
    #         lambda l: l.is_many2many
    #     )
    #     self.assertTrue(export_fields_m2m)
    #     export_fields_m2m.write({"number_occurence": nb_occurence})
    #     users = self.env["res.users"].search([])
    #     self.ir_exports_m2m._export_with_record(users)
    #     attachment = self._get_attachment(self.ir_exports_m2m)
    #     expected_attachment_name = "{name}{ext}".format(
    #         name=self.ir_exports_m2m.name, ext=".xlsx"
    #     )
    #     self.assertEquals(expected_attachment_name, attachment.name)
    #     decoded_data = base64.b64decode(attachment.datas)
    #     wb = open_workbook(file_contents=decoded_data)
    #     sheet1 = wb.sheet_by_index(0)
    #     for ind, user in enumerate(users, start=1):
    #         xml_id = user.get_xml_id().get(user.id, "")
    #         self.assertEquals(xml_id, sheet1.cell_value(ind, 0))
    #         self.assertEquals(user.name or "", sheet1.cell_value(ind, 1))
    #         for ind_company, company in enumerate(user.company_ids, start=2):
    #             self.assertEquals(
    #                 company.name or "", sheet1.cell_value(ind, ind_company)
    #             )
    #         ind_already_checked = max(1, ind_company + 1)
    #         # Ensure others are empty
    #         for ind_company in range(ind_already_checked, nb_occurence):
    #             self.assertEquals("", sheet1.cell_value(ind, ind_company))

    # def test_export_with_record(self):
    #     self.ir_exports.export_fields[4].unlink()
    #     self.ir_exports._export_with_record(self.partners)
    #     attachment = self._get_attachment(self.ir_exports)
    #     self.assertEqual(attachment.name, "Partner list.xlsx")
    #     decoded_data = base64.b64decode(attachment.datas)
    #     wb = open_workbook(file_contents=decoded_data)
    #     sheet1 = wb.sheet_by_index(0)
    #     self.assertEqual(sheet1.cell_value(1, 0), "base.res_partner_1")
    #     self.assertEqual(sheet1.cell_value(2, 0), "base.res_partner_2")
    #     self.assertEqual(sheet1.cell_value(3, 0), "base.res_partner_3")
    #     self.assertEqual(sheet1.cell_value(1, 1), "Wood Corner")
    #     self.assertEqual(sheet1.cell_value(2, 1), "Deco Addict")
    #     self.assertEqual(sheet1.cell_value(3, 1), "Gemini Furniture")
    #     self.assertEqual(sheet1.cell_value(1, 2), "1164 Cambridge Drive")
    #     self.assertEqual(sheet1.cell_value(2, 2), "325 Elsie Drive")
    #     self.assertEqual(sheet1.cell_value(3, 2), "1128 Lunetta Street")
    #     self.assertEqual(sheet1.cell_value(1, 3), "US")
    #     self.assertEqual(sheet1.cell_value(2, 3), "US")
    #     self.assertEqual(sheet1.cell_value(3, 3), "US")
    #
    # def test_export_multi_level_fields(self):
    #     self.ir_exports._export_with_record(self.partner_2)
    #     attachment = self._get_attachment(self.ir_exports)
    #     self.assertEqual(attachment.name, "Partner list.xlsx")
    #     decoded_data = base64.b64decode(attachment.datas)
    #     wb = open_workbook(file_contents=decoded_data)
    #     sheet1 = wb.sheet_by_index(0)
    #     self.assertEqual(sheet1.cell_value(1, 0), "base.res_partner_2")
    #     self.assertEqual(sheet1.cell_value(1, 1), "Deco Addict")
    #     self.assertEqual(sheet1.cell_value(1, 2), "325 Elsie Drive")
    #     self.assertEqual(sheet1.cell_value(1, 3), "US")
    #     self.assertEqual(sheet1.cell_value(1, 4), "US")
    #
    # def test_export_with_record_wizard(self):
    #     self.ir_exports.generate_pattern()
    #     wiz = self.env["export.pattern.wizard"].with_context(
    #         active_ids=self.partners.ids, active_model=self.partners._name
    #     ).create({"model": self.partners._name, "ir_exports_id": self.ir_exports.id})
    #     job = self.job_counter()
    #     wiz.run()
    #     new_job = job.search_created()
    #     self.assertEquals(job.count_created(), 1)
    #     self.assertIn(
    #         "Generate export 'res.partner' with export pattern 'Partner list'",
    #         new_job.name,
    #     )
    #     self.assertEqual(new_job.model_name, "res.partner")

    def _helper_get_resulting_wb(self, export, records):
        export._export_with_record(records)
        attachment = self._get_attachment(export)
        self.assertEqual(attachment.name, export.name + ".xlsx")
        decoded_data = base64.b64decode(attachment.datas)
        return open_workbook(file_contents=decoded_data)

    def _helper_check_cell_values(self, sheet, expected_values):
        """ To allow for csv-like syntax in tests, just give a list
        of lists, with 1 list <=> 1 row """
        for itr_row, row in enumerate(expected_values, start=1):
            for itr_cell, expected_cell_value in enumerate(row):
                cell_value = sheet.cell_value(itr_row, itr_cell)
                self.assertEqual(cell_value, expected_cell_value)

    def _helper_check_headers(self, sheet, expected_headers):
        for itr_cell, expected_cell_value in enumerate(expected_headers):
            cell_value = sheet.cell_value(0, itr_cell)
            self.assertEqual(cell_value, expected_cell_value)

    def test_export_headers(self):
        wb = self._helper_get_resulting_wb(self.ir_exports, self.partners)
        sheet = wb.sheet_by_index(0)
        expected_headers = ["id", "name", "street", "country_id|code", "parent_id|country_id|code"],
        self._helper_check_cell_values(sheet, expected_headers)

    def test_export_cell_vals(self):
        wb = self._helper_get_resulting_wb(self.ir_exports, self.partners)
        sheet = wb.sheet_by_index(0)
        expected_values = [
            ["base.res_partner_1", "Wood Corner", "1164 Cambridge Drive", "US"],
            ["base.res_partner_2", "Deco Addict", "325 Elsie Drive", "US"],
            ["base.res_partner_3", "Gemini Furniture", "1128 Lunetta Street", "US"]
        ]
        self._helper_check_cell_values(sheet, expected_values)

    def test_export_m2m_headers(self):
        wb = self._helper_get_resulting_wb(self.ir_exports_m2m, self.users)
        sheet_base = wb.sheet_by_index(0)
        expected_headers_base = [
            ["id", "name", "company_ids|1|name"],
        ]
        self._helper_check_headers(sheet_base, expected_headers_base)
        sheet_tab_2 = wb.sheet_by_name("Company list")
        expected_headers_tab_2 = ["name"]
        self._helper_check_headers(sheet_tab_2, expected_headers_tab_2)

    def test_export_m2m_values(self):
        wb = self._helper_get_resulting_wb(self.ir_exports_m2m, self.users)
        sheet_base = wb.sheet_by_index(0)
        expected_values_base = [
            ["pattern_import_export.demo_user_1", "Wood Corner", "Company 1 (export demo)"],
            ["pattern_import_export.demo_user_2", "Wood Corner", "Company 1 (export demo)"],
            ["pattern_import_export.demo_user_3", "Deco Addict", "Company 1 (export demo)"]
        ]
        self._helper_check_cell_values(sheet_base, expected_values_base)
        sheet_tab_2 = wb.sheet_by_name("Company list")
        expected_values_tab_2 = [
            ["Company 1 (export demo)"],
            ["Company 1 (export demo)"],
            ["Company 1 (export demo)"],
        ]
        self._helper_check_cell_values(sheet_tab_2, expected_values_tab_2)

    def test_export_o2m_headers(self):
        wb = self._helper_get_resulting_wb(self.ir_exports_m2m, self.users)
        sheet = wb.sheet_by_index(0)
        expected_headers = [
            "id",
            "name",
            "user_ids|1|id",
            "user_ids|1|name",
            "user_ids|1|company_ids|1|name",
            "user_ids|2|id",
            "user_ids|2|name",
            "user_ids|2|company_ids|1|name",
            "user_ids|3|id",
            "user_ids|3|name",
            "user_ids|3|company_ids|1|name",
        ]
        self._helper_check_headers(sheet, expected_headers)

    def test_export_o2m_values(self):
        wb = self._helper_get_resulting_wb(self.ir_exports_m2m, self.users)
        sheet = wb.sheet_by_index(0)
        expected_values = [
            []
            "id",
            "name",
            "user_ids|1|id",
            "user_ids|1|name",
            "user_ids|1|company_ids|1|name",
            "user_ids|2|id",
            "user_ids|2|name",
            "user_ids|2|company_ids|1|name",
            "user_ids|3|id",
            "user_ids|3|name",
            "user_ids|3|company_ids|1|name",
        ]
        self._helper_check_cell_values(sheet, expected_values)