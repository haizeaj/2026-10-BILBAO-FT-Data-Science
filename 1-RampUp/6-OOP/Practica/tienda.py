class Tienda:
    tipo = "Electrodomésticos"
    abierta = True
    def __init__(self, nombre, direccion, empleados, ventas_3meses):
            # Atributos particulares de cada instancia
            self.nombre = nombre
            self.direccion = direccion
            self.empleados = empleados
            self.ventas_3meses = ventas_3meses 
    
    def calculo_ventas(self):
        return sum(self.ventas_3meses)
    
    def calcular_media_ventas_por_empleado(self):
        total_ventas = self.calculo_ventas()
        if self.empleados == 0:
            return 0
        media_por_empleado = total_ventas / self.empleados
        return media_por_empleado            

    def info_tienda(self):
        return f"Tienda: {self.nombre} - Dirección: {self.direccion}" 

    def ventas_mes(self):
        return self.ventas_3meses[-1]

    def ventas_marketing(self, inversion_marketing: float):
        if inversion_marketing < 1000:
            multiplicador = 1.2
        else:
            multiplicador = 1.5
            for indice, venta in enumerate(self.ventas_3meses):
                self.ventas_3meses[indice] = venta * multiplicador
        return self.ventas_3meses