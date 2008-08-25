# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2004-2006 TINY SPRL. (http://tiny.be) All Rights Reserved.
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

import pooler
import time
from report import report_sxw

class auction_objects(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        print "int the report objects"
        super(auction_objects, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'time': time,
            #'lines': self.lines
            #'get_data' : self.get_data
        })

#   def lines(self, auction_id):
#        print " in the lines fuction"
#        print "value of  auction_id",auction_id.id,auction_id.name........................
#
#        cr.execute('select ad.name from auction_dates ad, a1uction_lots al where ad.id=al.%d group by ad.name',(auction_id))
#        print "value of query",cr.fetchone()
#        return self.cr.fetchone()[0]
#   def get_data(self, auction_id):
#       res = self.pool.get('auction.bid.lines').read(self.cr,self.uid,[lot_id])
#       print res;
#       print "=================================================="
#       return True



report_sxw.report_sxw('report.auction.objects', 'auction.lots', 'addons/auction/report/auction_objects.rml', parser=auction_objects)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
