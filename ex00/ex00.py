lista_ft = ["Hola", "¡tata!"]
lista_ft[1] = "¡Mundo!"
print(lista_ft)

ft_tuple = ("Hola", "¡Toto!")
temp_list = list(ft_tuple)
temp_list[1] = "¡España!"
ft_tuple = tuple(temp_list)
print(ft_tuple)

ft_set = {"Hola", "¡tutú!"}
ft_set.remove("¡tutú!")
ft_set.add("¡Urduliz!")
print(ft_set)

ft_dict = {"Hola": "¡Titi!"}
ft_dict["Hola"] = "¡42Urduliz!"
print(ft_dict)

