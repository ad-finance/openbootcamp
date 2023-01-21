from datetime import time
from datetime import datetime
from datetime import timedelta

HoyEs = datetime.now()

HoraActual = time(HoyEs.hour, HoyEs.minute, HoyEs.second)

HoraDeIrse = time(hour=19,minute=0,second=0)

if HoraActual <= HoraDeIrse:
    print(Diferencia = time(HoraDeIrse.hour-HoraActual.hour,HoraActual.minute,HoraActual.second))
else: print("Hora de irse!")

