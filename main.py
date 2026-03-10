from clases.Herencia1.taxi import Taxi
from clases.Herencia1.auto_particular import AutoParticular

def main():
    coche = Taxi("123-GTO","Versa",1000,"123-a")
    
    print(coche)
    coche.encender()
    coche.subirPasajeros()
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()
    
    ap = AutoParticular("123","Alejandra",15,"Volvo","Plata","987-G")
    print(ap)
    ap.subirseAuto()
    ap.EncenderAuto()
    ap.llegarDestino()
    ap.bajandoAuto()
    
if __name__=='__main__':
    main()