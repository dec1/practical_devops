

### Previous command (!x)


`!str`          (prev command) starting with "str"

`!^`            second word (first arg) (of prev command)
`!$`            last word ....


`!!`           all of (prev command)
 `sudo !!`     (prev command) as sudo

###

`!!:gs/old/new/`    (all of prev command) but ever instance of "old" -> "new" (gs = _"global substitute"_)

`!^old^new`         (all of prev command) but replace first instance of "old" -> "new"


### search
`CTRL + R`    
 - interactive command **history** search
                (repeat shortcut to cycle through results)
            `Enter` to choose
