{
        "name" : "Luxembourg - Plan Comptable Minimum Normalise",
        "version" : "1.0",
        "author" : "Tiny",
        "website" : "http://openerp.com",
        "category" : "Localisation/Account Charts",
        "description": """ 
This module install:

    *the KLUWER Chart of Accounts,
    *the Tax Code Chart for Luxembourg
    *the main taxes used in Luxembourg""",
        "depends" : ["account","account_report","base_vat","base_iban"],
        "init_xml" : [ ],
        "demo_xml" : [ "account.report.report.csv" ],
        "update_xml" : [
            "l10n_lu_data.xml",
            "l10n_lu_wizard.xml",
            "l10n_lu_report.xml",
        ],
        "installable": True
} 