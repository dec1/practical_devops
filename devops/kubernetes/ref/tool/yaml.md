- `key`: `value`
    - `value` can be:
        - `scalar`
        - `map`     
        - `list`

    - values of map/list can in turn be (**recursively**)  scalar, list, map    


 Note: Names of `keys` below refer to tyoe of value (not key - which in example are always scalar - even though in general this need not be).

- #### Lists - Discern boundary (crucial to grokking doc structure)
    - A line that starts with (optional whitespace and) `-` indicates a list item.
    - Each subsequent line that begins with `-` at the same indentation level is considered a sibling list item.
    - Everthing before the `-` starting the next sibling is part of teh first list item  (which may be recursive ie itself a list or map...)
    - This sibling relationship continues until a new key-value pair (`key:`) is encountered at the **same indentation** level as the list items' **parent key**.


```yaml
# value is scalar
scalar: val

# ------------------------
# values are lists
list: 
- 1
- 2

list_also: 
  - 1
  - 2

list2: [1, 2]
    
list3: [
    1,
2]

# ------------------------
# values are maps
map:
  one: 1
  two: 2

map2: {one: 1, two: 2 }

map3: {
  one: 1, 
    two: 2 }
    
# ------------------------
# values are not maps - careful
map_not:  # null is implicit value (without subsequent lines indented)
a1: 1
b1: 2

map_not2: null  # ie
a2: 1
b2: 2
# ------------------------
# nested:
#---------
# values is lists with some items being (nested) lists/maps - careful

nested: 
- 1
- 2: two
  3: three
- - 4
  - 5 

nested2: [
    1, 
    {
      "2": "two", 
      "3": "three"
    }, 
    [
      4, 
      5
    ]
  ]
  # ------------------------

```

----

### Quotes with Key, Value


 - **Key** 
    - _always_  **string** (interpretation)
    
- **Value**
    - may be _either_ (string _or_ non-string)

###

- **Strings**:
    - **special characters**(eg whitespace) -  use Quotes 
    - else  _optional_  
    
- **Non-Strings** - never quote (cant contain special-chars)

-----

### Literal Block Scalar ( **\: |**  )

- Can be used to **start a value** (only), which can then contain
- **embedded newlines** and other whitespace
```yaml
  my-key: |
    my-val_line_1
    my-val_line_2
```  

###
Multiple Documents
- `---` yaml document separator in single file/stream

###
Online tools:
- [yaml lint](https://www.yamllint.com/) - makes canaonical
- [yaml pareser](https://yaml-online-parser.appspot.com/) - shows json 
- [jsonformatter](https://jsonformatter.org/yaml-parsersemantic) - shows tree



