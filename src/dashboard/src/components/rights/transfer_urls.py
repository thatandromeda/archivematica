# This file is part of Archivematica.
#
# Copyright 2010-2012 Artefactual Systems Inc. <http://artefactual.com>
#
# Archivematica is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Archivematica is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Archivematica.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import patterns

urlpatterns = patterns('components.rights.views',
    (r'^$', 'transfer_rights_list'),
    (r'add/$', 'transfer_rights_edit'),
    (r'delete/(?P<id>\d+)/$', 'transfer_rights_delete'),
    (r'grants/(?P<id>\d+)/$', 'transfer_rights_grants_edit'),
    (r'(?P<id>\d+)/$', 'transfer_rights_edit')
)
