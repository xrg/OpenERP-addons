# -*- encoding: utf-8 -*-
from osv import fields,osv

AVAILABLE_STATES = [
    ('draft','Draft'),
    ('open','Open'),
    ('cancel', 'Canceled'),
    ('done', 'Closed'),
    ('pending','Pending')
]
class report_crm_case_section_categ2(osv.osv):
    _name = "report.crm.case.section.categ2"
    _description = "Cases by section and category2"
    _auto = False
    _columns = {
        'name': fields.date('Month', readonly=True),
        'user_id':fields.many2one('res.users', 'User', readonly=True),
        'section_id':fields.many2one('crm.case.section', 'Section', readonly=True),
        'category2_id':fields.many2one('crm.case.category2', 'Type', readonly=True),
        'stage_id':fields.many2one('crm.case.stage', 'Stage', readonly=True),
        'nbr': fields.integer('# of Cases', readonly=True),
        'state': fields.selection(AVAILABLE_STATES, 'State', size=16, readonly=True),        
        'delay_close': fields.char('Delay Close', size=20, readonly=True),
                }
    _order = 'category2_id, section_id'
    
    def init(self, cr):
        cr.execute("""
              create or replace view report_crm_case_section_categ2 as (
                select
                    min(c.id) as id,
                    substring(c.create_date for 7)||'-01' as name,
                    c.user_id,
                    c.state,
                    c.category2_id,
                    c.stage_id,
                    c.section_id,
                    count(*) as nbr,
                    to_char(avg(date_closed-c.create_date), 'DD"d" HH24:MI:SS') as delay_close
                from
                    crm_case c
                where c.category2_id is not null
                group by substring(c.create_date for 7), c.user_id, c.state, c.stage_id, c.category2_id, c.section_id)""")

report_crm_case_section_categ2()

class report_crm_case_section_stage(osv.osv):
    _name = "report.crm.case.section.stage"
    _description = "Cases by section and stage"
    _auto = False
    _columns = {
        'name': fields.date('Month', readonly=True),
        'user_id':fields.many2one('res.users', 'User', readonly=True),
        'section_id':fields.many2one('crm.case.section', 'Section', readonly=True),
        'categ_id':fields.many2one('crm.case.categ', 'Category', readonly=True),
        'stage_id':fields.many2one('crm.case.stage', 'Stage', readonly=True),
        'nbr': fields.integer('# of Cases', readonly=True),
        'state': fields.selection(AVAILABLE_STATES, 'State', size=16, readonly=True),        
        'delay_close': fields.char('Delay Close', size=20, readonly=True),
                }
    _order = 'stage_id, section_id'
    
    def init(self, cr):
        cr.execute("""
              create or replace view report_crm_case_section_stage as (
                select
                    min(c.id) as id,
                    substring(c.create_date for 7)||'-01' as name,
                    c.user_id,
                    c.state,
                    c.stage_id,
                    c.section_id,
                    count(*) as nbr,
                    to_char(avg(date_closed-c.create_date), 'DD"d" HH24:MI:SS') as delay_close
                from
                    crm_case c
                where c.stage_id is not null
                group by substring(c.create_date for 7), c.user_id, c.state, c.stage_id, c.section_id)""")

report_crm_case_section_stage()

class report_crm_case_section_categ_stage(osv.osv):
    _name = "report.crm.case.section.categ.stage"
    _description = "Cases by section, Category and stage"
    _auto = False
    _columns = {
        'name': fields.date('Month', readonly=True),
        'user_id':fields.many2one('res.users', 'User', readonly=True),
        'categ_id':fields.many2one('crm.case.categ', 'Category', readonly=True),
        'section_id':fields.many2one('crm.case.section', 'Section', readonly=True),
        'stage_id':fields.many2one('crm.case.stage', 'Stage', readonly=True),
        'nbr': fields.integer('# of Cases', readonly=True),
        'state': fields.selection(AVAILABLE_STATES, 'State', size=16, readonly=True),        
        'delay_close': fields.char('Delay Close', size=20, readonly=True),
                }
    _order = 'stage_id, section_id, categ_id'
    
    def init(self, cr):
        cr.execute("""
              create or replace view report_crm_case_section_categ_stage as (
                select
                    min(c.id) as id,
                    substring(c.create_date for 7)||'-01' as name,
                    c.user_id,
                    c.categ_id,
                    c.state,
                    c.stage_id,
                    c.section_id,
                    count(*) as nbr,
                    to_char(avg(date_closed-c.create_date), 'DD"d" HH24:MI:SS') as delay_close
                from
                    crm_case c
                where c.categ_id is not null AND c.stage_id is not null
                group by substring(c.create_date for 7), c.user_id, c.categ_id, c.state, c.stage_id, c.section_id)""")

report_crm_case_section_categ_stage()

class report_crm_case_section_categ_categ2(osv.osv):
    _name = "report.crm.case.section.categ.categ2"
    _description = "Cases by section, Category and Category2"
    _auto = False
    _columns = {
        'name': fields.date('Month', readonly=True),
        'user_id':fields.many2one('res.users', 'User', readonly=True),
        'categ_id':fields.many2one('crm.case.categ', 'Category', readonly=True),
        'category2_id':fields.many2one('crm.case.category2', 'Type', readonly=True),
        'section_id':fields.many2one('crm.case.section', 'Section', readonly=True),
        'stage_id':fields.many2one('crm.case.stage', 'Stage', readonly=True),
        'nbr': fields.integer('# of Cases', readonly=True),
        'state': fields.selection(AVAILABLE_STATES, 'State', size=16, readonly=True),        
        'delay_close': fields.char('Delay Close', size=20, readonly=True),
                }
    _order = 'section_id, categ_id, category2_id'
    
    def init(self, cr):
        cr.execute("""
              create or replace view report_crm_case_section_categ_categ2 as (
                select
                    min(c.id) as id,
                    substring(c.create_date for 7)||'-01' as name,
                    c.user_id,
                    c.categ_id,
                    c.category2_id,
                    c.state,
                    c.stage_id,
                    c.section_id,
                    count(*) as nbr,
                    to_char(avg(date_closed-c.create_date), 'DD"d" HH24:MI:SS') as delay_close
                from
                    crm_case c
                where c.categ_id is not null AND c.category2_id is not null
                group by substring(c.create_date for 7), c.user_id, c.categ_id, c.category2_id, c.state, c.stage_id, c.section_id)""")

report_crm_case_section_categ_categ2()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
