#!/usr/bin/env python


class GetId():
    def __init__(self, start_value = 1):
        self._start_value = start_value

    def get_id(self):
        value = self._start_value
        self._start_value += 1
        return value

g = GetId(100)

print(GetId)
print(g)
print(g.get_id())
print(g.get_id())
print(g.get_id())
print(GetId.get_id(g))


