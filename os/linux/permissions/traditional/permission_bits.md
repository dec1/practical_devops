#### `Permission  Bits`
Also known as `File Mode`

 3 triads of characters in [output of ls](ls.md)

| user    (1st triad)          | group (2nd triad)                         | other  (3rd triad)             |
| ----------------- | ------------------------------ | ------------------- |
| `[r][w]` **`[x\|s\|S]`** | `[r][w]` **`[x\|s\|S]`** | `[r][w]` **`[x\|t]`** |





###
- Triad  Values

    | Permission | File Action                              | Directory Action                       |
    |------------|------------------------------------------|----------------------------------------|
    | `x`        | **execute**                              | `cd`  |
    | `r`        | **read**  (contents)                                   | `ls`                   |
    | `w`        | **write** (contents)                      |`touch`, `rm`,  `mv` <br>  create, delete, rename contained files  <br><br> *(non-intuitive - see _sticky bit_ below; owner of dir can delete/rename contained files owned by someone else)* |
    | `S`       | **`setuid/setgid`** are set but `x` is _not_ <br> <br> can only appear in 3rd col (where x usually is) of _user/group_  triad.   <br> <br>  file runs as process with uid/gid of file, not that of process accessing the file   <br>    <br>  _s_ (without _x_) is not very useful - since without _x_ nobody can execute  - see `s` | new files and subdirectories created within this dir have their group set to that of the dir, not the process creating them <br><br> subdirs also inherit setgid | 
    | `s`       | `s` and `x` are both set <br> <br> can only appear in 3rd col (where x usually is) of _user/group_  triad
    | `t`        |   | **`sticky bit`**   when visible in 3rd col of _other_ triad <br> <br> **only owner of files** (or root)  within can delete, rename files -                                                    not owner of  this dir  (cant be used in any other column) |