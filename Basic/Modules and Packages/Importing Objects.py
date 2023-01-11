# game.py
# import the draw module
from draw import draw_game #Usar from draw import * para importar todos os objetos de um módulo

def main():
    result = play_game()
    draw_game(result)

# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    # Podemos escolher qualquer nome para carregar um modulo
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)