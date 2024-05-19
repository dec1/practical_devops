
- ### explain
    - `k` **`explain`** `pod` - high level
        - explain _resource_ **Type** _pod_ 
        eg ConJob moved from 
        _"batch/v1beta1"_ ( kubernetes 1.20) -> _"batch/v1"_(kubernetes 1.21)
        kubectl explain cronjob tells you which apiVersion you should be using in your manifests (for the version of kubernetes installed  - which may be 1.20 or older)
        ####
    - `k explain` **`pod.spec`** - subset details

(see also - help on [commands](../main.md))

   
   