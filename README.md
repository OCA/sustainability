
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/sustainability-suite/sustainability-odoo/actions/workflows/pre-commit.yml/badge.svg?branch=16.0)](https://github.com/sustainability-suite/sustainability-odoo/actions/workflows/pre-commit.yml?query=branch%3A16.0)
[![Build Status](https://github.com/sustainability-suite/sustainability-odoo/actions/workflows/test.yml/badge.svg?branch=16.0)](https://github.com/sustainability-suite/sustainability-odoo/actions/workflows/test.yml?query=branch%3A16.0)
[![codecov](https://codecov.io/gh/sustainability-suite/sustainability-odoo/branch/16.0/graph/badge.svg)](https://codecov.io/gh/sustainability-suite/sustainability-odoo)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

# Sustainability

The Odoo Sustainability Module is designed to seamlessly integrate sustainability management and the carbon CO2 emissions footprint computation into your Odoo ERP system.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[sustainability](sustainability/) | 16.0.2.2.0 | <a href='https://github.com/jguenat'><img src='https://github.com/jguenat.png' width='32' height='32' style='border-radius:50%;' alt='jguenat'/></a> <a href='https://github.com/bonnetadam'><img src='https://github.com/bonnetadam.png' width='32' height='32' style='border-radius:50%;' alt='bonnetadam'/></a> <a href='https://github.com/jacopobacci'><img src='https://github.com/jacopobacci.png' width='32' height='32' style='border-radius:50%;' alt='jacopobacci'/></a> | Base module to track CO2 equivalent in accounting, Sustainability, GHG Protocol, CSRD Directive, BEGES, ADEME, ISO format, Action Plan, Emission Factors, carbon CO2 footprint computation, Analytical accounting, Decarbonization
[sustainability_account_asset_management](sustainability_account_asset_management/) | 16.0.1.0.0 | <a href='https://github.com/jguenat'><img src='https://github.com/jguenat.png' width='32' height='32' style='border-radius:50%;' alt='jguenat'/></a> | Glue module to make sustainability module compatible with assets management from OCA
[sustainability_employee_commuting](sustainability_employee_commuting/) | 16.0.1.0.0 | <a href='https://github.com/bonnetadam'><img src='https://github.com/bonnetadam.png' width='32' height='32' style='border-radius:50%;' alt='bonnetadam'/></a> <a href='https://github.com/jacopobacci'><img src='https://github.com/jacopobacci.png' width='32' height='32' style='border-radius:50%;' alt='jacopobacci'/></a> | Module for employee commuting co2
[sustainability_hr_expense_report](sustainability_hr_expense_report/) | 16.0.0.2.0 | <a href='https://github.com/bonnetadam'><img src='https://github.com/bonnetadam.png' width='32' height='32' style='border-radius:50%;' alt='bonnetadam'/></a> | Provide CO2 accounting data for expense reports
[sustainability_mis_builder](sustainability_mis_builder/) | 16.0.0.1.0 | <a href='https://github.com/jguenat'><img src='https://github.com/jguenat.png' width='32' height='32' style='border-radius:50%;' alt='jguenat'/></a> | Provide CO2 accounting lines data for MIS builder reports
[sustainability_purchase](sustainability_purchase/) | 16.0.2.0.1 | <a href='https://github.com/jguenat'><img src='https://github.com/jguenat.png' width='32' height='32' style='border-radius:50%;' alt='jguenat'/></a> <a href='https://github.com/bonnetadam'><img src='https://github.com/bonnetadam.png' width='32' height='32' style='border-radius:50%;' alt='bonnetadam'/></a> <a href='https://github.com/jacopobacci'><img src='https://github.com/jacopobacci.png' width='32' height='32' style='border-radius:50%;' alt='jacopobacci'/></a> | Glue module for sustainability & purchase modules
[sustainability_purchase_stock](sustainability_purchase_stock/) | 16.0.1.1.0 | <a href='https://github.com/jacopobacci'><img src='https://github.com/jacopobacci.png' width='32' height='32' style='border-radius:50%;' alt='jacopobacci'/></a> | Sustainability Purchase Stock
[sustainability_stock](sustainability_stock/) | 16.0.2.0.0 | <a href='https://github.com/jacopobacci'><img src='https://github.com/jacopobacci.png' width='32' height='32' style='border-radius:50%;' alt='jacopobacci'/></a> | Sustainability Inventory

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to MCO2
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
<!-- /!\ Non OCA Context : Set here the full description of your organization. -->
