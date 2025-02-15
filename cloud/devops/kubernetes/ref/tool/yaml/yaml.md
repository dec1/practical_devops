## YAML

- **`key`**: **`value`**
    - `value` can be:
        - `scalar` (number, bool, string, date(time), null)
        - `dict`  (also called `map`)   
        - `list` of values
    - `key` can be:
        - `scalar` (number, bool, string, date(time))
    - values of map/list can in turn be (**recursively**) scalar, list, or map

### 
### Strings
 - **Key**,  **Value**
    - may be _either_ (string _or_ non-string)

- Quotes optional when
    -  not possible to interpret string as other scaler type (ie number, bool, string, date(time), null)
            - unquoted scalars will be interpreted as non-strings if possible 
    - string doesnt contain special characters

---

###
- [example.yaml](example.yaml)
- [grok](grok.md)
- [online validator](https://jsonformatter.org/yaml-validator)
- [json vs yaml](json_vs_yaml.md)
----


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

---
##
