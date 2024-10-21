# This file is part of Buildbot.  Buildbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Buildbot Team Members

from __future__ import annotations

from buildbot.test.fakedb.row import Row


class Step(Row):
    table = "steps"

    id_column = 'id'
    foreignKeys = ('buildid',)
    required_columns = ('buildid',)

    def __init__(
        self,
        id=None,
        number=29,
        name='step29',
        buildid=None,
        started_at=1304262222,
        locks_acquired_at=None,
        complete_at=None,
        state_string='',
        results=None,
        urls_json='[]',
        hidden=0,
    ):
        super().__init__(
            id=id,
            number=number,
            name=name,
            buildid=buildid,
            started_at=started_at,
            locks_acquired_at=locks_acquired_at,
            complete_at=complete_at,
            state_string=state_string,
            results=results,
            urls_json=urls_json,
            hidden=hidden,
        )
