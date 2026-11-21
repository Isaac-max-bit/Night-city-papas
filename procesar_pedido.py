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
    print("=========================\n")

    # Datos previos de tu pedido de Night-city papas
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

    if antojo not in carta:
        print(f"\n¡Hola {nombre}! No hay opción (El plato ingresado no existe).")
        return

    plato_seleccionado = carta[antojo]
    tiempo_prep = plato_seleccionado["tiempo"]
    precio_sugerido = plato_seleccionado["precio"]

    if es_del_barrio:
        precio_sugerido = int(precio_sugerido * 0.9)  # Descuento del 10%
        estado_barrio = "Aplicado descuento del 10% por ser del barrio"
    else:
        estado_barrio = "Se mantiene el precio original"

    if minutos_disponibles < tiempo_prep:
        print(
            f"\n¡Hola {nombre}! No hay opción (No cuentas con los minutos"
            f" suficientes para preparar {antojo})."
        )
        return

    # =========================================================================
    # PASO 1: Recibe y convierte las cuatro entradas en pesos enteros
    # =========================================================================
    plato_1 = int(
        input(f"Precio del plato 1 (pesos enteros, sugerido {precio_sugerido}): ")
    )
    plato_2 = int(input("Precio del plato 2 (pesos enteros): "))
    domicilio = int(input("Valor del domicilio (pesos enteros): "))
    efectivo = int(
        input("Efectivo entregado por el cliente (pesos enteros): ")
    )

    # =========================================================================
    # PASO 2: Primero el total (sin efectivo), después el saldo (efectivo - total)
    # =========================================================================
    total = plato_1 + plato_2 + domicilio
    saldo = efectivo - total

    # =========================================================================
    # PASO 3 y PASO 4: Salida con etiquetas legibles para probar en tu tabla
    # y contrastar casos (saldo 0, todo en cero, o ingresar "hola" -> ValueError)
    # =========================================================================
    print(
        f"\n¡Hola {nombre}! Tu pedido de '{antojo.capitalize()}' ha sido"
        " confirmado."
    )
    print(
        f"• Tiempo requerido: {tiempo_prep} minutos (tienes"
        f" {minutos_disponibles})."
    )
    print(f"• Estado: {estado_barrio}.")
    print(f"Total: {total}")
    print(f"Saldo: {saldo}")


if __name__ == "__main__":
    procesar_pedido()