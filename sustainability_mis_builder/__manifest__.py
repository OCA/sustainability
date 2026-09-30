# © 2023 Open Net Sarl
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sustainability MIS Builder",
    "summary": "Provide CO2e accounting lines data for MIS builder reports",
    "version": "18.0.1.1.0",
    "author": "MCO2, Open Net Sàrl, Odoo Community Association (OCA)",
    "maintainers": ["jguenat"],
    "development_status": "Production/Stable",
    "category": "Accounting/Sustainability",
    "website": "https://github.com/OCA/sustainability",
    "depends": ["mis_builder", "sustainability"],
    "data": [
        "views/mis_carbon_account_move_line.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "license": "AGPL-3",
}
