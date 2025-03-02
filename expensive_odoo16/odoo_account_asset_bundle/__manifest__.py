# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Account Asset Management Bundle App',
    'version': '3.4.0',
    'category' : 'Accounting/Accounting',
    'price': 29.0,
    'license': 'Other proprietary',
    'depends': [
        'odoo_account_asset_extend_ce',
        'account_asset_disposal_ce',
        'material_purchase_requisitions',
        'odoo_asset_maintenance_ce',
        'odoo_asset_transfer_ce',
        'odoo_disposal_extend_ce',
        'odoo_asset_dashboard',
    ],
    'currency': 'EUR',
    'summary': """Account Asset Management Bundle App""",
    'description': """
Account Asset Disposal

This module enables the feature to dispose the asset. User can use two below methods to dispose any asset.
Sales Dispose
Asset Write-Off
This will allow user to dispose asset of company directly from Asset form. We have provide new tab under Asset form. 
You can see blog of our here on this: http://www.probuse.com/blog/erp-functional-27/post/asset-disposal-write-off-69 
**Note: This module only support Invoice sales of Asset not Cash sales.
asset close
asset dispose
asset disposal
account asset
account asset disposal
disposal process
process disposal

asset dashboard
account_asset
asset accounting
asset management
odoo asset
Asset Disposal
Dispose Assets
Account Asset Disposal,
Material Purchase Requisitions
    This module allowed Purchase requisition of employee.
Purchase_Requisition_Via_iProcurement
Purchase Requisitions
Purchase Requisition
iProcurement
Inter-Organization Shipping Network
Online Requisitions
Issue Enforcement
Inventory Replenishment Requisitions
Replenishment Requisitions
MRP Generated Requisitions
generated Requisitions
purchase Sales Orders
Complete Requisitions Status Visibility
Using purchase Requisitions
purchase requisitions
replenishment requisitions
employee Requisition
employee purchase Requisition
user Requisition
stock Requisition
inventory Requisition
warehouse Requisition
factory Requisition
department Requisition
manager Requisition
Submit requisition
Create purchase Orders
purchase Orders
product Requisition
item Requisition
material Requisition
product Requisitions
material purchase Requisition
material Requisition purchase
purchase material Requisition
product purchase Requisition
item Requisitions
material Requisitions
products Requisitions
purchase Requisition Process
Approving or Denying the purchase Requisition
Denying purchase Requisition​
construction managment
real estate management
construction app
Requisition
Requisitions
internal Requisitions
* INHERIT hr.department.form.view (form)
* INHERIT hr.employee.form.view (form)
* INHERIT stock.picking.form.view (form)
material.purchase.requisition search (search)
material.purchase.requisition.form.view (form)
material.purchase.requisition.view.tree (tree)
purchase_requisition (qweb)
Main Features:
allow your employees to Create Purchase Requisition.
Employees can request multiple material/items on single purchase Requisition request.
Approval of Department Head.
Approval of Purchase Requisition Head.
Email notifications to Department Manager, Requisition Manager for approval.
- Request for Purchase Requisition will go to stock/warehouse as internal picking / internal order and purchase order.
- Warehouse can dispatch material to employee location and if material not present then procurment will created by Odoo standard.
- Purchase Requisition user can decide whether product requested by employee will come from stock/warehouse directly or it needs to be purchase from vendor. So we have field on requisition lines where responsible can select Requisition action: 1. Purchase Order 2. Internal Picking. If option 1 is selected then system will create internal order / internal picking request and if option 2 is selected system will create multiple purchase order / RFQ to vendors selected on lines.
- For more details please see Video on live preview or ask us by email...

 Odoo Account Asset Extend
 
 Odoo Asset Maintenance
 
 Odoo Asset Transfer
 
 Odoo Disposal Extend
 
    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'http://www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/image.jpg'],
#    'live_test_url': 'https://youtu.be/gkU-pnHNUGc',

    'data':[
          
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
