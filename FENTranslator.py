import globalPluginHandler
import api
import ui

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

  def orden(self, letras):
    piezas = "KQRBNP/kqrbnp"
    for i in range(len(piezas)):
      if piezas[i] == letras[0]:
        return i

  def script_showText(self, gesture):
    board=['a8','b8','c8','d8','e8','f8','g8','h8','a7','b7','c7','d7','e7','f7','g7','h7','a6','b6','c6','d6','e6','f6','g6','h6','a5','b5','c5','d5','e5','f5','g5','h5','a4','b4','c4','d4','e4','f4','g4','h4','a3','b3','c3','d3','e3','f3','g3','h3','a2','b2','c2','d2','e2','f2','g2','h2','a1','b1','c1','d1','e1','f1','g1','h1']
    fen = api.getClipData()[6:-1].split()
    if '-' in fen:
      pos=''.join(fen[0].split('/'))
      turno = fen[1]
    if 'w' in turno:
      turno ='Juegan las blancas:'
    elif 'b' in turno:
      turno ='Juegan las negras:'
    numbers=['1','2','3','4','5','6','7','8']
    piezas = ['/']
    n=0
    for c in pos:
      if c in numbers:
        n += int(c)
      else:
        piezas.append(c+board[n])
        n+=1
    piezas = sorted(piezas, key=self.orden)
    posicion = turno+'\n'+''.join(piezas)
    ui.browseableMessage(posicion)
    api.copyToClip(posicion)

  __gestures={
    "kb:NVDA+Ñ": "showText"
  }

