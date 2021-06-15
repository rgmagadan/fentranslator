import globalPluginHandler
import api
import ui

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

  def orden(self, letras):
    if letras[0] == 'k' or letras[0] == 'K':
      v=0
    elif letras[0] == 'q' or letras[0] == 'Q':
      v=1
    elif letras[0] == 'r' or letras[0] == 'R':
      v=2
    elif letras[0] == 'b' or letras[0] == 'B':
      v=3
    elif letras[0] == 'n' or letras[0] == 'N':
      v=4
    elif letras[0] == 'p' or letras[0] == 'P':
      v=5
    return v


  def script_showText(self, gesture):
    board=['a8','b8','c8','d8','e8','f8','g8','h8','a7','b7','c7','d7','e7','f7','g7','h7','a6','b6','c6','d6','e6','f6','g6','h6','a5','b5','c5','d5','e5','f5','g5','h5','a4','b4','c4','d4','e4','f4','g4','h4','a3','b3','c3','d3','e3','f3','g3','h3','a2','b2','c2','d2','e2','f2','g2','h2','a1','b1','c1','d1','e1','f1','g1','h1']
    numbers=['1','2','3','4','5','6','7','8']
    texto = api.getClipData()
    fen = texto[6:-1].split()
    if '-' in fen:
      pos=''.join(fen[0].split('/'))
      j=fen[1]
    blancas=[]
    negras=[]
    n=0
    if 'w' in j:
      j='Juegan las blancas:'
    elif 'b' in j:
      j='Juegan las negras:'
    for c in pos:
      if c in numbers:
        n=n+int(c)
      elif c.islower():
        negras.append(c+board[n])
        n+=1
      else:
        blancas.append(c+board[n])
        n+=1
        blancas = sorted(blancas, key=self.orden)
        negras = sorted(negras, key=self.orden)
        posicion = j+'\n'+''.join(blancas)+'/'+''.join(negras)+'\n'
    ui.browseableMessage(posicion)
    api.copyToClip(posicion)

  __gestures={
    "kb:NVDA+Ñ": "showText"
  }

