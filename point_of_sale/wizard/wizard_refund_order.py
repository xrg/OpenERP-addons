# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2005-2006 TINY SPRL. (http://tiny.be) All Rights Reserved.
#
# $Id:
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################


#import time
#import netsvc
#from tools.misc import UpdateableStr
#import pooler
import wizard
import pooler


warning_form = '''<?xml version="1.0"?>
<form string="Refund ">
<separator string="Refund order :" colspan="4"/>
<newline/>
<field name="date_validity"/>
</form>
'''

warning_fields = {
    'date_validity': {'string': 'Validity Date', 'type': 'date'}
}


def _get_date(self, cr, uid, data, context):
    order_ref = pooler.get_pool(cr.dbname).get('pos.order')
    order = order_ref.browse(cr, uid, data['id'], context)
    return {'date_validity': order.date_validity}


def _refunding(self, cr, uid, data, context):
    order_ref = pooler.get_pool(cr.dbname).get('pos.order')
    clone_list = order_ref.refund(cr, uid, data['ids'], context)

    if data['form']['date_validity']:
        order_ref.write(cr, uid, clone_list, {
            'date_validity': data['form']['date_validity']
            })

    return {
        'domain': "[('id','in',["+','.join(map(str, clone_list))+"])]",
        'name': 'Refunded Orders',
        'view_type': 'form',
        'view_mode': 'tree,form',
        'res_model': 'pos.order',
        'view_id': False,
        #'context': "{'journal_id':%d}" % (form['journal_id'],),
        'type': 'ir.actions.act_window'
    }


class refund_order(wizard.interface):
    states = {
        'init': {
            'actions': [_get_date],
            'result': {
                'type': 'form',
                'arch': warning_form,
                'fields': warning_fields,
                'state': [('end', 'Cancel', 'gtk-no'), ('refund_n_quit', 'Ok', 'gtk-yes')]
            }
        },
        'refund_n_quit': {
            'actions': [],
            'result': {
                'type': 'action',
                'action': _refunding,
                'state': 'end'
            }
        },
    }

refund_order('pos.refund_order')
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
