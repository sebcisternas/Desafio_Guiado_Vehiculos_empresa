from appweb.models import Chofer,Vehiculo,RegistroContabilidad


def crear_vehiculo(patente,modelo,marca,year,activo=False):
    vehiculo = Vehiculo(patente=patente,modelo=modelo,marca=marca,year=year)
    vehiculo.save()
    print("Se ha creado exitosamente el vehiculo.")
    return vehiculo


def crear_chofer(rut,nombre,apellido,activo=False):
    
    if Chofer.objects.filter(rut=rut).exists():
            print("Ya existe este Rut.")
            return None
        
        
    chofer = Chofer(rut=rut,nombre=nombre,apellido=apellido,activo=activo)    
    chofer.save()
    print("Se ha creado exitosamente el chofer.")
    return chofer



def crear_registro_contable(fecha_compra,valor,vehiculo):
    
    if RegistroContabilidad.objects.filter(vehiculo=vehiculo).exists():
            print("Ya existe esta fecha.")
            return None
    
    registro_contable = RegistroContabilidad(fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo)
    registro_contable.save()
    
    print("Se ha creado exitosamente el registro.")
    return registro_contable



def deshabilitar_chofer(rut):
    if Chofer.objects.filter(rut=rut).exists():
        chofer = Chofer.objects.get(rut=rut)
        chofer.activo = False
        chofer.save()
        print("Se ha deshabilitado exitosamente el chofer.")
        return chofer
    else:
        print("No existe este chofer.")
        return None


    
def deshabilidar_vehiculo(patente):
    if Vehiculo.objects.filter(patente=patente).exists():
        vehiculo = Vehiculo.objects.get(patente=patente)
        vehiculo.activo = False
        vehiculo.save()
        print("Se ha deshabilitado exitosamente el vehiculo.")
        return vehiculo
    
def habilitar_chofer(rut):
    if Chofer.objects.filter(rut=rut).exists():
        chofer = Chofer.objects.get(rut=rut)
        chofer.activo = True
        chofer.save()
        print("Se ha habilitado exitosamente el chofer.")
        return chofer
    else:
        print("No existe este chofer.")
        return None
    
     
def habilitar_vehiculo(patente):
    if Vehiculo.objects.filter(patente=patente).exists():
        vehiculo = Vehiculo.objects.get(patente=patente)
        vehiculo.activo = True
        vehiculo.save()
        print("Se ha habilitado exitosamente el vehiculo.")
        return vehiculo

def obtener_vehiculo(patente):
    if Vehiculo.objects.filter(patente=patente).exists():
        vehiculo = Vehiculo.objects.get(patente=patente)
        print("Se ha encontrado exitosamente el vehiculo.")
        return vehiculo
    else:
        print("No existe este vehiculo.")
        

def obtener_chofer(rut):
    if Chofer.objects.filter(rut=rut).exists():
        chofer = Chofer.objects.get(rut=rut)
        print("Se ha encontrado exitosamente el chofer.")
        return chofer
    else:
        print("No existe este chofer.")
        
def asignar_chofer_a_vehiculo(rut):
    if Chofer.objects.filter(rut=rut).exists():
        chofer = Chofer.objects.get(rut=rut)
        if chofer.activo == True:
            if chofer.vehiculo == None:
                print("Se ha asignado exitosamente el chofer al vehiculo.")
                return chofer  
            
def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    if vehiculos:
        print("Datos de los vehículos:")
        for vehiculo in vehiculos:
            chofer_asignado = vehiculo.chofer.nombre + ' ' + vehiculo.chofer.apellido if vehiculo.chofer else "Ningún chofer asignado"
            mensaje = (
                f"Patente: {vehiculo.patente}\n"
                f"Marca: {vehiculo.marca}\n"
                f"Modelo: {vehiculo.modelo}\n"
                f"Año: {vehiculo.year}\n"
                f"Activo: {'Sí' if vehiculo.activo else 'No'}\n"
                f"Chofer asignado: {chofer_asignado}\n"
            )
            print(mensaje)
    else:
        print("No hay vehículos registrados.")