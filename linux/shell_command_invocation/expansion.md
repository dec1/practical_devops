
## Shell Expansion
eg Argument Expansion and Substitution

#### \$ , ${}  - Variable Expansion 

```
var=10
$var      # use the variable
${var}    # (unnecessary) same as above 
${var}bar # (necessary) expand var, and concatenate "bar"
```
#### $() - Command Substitution 

`var = $(some_cmd)`    the output of some_cmd
-  Backticks - alternative (older and **less preferable**) syntax.  
`` var = `some_cmd` `` 
  Less readable esp for nested commands. constrast eg:
  `var=$(cmd_1 $(cmd_2))` vs ```var = `cmd_1 \`cmd_2\`` ``` 

#### <() - Process Substitution 
`var = <(some_cmd)`  path to a (virtual) file _containing_ output of some_cmd
- strictly speaking its a file descriptor (rather than file path)
- can be useful when piping to another command (eg _source_) that expects a file path eg.


`source <(some_cmd)`

which is equivalent to:
```
some_cmd > tmp_file 
source < tmp_file   
rm tmp_file
``````


#### {} - Brace Expansion 
**without $** - with it would be parameter expansion - see above
`a{b,c} -> ab ac`
eg
`mv a{tex, txt}` -> `mv a.tex a.txt`   changes file extension 

#### $(()) - Arithmetic expansion: 
- `$((4+5)) -> 9`


#### \\ - Escape sequences:  
- `\n -> newline`
