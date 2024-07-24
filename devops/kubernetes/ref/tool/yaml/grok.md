### Grokking Yaml 

- #### Lists - Discern boundary (crucial to grokking document structure)
    - A line that starts with (optional whitespace and) `-` indicates a list **item**.
    - Each subsequent line that begins with `-` at the same indentation level is considered a sibling list item.
    - Everything before the `-` starting the next sibling is part of the first list item (which may be recursive, i.e., itself a list or map).
    - This sibling relationship continues until a new key-value pair (`key:`) is encountered at the **same indentation** level as the list items' **parent key**.

```yaml
#  Names of `keys` below refer to the type of value (not the key itself)

# value is scalar
scalar: val

# ------------------------
# values are lists

list_name: 
- 1     # list item (value)
- 2     # list item (value)

list_also: 
  - 1
  - 2

list2: [1, 2]
    
list3: [
    1,
    2
]

# ------------------------
# values are maps

map:
  one: 1
  two: 2

map2: {one: 1, two: 2 }

map3: {
  one: 1, 
  two: 2
}
    
# ------------------------
# values are not maps - careful
map_not:  # null is implicit value (without subsequent lines indented)
a1: 1
b1: 2

map_not2: null  # explicit null value
a2: 1
b2: 2
# ------------------------
# nested:
#---------
# values are lists with some items being (nested) lists/maps - careful

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
