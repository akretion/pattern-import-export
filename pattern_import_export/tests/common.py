# Copyright 2020 Akretion France (http://www.akretion.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import base64
from contextlib import contextmanager

from odoo.tests import new_test_user

from odoo.addons.queue_job.tests.common import JobMixin

from ..models.ir_exports import COLUMN_X2M_SEPARATOR


class ExportPatternCommon(JobMixin):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.Exports = cls.env["ir.exports"]
        cls.Company = cls.env["res.company"]
        cls.Attachment = cls.env["ir.attachment"]
        cls.ExportPatternWizard = cls.env["export.pattern.wizard"]
        cls.Users = cls.env["res.users"]
        cls.Partner = cls.env["res.partner"]
        cls.PartnerIndustry = cls.env["res.partner.industry"]
        cls.PartnerCategory = cls.env["res.partner.category"]
        cls.partner_1 = cls.env.ref("base.res_partner_1")
        cls.partner_2 = cls.env.ref("base.res_partner_2")
        cls.partner_3 = cls.env.ref("base.res_partner_3")
        cls.country_be = cls.env.ref("base.be")
        cls.country_us = cls.env.ref("base.us")
        cls.group_manager = cls.env.ref("base.group_erp_manager")
        cls.group_no_one = cls.env.ref("base.group_no_one")
        cls.group_job = cls.env.ref("queue_job.group_queue_job_manager")
        cls.field_user_name = cls.env.ref("base.field_res_users__name")
        cls.field_user_id = cls.env.ref("base.field_res_users__id")
        cls.field_user_login = cls.env.ref("base.field_res_users__login")
        cls.industry1 = cls.env.ref("base.res_partner_industry_A")
        cls.industry2 = cls.env.ref("base.res_partner_industry_B")
        cls.industries = cls.industry1 | cls.industry2
        cls.partner_cat1 = cls.env.ref("base.res_partner_category_3")
        cls.partner_cat2 = cls.env.ref("base.res_partner_category_11")
        cls.partner_catgs = cls.partner_cat1 | cls.partner_cat2
        cls.user1 = cls.env.ref("pattern_import_export.demo_user_1")
        cls.user2 = cls.env.ref("pattern_import_export.demo_user_2")
        cls.user3 = cls.env.ref("pattern_import_export.demo_user_3")
        cls.users = cls.user1 | cls.user2 | cls.user3
        cls.partners = cls.partner_1 | cls.partner_2 | cls.partner_3
        cls.company1 = cls.env.ref("base.main_company")
        cls.company2 = cls.env.ref("pattern_import_export.demo_company_1")
        cls.company3 = cls.env.ref("pattern_import_export.demo_company_2")
        cls.companies = cls.company1 | cls.company2 | cls.company3
        cls.separator = COLUMN_X2M_SEPARATOR
        cls.select_tab = cls.env.ref("pattern_import_export.demo_export_tab_1")
        cls.select_tab_company = cls.env.ref("pattern_import_export.demo_export_tab_2")
        cls.ir_exports = cls.env.ref("pattern_import_export.demo_export")
        cls.ir_exports_m2m = cls.env.ref("pattern_import_export.demo_export_m2m")
        cls.ir_exports_o2m = cls.env.ref("pattern_import_export.demo_export_o2m")
        cls.empty_attachment = cls.env.ref(
            "pattern_import_export.demo_empty_attachment"
        )

    def _get_attachment(self, record):
        """
        Get the first attachment from given recordset
        @param record: recordset
        @return: ir.attachment
        """
        return self.Attachment.search(
            [("res_model", "=", record._name), ("res_id", "=", record.id)], limit=1
        )

    @contextmanager
    def _mock_read_import_data(self, main_data):
        """
        Mock the _read_import_data from Exports to return directly
        received datafile
        @return:
        """

        def _read_import_data(self, datafile):
            return main_data

        self.Exports._patch_method("_read_import_data", _read_import_data)
        yield
        self.Exports._revert_method("_read_import_data")
