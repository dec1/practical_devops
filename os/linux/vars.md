Export
------

**`export`** `myvar=3`

Create an environment variable. Since child processes  get evn seeded from parent's env -> they will see it.
(Note any changes child subsequently makes to env does not affect that of parent .. need "source" for this  - see below)


Source
-------
**`source`** `my_script.sh  ` 
 or equivalently
` .` `my_script.sh`

Run my_script.sh in env of caller. 
Thus changes to env made by child do **affect caller**
