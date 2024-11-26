# Python-Piscine

## python4_2

### [Ex00](ex00/Hello.py)

#### The first exercise to learn basic Python Variables

- **Tuples**
  - Tuples are inmutable but in this exercise we have to change position  1 value  of the tuple and this is my way to do it
  - ```python
    # this is the original tuple
    ft_tuple = ("Hola", "¡Toto!")
    # made a list wit the tuple and now we can change values
    temp_list = list(ft_tuple)
    temp_list[1] = "¡España!"
    #now convert back to tuple
    ft_tuple = tuple(temp_list)
    ```
