# Copyright (c) 2014 Rackspace Hosting
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Table

from oslo.utils import timeutils


def upgrade(engine):
    meta = MetaData()
    meta.bind = engine

    # Create new table partner
    table = Table('temp_instances', meta,
            Column('created_at', DateTime, default=timeutils.utcnow),
            Column('updated_at', DateTime, onupdate=timeutils.utcnow),
            Column('deleted_at', DateTime),
            Column('started_at', DateTime, nullable=False, default=timeutils.utcnow),
            Column('stopped_at', DateTime, nullable=False, default=timeutils.utcnow),
            Column('deleted', Integer, default=0, nullable=False),
            Column('id', Integer, primary_key=True, nullable=False, autoincrement=True),
            Column('host', String(10), nullable=False),
            Column('flavor', Integer, nullable=False),
            mysql_engine='InnoDB',
            mysql_charset='utf8'
    )
    table.create()


def downgrade(engine):
    meta = MetaData()
    meta.bind = engine

    table = Table('temp_instances', meta)
    table.drop(checkfirst=True)
