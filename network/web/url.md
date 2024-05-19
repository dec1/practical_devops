### Url Anatomy


`https://` `[user[:password]@]` `www.sdom.dom.com` `[:443]` /`some/path` `[?key=val1&key2=val2]` `[#question13]`

`scheme://` `authority` /`path` `[?queryString]` `[#fragment]`
###
- `scheme` - https
- `authority` - user:password@**host**:port
    
    ###
    - **`host`**   -      **`hostname`**.**`domain`**
      - `hostname` -    `www`
      - `domain`  - `sdom.dom.com`

        ### 
        - `top level`    -     com
        - `sub`      -  dom
        - `subsub`   -  sdom


    ###
    - `port` - 443
- `path`:       -    some/path
- `queryString` key val pairs separated by `&` or `;`
    - key=val1
    - key2=val2 


##
- `fragment`:  -       question13       

---

 - [what-every-developer-should-know-about-urls](https://skorks.com/2010/05/what-every-developer-should-know-about-urls/)
 - [qt -  url](https://doc.qt.io/qt-6/qurl.htm)