#Calcular el porcentaje que corresponde a cada departamento

#Definir la funcion
def calcularpresupuestos(monto):
    recursoshumanos = monto * 0.50
    manufactura = monto * 0.25
    empaquetado = monto * 0.15
    publicidad = monto * 0.10
    
    #Mostrar los resultados
    print(f"Recursos Humanos: ${recursoshumanos:.2f}")
    print(f"Manufactura: ${manufactura:.2f}")
    print(f"Empaquetado: ${empaquetado:.2f}")
    print(f"Publicidad: ${publicidad:.2f}")

#Solicitar el presupuesto
presupuestoanual = float(input("Ingrese el monto del presupuesto anual: $"))
calcularpresupuestos(presupuestoanual)