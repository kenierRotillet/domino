import jugador
import generaFichas

listafichas=generaFichas.cGenera()

j1=jugador.cJugador("jugador1",listafichas.listas[0:10])
j2=jugador.cJugador("jugador2",listafichas.listas[10:20])
j3=jugador.cJugador("jugador3",listafichas.listas[20:30])
j4=jugador.cJugador("jugador4",listafichas.listas[30:40])

print(j1.fichas[0].)
print(j2.fichas)
print(j3.fichas)
print(j4.fichas)

