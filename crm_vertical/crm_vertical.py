# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2004-2008 TINY SPRL. (http://tiny.be) All Rights Reserved.
#
# $Id$
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

import time
import tools
from osv import fields,osv,orm
import os
import mx.DateTime
import base64

# here need to implement inheritance on osv_memory object. after that, it will work well.
class crm_menu_config_wizard(osv.osv_memory):
    _inherit='crm.menu.config_wizard'
    def action_create(self, cr, uid, ids, *args):
        res=super(crm_menu_config_wizard, self).action_create(cr, uid, ids, *args)
        for res in self.read(cr,uid,ids):
            res.__delitem__('id')
            for section in res :
                if res[section]:
                    file_name = 'crm_'+section+'_vertical_view.xml'
                    try:
                        tools.convert_xml_import(cr, 'crm_configuration', tools.file_open(os.path.join('crm_vertical',file_name )),  {}, 'init', *args)
                    except Exception, e:
                        raise osv.except_osv('Error !', e)
        return res

crm_menu_config_wizard()