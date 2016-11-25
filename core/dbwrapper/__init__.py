#!/usr/bin/env python
#coding=utf-8
#by nagexiucai

from core.base import Base
from core.log import Log
from core.fs import FS
import sqlite3

class MiniDBMS(Base):
    ASSIGNMENT = '%s=%s'
    CREATE = 'create table %s (%s);'
    INSERT = 'insert into %s values (%s);'
    PLACEHOLDER = '?'
    SEPARATOR = ' '
    SUBSEPARAOR = ','
    SELECT = 'select %s from %s;'
    DECLARATION = '%s %s'
    UPDATE = 'update %s set %s;'
    @classmethod
    def sql_structure_generator(cls, fields, types):
        structures = [MiniDBMS.DECLARATION % (f, t) for f, t in zip(fields, types)]
        structure = MiniDBMS.SUBSEPARAOR.join(structures)
        Log._(structure, Log.VORBOSE)
        return structure
    @classmethod
    def sql_assignment_generator(cls, fields, data): #todo: more perfecter(correct value format according to filed type of each field)
        assignments = [MiniDBMS.ASSIGNMENT % (f, d) for f, d in zip(fields, data)]
        assignment = MiniDBMS.SEPARATOR.join(assignments)
        Log._(assignment, Log.VORBOSE)
        return assignment
    @classmethod
    def sql_placeholder_generator(cls, count):
        placeholder = MiniDBMS.SUBSEPARAOR.join([MiniDBMS.PLACEHOLDER]*count)
        Log._(placeholder, Log.VORBOSE)
        return placeholder
    def __init__(self, *args, **kws):
        super(MiniDBMS, self).__init__(*args, **kws)
        self.__driver = sqlite3.connect(FS.join_path(FS.inner_root(), 'db'), check_same_thread=False) #todo: ephemeral means
        self.__cursor = self.__driver.cursor()
        self.__log = None #todo: operating logs
    def create(self, table, fields, types):
        sql = MiniDBMS.CREATE % (table, MiniDBMS.sql_structure_generator(fields, types))
        Log._(sql, Log.ORDINARY)
        state = self._execute(sql)
        self._commit()
        return state
    def update(self, table, fields, data):
        sql = MiniDBMS.UPDATE % (table, MiniDBMS.sql_assignment_generator(fields, data))
        Log._(sql, Log.ORDINARY)
        state = self._execute(sql)
        self._commit()
        return state
    def insert(self, table, data):
        sql = MiniDBMS.INSERT % (table, MiniDBMS.sql_placeholder_generator(max([len(d) for d in data])))
        Log._(sql, Log.ORDINARY)
        state = self._batch_execute(sql, data)
        self._commit()
        return state
    def destroy(self, *args, **kws):
        self.__cursor.close()
        self.__driver.close()
    def show(self, table): #todo: so crude
        self._execute(MiniDBMS.SELECT % ('*', table))
        data = self.__cursor.fetchall()
        Log.beauty(data)
        return data
    def _execute(self, sql):
        state = True
        try:
            Log._(sql, Log.VORBOSE)
            self.__cursor.execute(sql)
        except: #todo: refined
            state = False
            Log._('crash', Log.SERIOUS)
            Log.exception()
        finally:
            pass
        return state
    def _batch_execute(self, sql, data):
        return self.__cursor.executemany(sql, data)
    def _commit(self):
        self.__driver.commit()

if __name__ == '__main__':
    Log.LEVEL = Log.ORDINARY
    table = 'person'
    fields = ('name', 'age', 'address', 'at')
    types = ('TEXT', 'INT', 'TEXT', 'TIMESTAMP') #TIMESTAMP FORMAT IS 'YYYY-MM-DD HH:MM:SS'
    data = ('who', 'how-old', 'where', '2016-11-03 10:52:30')
    MiniDBMS.sql_structure_generator(fields, types)
    MiniDBMS.sql_assignment_generator(fields, data)
    mdbms = MiniDBMS()
    mdbms.create(table, fields, types)
    mdbms.insert(table, [data, data, data])
    mdbms.show(table)
    mdbms.destroy()
