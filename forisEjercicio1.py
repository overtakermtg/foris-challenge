# Ejercicio 1 foris
text= "afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood"

# recorre todos los largos posibles de textos
for fin in range(0,len(text)):
	#recorre todo el texto buscando cambiando el inicio de la palabra
	for ini in range(0,len(text)):
		# guarda la palabra generada para luego evaluarla
		word = text[ini:fin]
		# word[::-1] es para invertir la palabra
		if word == word[::-1] and len(word) > 3:
			# solo imprime los palindromos 
			print(word)
