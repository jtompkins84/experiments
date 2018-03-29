# Author:       Joseph Tompkins
# Date:         03/29/2018
# Description:  A very simple hash table implementation which uses a slightly modified SDBM hash function.
#               This function was chosen for its speed, simplicity, low number of collisions,
#               and decent hash distribution.
#               This script is a learning exercise, and not meant for actual use.


__all__ = ['hashcode', 'hashtable']


from collections import Iterable


def hashcode(key):
    """
    Computes a hash code for a given key value.
    Uses the SDBM hash function.
    """
    hash = 0
    key = str(key).encode('utf-8')
    _bytes = bytearray(bytes(key))
    for byte in _bytes:
        byte = byte << 8
        hash = byte + (hash << 6) + (hash << 16) - hash
    return hash

class hashtable:
    def __init__(self, table_sz=4096):
        self.__table_sz = table_sz
        self.__table = [None] * table_sz

    def set(self, key, value):
        """
        Set the value of the item corresponding with the given key.\n
        If the item does not yet exist, a new key/value pair will be created.
        """
        hash = hashcode(key)
        index = hash % self.__table_sz
        if self.__table[index] is None:
            self.__table[index] = list()
        if key not in [item[0] for item in self.__table[index]]:
            self.__table[index].append((key, value))
        else:
            self.__table[index] = value

    def get(self, key):
        """Get the value of the item"""
        hash = hashcode(key)
        index = hash % self.__table_sz
        for item in self.__table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError

    def remove(self, key):
        """Removes the item with the item with the given key."""
        hash = hashcode(key)
        index = hash % self.__table_sz
        for item in self.__table[index]:
            if item[0] == hash:
                self.__table.pop(index)
