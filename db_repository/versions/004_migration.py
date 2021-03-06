from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
item = Table('item', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('item_name', String(length=140)),
    Column('aisle_id', Integer),
)

aisle = Table('aisle', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('items', VARCHAR(length=140)),
    Column('list_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['item'].create()
    pre_meta.tables['aisle'].columns['items'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['item'].drop()
    pre_meta.tables['aisle'].columns['items'].create()
