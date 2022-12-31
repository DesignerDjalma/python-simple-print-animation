
import sys
import time

CLEAR_LINE = "\033[K"

animacao = {
    1: ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏",],
    2: ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷",],
    3: ["⠋","⠙","⠚","⠞","⠖","⠦","⠴","⠲","⠳","⠓",],
    4: ["⠄","⠆","⠇","⠋","⠙","⠸","⠰","⠠","⠰","⠸","⠙","⠋","⠇","⠆",],
    5: ["⠋","⠙","⠚","⠒","⠂","⠂","⠒","⠲","⠴","⠦","⠖","⠒","⠐","⠐","⠒","⠓","⠋",],
    6: ["⠁","⠉","⠙","⠚","⠒","⠂","⠂","⠒","⠲","⠴","⠤","⠄","⠄","⠤","⠴","⠲","⠒","⠂","⠂","⠒","⠚","⠙","⠉","⠁",],
    7: ["⠈","⠉","⠋","⠓","⠒","⠐","⠐","⠒","⠖","⠦","⠤","⠠","⠠","⠤","⠦","⠖","⠒","⠐","⠐","⠒","⠓","⠋","⠉","⠈",],
    8: ["⠁","⠁","⠉","⠙","⠚","⠒","⠂","⠂","⠒","⠲","⠴","⠤","⠄","⠄","⠤","⠠","⠠","⠤","⠦","⠖","⠒","⠐","⠐","⠒","⠓","⠋","⠉","⠈","⠈",],
    9: ["⢹","⢺","⢼","⣸","⣇","⡧","⡗","⡏",],
    10: ["⢄","⢂","⢁","⡁","⡈","⡐","⡠",],
    11: ["⠁","⠂","⠄","⡀","⢀","⠠","⠐","⠈",],
    12: ["⢀⠀","⡀⠀","⠄⠀","⢂⠀","⡂⠀","⠅⠀","⢃⠀","⡃⠀","⠍⠀","⢋⠀","⡋⠀","⠍⠁","⢋⠁","⡋⠁","⠍⠉","⠋⠉","⠋⠉","⠉⠙","⠉⠙","⠉⠩","⠈⢙","⠈⡙","⢈⠩","⡀⢙","⠄⡙","⢂⠩","⡂⢘","⠅⡘","⢃⠨","⡃⢐","⠍⡐","⢋⠠","⡋⢀","⠍⡁","⢋⠁","⡋⠁","⠍⠉","⠋⠉","⠋⠉","⠉⠙","⠉⠙","⠉⠩","⠈⢙","⠈⡙","⠈⠩","⠀⢙","⠀⡙","⠀⠩","⠀⢘","⠀⡘","⠀⠨","⠀⢐","⠀⡐","⠀⠠","⠀⢀","⠀⡀",],
}

def escrever(t, fps=30) -> None:
    sys.stdout.write("\r")
    sys.stdout.write(f" {t}")
    time.sleep(1/fps)


def limparTela() -> None:
    sys.stdout.write(f"{CLEAR_LINE}")
    sys.stdout.write("\r")
    print("   ")


class Animacao:
    def __init__(self, texto: str = "Carregando",
                 tempo: int = 3, estilo_anim = 1,
                 fps: int = 30 ) -> None:

        self.start(
            texto=texto,
            tempo=tempo,
            estilo_anim=estilo_anim,
            fps=fps,
        )

    def start(self, texto="Carregando", tempo=3, estilo_anim=1, fps=30):
        frames = animacao[estilo_anim]
        segundos = range(tempo)
        for sec in segundos:
            for frame in frames:
                escrever(f"{frame} {texto}{CLEAR_LINE} {sec+1}/{tempo}", fps=fps)
        limparTela()
                

if __name__ == "__main__":
    print("Iniciando Programa...")
    Animacao("Carregando Modulos", tempo=2, estilo_anim=12, fps=30)
    print("Concluído!")

