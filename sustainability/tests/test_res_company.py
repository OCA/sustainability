from odoo.tests import TransactionCase


class TestResCompanyFallbackFactor(TransactionCase):
    def _archive_fallback_factors(self, name):
        # The demo data ships a factor with this name. create() then reuses it and
        # never reaches the branch that builds a new factor, which hid the bug in CI.
        self.env["carbon.factor"].search([("name", "=", name)]).active = False

    def test_create_company_without_currency(self):
        # Used to raise UnboundLocalError: 'currency' was only bound when
        # currency_id was in the create values.
        self._archive_fallback_factors("Global Emission Factor Fallback")
        company = self.env["res.company"].create({"name": "Company without currency"})
        factor = company.carbon_in_factor_id
        self.assertEqual(factor.name, "Global Emission Factor Fallback")
        self.assertTrue(factor.active)
        self.assertFalse(factor.value_ids.carbon_monetary_currency_id)
        self.assertEqual(company.carbon_out_factor_id, factor)

    def test_create_company_with_currency(self):
        currency = self.env.ref("base.USD")
        name = f"Global Emission Factor Fallback {currency.name}"
        self._archive_fallback_factors(name)
        company = self.env["res.company"].create(
            {"name": "Company with currency", "currency_id": currency.id}
        )
        factor = company.carbon_in_factor_id
        self.assertEqual(factor.name, name)
        self.assertEqual(factor.value_ids.carbon_monetary_currency_id, currency)
