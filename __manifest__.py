{
    'name': 'LBX-MS-20231009',
    'author':' M.SHAHIDH',
    'sequence': 1,
    'summary': 'New interface for ITL Purches order ',
    'category': 'Administration/Automation',
    'depends':[
        'mail',
        'product',
    ],
    'data': [
        'views/menu.xml',
        'views/AdditionalInstructions.xml',
        'views/caution.xml',
        'views/ChildWarnings.xml',
        'views/Copyrights.xml',
        'views/Customers.xml',
        'views/Departments.xml',
        'views/GetChains.xml',
        'views/GetITLOffices.xml',
        'views/PantoneRefs.xml',
        'views/ProductBenifits.xml',
        'views/ProductDescriptions.xml',
        'views/Products.xml',
        'views/Seasons.xml',
        'views/Sizes.xml',
        'views/TextColours.xml',
        'views/TogRatings.xml',
        'views/care_instruction.xml',
        'views/care_instruction_set.xml',
        'views/dashboard.xml',
        'views/kanban._test.xml',
        'views/components.xml',
        'views/countries_of_origin.xml',
        'views/fibres.xml',
        'views/brands.xml',
        'views/get_vs_stores_options.xml',
        'views/multi_part_sets.xml',
        'views/washsymbols.xml',
        'views/transaction.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        # 'data/brand_data.xml',
        'views/test_transaction.xml',
        # 'views/materialmap.xml',
        'views/sizeid.xml',
        'views/referencemaster.xml',
        'views/typeofmaterial.xml',
        'views/getpo.xml',
        # 'views/menu_transaction.xml', 
        'views/get_po_test.xml',
        'views/mas_integration_get_po.xml',
        'views/mas_integration_get_vpo.xml',

        'views/brandix_integration_get_po.xml',
        'views/brandix_integration_get_vpo.xml',

        'views/sub_chain.xml',
        'views/sub_itl_code.xml',
        'views/sub_product.xml',
        'views/tree_check.xml',
        'views/color_code_master.xml',
        
        # 2023-12-09
        'views/sub_fiber.xml',
        'views/set_fiber.xml',
        'views/sub_component.xml',
        'views/sub_care_instruction_code.xml',
        'views/size_mapping_01.xml',
        'views/size_range.xml',
        'views/coo_master.xml',

        # 2023-12-27
        'views/size_master.xml',
        'views/season_master.xml',
        'views/reference_master.xml',
        'views/care_instruction_code.xml',

        'views/collection_master.xml',
        'views/silhouette_master.xml',
        
    ],
    'assets': {
        'web.assets_backend': [
            # ('origen_theme_lbx/static/css/style.css'),
            ('ITL_LBX_MS/static/css/style_backend.css'),#for app screen nave bar
            # ('origen_theme_lbx/static/less/styles_backend.less'),
        ],
    },
    'installable': True,
    'application': True,
}