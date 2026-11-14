def procesar_pedido():
  print("¡Bienvenido Night-city papas!\n")
  
  # Definición de la carta de platos con sus precios y tiempos de preparación
  carta = {
      "papas ropa vieja": {"precio": 24000, "tiempo": 20},
      "papas locas": {"precio": 20000, "tiempo": 18},
      "picada gigante": {"precio": 30000, "tiempo": 25},
      "arepa rellena": {"precio": 15000, "tiempo": 10},
  }

  print("=== MOSTRAR CARTA ===")
  for plato, info in carta.items():
    print(
        f"- {plato.capitalize()}: ${info['precio']:,.0f} - {info['tiempo']}"
        " minutos"
    )
  print("=====================\n")

  # 1. Recibir los datos del contrato
  nombre = input("Ingrese su nombre: ")
  antojo = input("Ingrese el plato deseado (antojo): ").strip().lower()

  try:
    minutos_disponibles = int(
        input("Ingrese sus minutos disponibles (tiempo de espera): ")
    )
  except ValueError:
    print("Error: Los minutos deben ser un valor numérico.")
    return

  es_del_barrio = (
      input("¿Es del barrio? (Sí / No): ").strip().lower() in ["sí", "si", "s"]
  )

  # 2. Buscar plato elegido en la carta y validar si existe
  if antojo not in carta:
    print(f"\n¡Hola {nombre}! No hay opción (El plato ingresado no existe).")
    return

  plato_seleccionado = carta[antojo]
  tiempo_prep = plato_seleccionado["tiempo"]
  precio_original = plato_seleccionado["precio"]

  # 3. Validar si los minutos disponibles son menores al tiempo de preparación
  if minutos_disponibles < tiempo_prep:
    print(
        f"\n¡Hola {nombre}! No hay opción (No cuentas con los minutos"
        f" suficientes para preparar {antojo})."
    )
    return

  # 4. Validar si es del barrio para aplicar descuento del 10%
  if es_del_barrio:
    precio_final = precio_original * 0.9  # Descuento del 10%
    estado_barrio = "Aplicado descuento del 10% por ser del barrio"
  else:
    precio_final = precio_original
    estado_barrio = "Se mantiene el precio original"

  # 5. Salida: un solo mensaje con los datos integrados
  mensaje = (
      f"\n¡Hola {nombre}! Tu pedido de '{antojo.capitalize()}' ha sido"
      f" confirmado.\n"
      f"• Tiempo requerido: {tiempo_prep} minutos (tienes"
      f" {minutos_disponibles}).\n"
      f"• Estado: {estado_barrio}.\n"
      f"• Precio final a pagar: ${precio_final:,.0f}"
  )

  print(mensaje)


if __name__ == "__main__":
  procesar_pedido()