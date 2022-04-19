# 100
# exercise solution

import re

str="""arvindkicchakaranje@gmail.com
priyakarane@gmail.com
satoshipatil@gmail.com
Traceback (most recent call last):
  File "./prog.py", line 12, in <module>
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexing.py", line 1762, in __getitem__
    return self._getitem_tuple(key)
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexing.py", line 1289, in _getitem_tuple
    retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexing.py", line 1912, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexing.py", line 1796, in _get_slice_axis
    indexer = labels.slice_indexer(
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexes/base.py", line 4712, in slice_indexer
    start_slice, end_slice = self.slice_locs(start, end, step=step, kind=kind)
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexes/base.py", line 4925, in slice_locs
    start_slice = self.get_slice_bound(start, "left", kind)
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexes/base.py", line 4837, in get_slice_bound
    label = self._maybe_cast_slice_bound(label, side, kind)
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexes/base.py", line 4789, in _maybe_cast_slice_bound
    self._invalid_indexer("slice", label)
  File "/usr/local/lib/python3.8/dist-packages/pandas/core/indexes/base.py", line 3075, in _invalid_indexer
    raise TypeError(
TypeError: cannot do slice indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [0] of <class 'int'>"""

email=re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z.+%]+[.][a-zA-Z.0-9]+", str)
print(email)

