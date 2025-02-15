#### Standard Streams

All processes have (from os) std steams, to which they can read/write.

- **cin**  
#####
- **cout**
- **cerr**    


####

Default
- **keyboard** - cin  , 
- **screen** -  cout, cerr

###
But  can be changed by

- **Redirect**   to/from **file**
    #####
    - **cin** (**<**)
        `c < file_in`
         *cin* of process c is file called *file_in*
    ####
    - **cout**(**>** or **1>**), **cerr** (**2>**) 
        - `c1` `> file_out`
        - `c1  1> file_out`
                *cout* of c1 is file called *file_out*

        ####
        - `c1 2> file_err`        
            *cerr* of c1 is file called *file_err*
        
        - `c1 2> file_err > file_out`        
            *cerr* of c1 is file called *file_err*, and its *cout* is file called *file_out*
        ####

        - `c1 > file_both 2>&1 ` 
        - `c1 > file_both &> ` 
            *cerr* and *cout* ...... *file_both* 
            (note: order of  matters: `c1 2>&1 > file_both` is _not_ the same - cerr goes to the _original_ dest of cout)

####

- **Pipe**  ( **|** ) between **process**_es_

    - `c1 | c2`
     *cout* of c1 is *cin* for c2
     
        - _Note_: c2 does **not wait** for c1 to finish before starting - 
        both c1 and c2 are started (almost) **simultaneously**.

    <br>

    - `c1 | tee [-a] file_out`
    **tee** writes it cin to both its cout and file_out (appending if -a is specified)

    