ft_list=["Hello", "tata!"]
ft_tuple=("Hello", "toto!")
ft_set={"Hello", "tutu!"}
ft_dict={"Hello", "titi!"}

ft_list = ["Hola", "¡tata!"]
ft_list[1] = "¡Mundo!"


ft_tuple = ("Hola", "¡Toto!")
lista_temporal = list(ft_tuple)
lista_temporal[1] = "¡España!"
ft_tuple = tuple(lista_temporal)


ft_set = {"Hola", "¡tutú!"}
ft_set.remove("¡tutú!")
ft_set.add("¡Urduliz!")


ft_dict = {"Hola": "¡Titi!"}
ft_dict["Hola"] = "¡42Urduliz!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)