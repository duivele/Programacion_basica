Algoritmo N_HAMBURGUESAS
	Escribir "Qué tipo de hambuguesa desea?";
	Leer tipo; //puede ser 1, 2 o 3
	Escribir  "Cuantas desea?";
	Leer cant; 
	
	Si (tipo = 1) Entonces
		pagar <- (cant*20)+((cant*20)*0.05);
		Escribir "Su total a pagar es: ", pagar;
	Sino Si (tipo = 2)Entonces
			pagar <- (cant*25)+((cant*25)*0.05);
			Escribir "Su total a pagar es: ", pagar;
			
		Sino Si (tipo = 3) Entonces
				pagar <- (cant*28)+((cant*28)*0.05);
				Escribir "Su total a pagar es: ", pagar;
			Sino 
				Escribir "Ingrese un tipo de hambuguesa valido";
			FinSi
		FinSi
	FinSi
FinAlgoritmo
