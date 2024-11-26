lista_ft = ["Hola", "¡tata!"]
lista_ft[1] = "¡Mundo!"
print(lista_ft)

ft_tuple = ("Hola", "¡Toto!")
lista_temporal = list(ft_tuple)
lista_temporal[1] = "¡España!"
ft_tuple = tuple(lista_temporal)
print(ft_tuple)

ft_set = {"Hola", "¡tutú!"}
ft_set.remove("¡tutú!")
ft_set.add("¡Urduliz!")
print(ft_set)

ft_dict = {"Hola": "¡Titi!"}
ft_dict["Hola"] = "¡42Urduliz!"
print(ft_dict)

