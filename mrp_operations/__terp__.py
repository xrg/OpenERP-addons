# -*- encoding: utf-8 -*-
{
    "name" : "Workcenter Production start end workflow",
    "version" : "1.0",
    "author" : "Tiny",
    "website" : "http://tinyerp.com/module_mrp.html",
    "category" : "Generic Modules/Production",
    "depends" : ["stock", "hr", "purchase", "product", "mrp"],
    "description": """
     This module adds state, date_start,date_stop in production order operation lines
     (in the "Workcenters" tab)
     State: draft, confirm, done, cancel
     When finnishing/confirming,cancelling production orders set all state lines to the according state
     Create menus:
         Production Management > All Operations
         Production Management > All Operations > Operations To Do (state="confirm")
     Which is a view on "Workcenters" lines in production order,
     editable tree

    Add buttons in the form view of production order under workcenter tab:
    * start (set state to confirm), set date_start
    * done (set state to done), set date_stop
    * set to draft (set state to draft)
    * cancel set state to cancel

    When the production order becomes "ready to produce", operations must
    become 'confirmed'. When the production order is done, all operations
    must become done.

    The field delay is the delay(stop date - start date).
    So that we can compare the theoric delay and real delay.

    """,
    "init_xml" : [],
    "demo_xml" : ["mrp_operation_data.xml"],
    "update_xml" : ["mrp_operations_workflow.xml","mrp_operations_view.xml","mrp_operations_report.xml"],
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
