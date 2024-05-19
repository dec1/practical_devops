
#### Modes 
- **Normal**
- **Command**
- **Insert**

- **Visual** Modes allow you to select text that gets visually highlighted. Then you can run (normal mode) commands on the selected text
    - `V`             visual line  (whole lines)
    - `v`             visual 
    - `Ctrl  + v`     visual block  


------
#### Normal Mode

`i`         - _Insert_ mode
`o`         - line break  **_after_**  current and _Insert_ mode
`O`         - line break  _before_  current and _Insert_ mode 


`:`         - command mode


##### Edit
- **yank**
    `y`            - yank selection (copy)
    `yy`           - yank line 
###
- **delete**
    `d`            - delete selection (cut)
    `dd`           - delete line   
    ####
    `x`            - delete (char after cursor)
    `X`            - backspace (delete char before cursor)


####
- **paste**
    `P`            - paste yank  (from prev yank - ie register)
    `p`            - paste yank on next line 
    #####
    `Cmd/Ctrl + V` - paste clipboard (os)


###
- **undo**
    `u`        - undo 
    `ctrl-r`   - redo 

####
- **indent** selection
    `>`        - in 
    `<`        - out

####
- **repeat** 
    `.`        - prev command


##### Move
`0`    - start of line
`$`    - end of line

`w`    - forward word
`b`    - backward word

##
`Ctrl+u` - 1/2 page Up
`Ctrl+d` - 1/2 page Down

`Ctrl+b` - page Up
`Ctrl+f` - page Down

##
`gg` or `[[` - first line 

`G `  or `]]` - last line

- **select all**
    `gg`, `V`, `G` - (**move** to first line, enter **visual** _line_ mode, **move** to last line)

------
#### Command Mode
##### Finish

`:w` - write file (with current selection, if any)
`:r` - read file
`:q` - quit
`Esc`- normal mode

`:set number` - toggle line numbers **on**
`:set nonumber` - toggle line numbers **off**

