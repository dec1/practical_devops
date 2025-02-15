

- `d` **`inspect`**  `my_ctr | myimg`
    detailed (json) info on docker object (eg container or image )
 

    - just one detail of inspect (uses "Go" template)
 `docker inspect --format='{{ .State.Running }}' my_ctr`