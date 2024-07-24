## JSON

- #### Values:
    - **Number** - integer or floating-point
    - **String** - quoted
    - **Boolean** - `true` or `false`
    - **Dict** - `{ "key": val, "key2": val2, ... }` where
        - keys are (quoted) strings
        - vals are any other `value`
        - also called `array`
    - **List** - `[val, val2, ...]` where
        - vals are any other `value`
    - **null** - literal

The outer element has to be an array `[]` or an object `{}`.

- [example.json](example.json)
- [json vs yaml](../yaml/json_vs_yaml.md)