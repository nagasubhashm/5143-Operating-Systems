## Listing

Example output:

```
-rwxr-xr-x@ 1 griffin  staff     0B Feb  5 18:17 __init__.py
-rw-r--r--@ 1 griffin  staff   189B Feb  5 18:17 __init__.pyc
drwxr-xr-x@ 4 griffin  staff   128B Feb  5 18:17 __pycache__/
-rwxr-xr-x@ 1 griffin  staff   1.2K Feb  5 18:17 cat.py
-rw-r--r--@ 1 griffin  staff   1.6K Feb  5 18:17 cat.pyc
-rwxr-xr-x@ 1 griffin  staff   1.0K Feb  5 18:17 commands.py
-rw-r--r--@ 1 griffin  staff   1.6K Feb  5 18:17 commands.pyc
-rw-r--r--@ 1 griffin  staff    46B Feb  5 18:17 exit.py
-rw-r--r--@ 1 griffin  staff   432B Feb  5 18:17 exit.pyc
-rw-r--r--@ 1 griffin  staff   837B Feb  5 18:17 getch.py
-rw-r--r--@ 1 griffin  staff   2.7K Feb  5 18:17 getch.pyc
-rw-r--r--@ 1 griffin  staff   2.3K Feb  5 18:17 grep.py
-rw-r--r--@ 1 griffin  staff   3.0K Feb  5 18:17 grep.pyc
-rw-r--r--@ 1 griffin  staff   482B Feb  5 18:17 history.py
-rw-r--r--@ 1 griffin  staff   915B Feb  5 18:17 history.pyc
-rwxr-xr-x@ 1 griffin  staff   2.4K Feb 13 11:38 ls.py
-rw-r--r--@ 1 griffin  staff   1.2K Feb  5 18:17 ls.pyc
-rwxr-xr-x@ 1 griffin  staff   104B Feb  5 18:17 pwd.py
-rw-r--r--@ 1 griffin  staff   475B Feb  5 18:17 pwd.pyc
-rw-r--r--@ 1 griffin  staff    36B Feb  5 18:17 test.py
-rw-r--r--@ 1 griffin  staff   369B Feb  5 18:17 test.pyc
```

```python
import os
info = os.lstat(somefileordir)
# info: (st_mode=33188, st_ino=5254022, st_dev=16777220, st_nlink=1, st_uid=503, st_gid=20, st_size=50695, st_atime=1534972368, st_mtime=1523569466, st_ctime=1534972368)
```

#### Column 1: Permissions `st_mode`

The first character in the permissions column can portray a few different attributes about the item. I only want you to determine if it is a: files, directory, or link.

```python
isLink = os.path.islink(fileordirname)
isDir = os.path.isdir(fileordirname)

if not isLink and not isDir:
    isFile = True
```
(st_mode=33188, st_ino=5254022, st_dev=16777220, st_nlink=1, st_uid=503, st_gid=20, st_size=50695, st_atime=1534972368, st_mtime=1523569466, st_ctime=1534972368)
      ^
      |
```

To grab the numeric permissions:

```
octalPerms = oct(info.st_mode)[-3:]
print(octalPerms)
```

prints (for example)

```
644
```

Turning this into `-rw-r--r--` is trivial.



```python
permission ={
  '0':('---'),
  '1':('--x'),
  '2':('-w-'),
  '3':('-wx'),
  '4':('r--'),
  '5':('r-x'),
  '6':('rw-'),
  '7':('rwx')
}
print(permission(6))
```
prints: `rw-`
  
#### Column 2: Links `st_nlink`
```
(st_mode=33188, st_ino=5254022, st_dev=16777220, st_nlink=1, st_uid=503, st_gid=20, st_size=50695, st_atime=1534972368, st_mtime=1523569466, st_ctime=1534972368)
                                                     ^
      
```



```
info.st_nlink
```

Gives a `1` in this case.

#### Column 3: Owner `st_uid`
```
(st_mode=33188, st_ino=5254022, st_dev=16777220, st_nlink=1, st_uid=503, st_gid=20, st_size=50695, st_atime=1534972368, st_mtime=1523569466, st_ctime=1534972368)
                                                                 ^

```
```python
import os
from pwd import getpwuid

getpwuid(os.stat(filename).st_uid).pw_name,
```

#### Column 4: Group `st_gid`
```
(st_mode=33188, st_ino=5254022, st_dev=16777220, st_nlink=1, st_uid=503, st_gid=20, st_size=50695, st_atime=1534972368, st_mtime=1523569466, st_ctime=1534972368)
                                                                             ^
      
```
```python
import os
from grp import getgrgid

getgrgid(os.stat(filename).st_gid).gr_name
```

#### Column 5: Size `st_size`
```
(st_mode=33188, st_ino=5254022, st_dev=16777220, st_nlink=1, st_uid=503, st_gid=20, st_size=50695, st_atime=1534972368, st_mtime=1523569466, st_ctime=1534972368)
                                                                                           ^
      
```
Trivial to convert size in bytes to human readable.

#### Column 6: Date `mtime`

```
(... , st_size=50695, st_atime=1534972368, st_mtime=1523569466, st_ctime=1534972368)
                                                  ^
```

- `mtime` , or modification time, is when the file was last modified. When you change the contents of a file, its mtime changes. 
- `ctime` , or change time, is when the file's property changes. ... 
- `atime` , or access time, is updated when the file's contents are read by an application or a command such as grep or cat


```
# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
from datetime import datetime
ts = int("1284101485") + 283824000 #added 9 years !

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
```

#### Column 7: Time `mtime`

See Column 6

#### Column 8: Name

You can do this one!

