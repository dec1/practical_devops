## ConfigMaps & Secrets

Config maps and secrets are both just **list** of **[key, value]** pairs (_entries_) but for convenience can be [created](configmap/cm_create.md) in any of **4** number of different ways, and [injected](configmap/cm_inject.md) into a pod in any of **2** different ways (independently of how they were created) 

- ###  ConfigMap
    Resources contain plaintext values (unencoded)
    In manifest:
    - `data`  plaintext
    - '_binaryData_'  no functional difference to  _data_ ("_supposed to be for base64 encoded values_")

- ### Secrets 
    Resources contain base64 encoded values
    - In Manifest:
        - `data`  base64 encoded  (see eg base64 command line tool - see below)
        - `stringData`  plaintext 

    - Imperative
        - `kubectl  create secret` 
            - `data`  pass as plaintext and encoded automatically
            - `stringData`  cant pass
    


---
see also [base64](../../../tool/base64.md)

