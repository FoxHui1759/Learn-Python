import os
import string
from vertex import Vertex


class composer:
    def __init__(self) -> None:
        self.vertices = {}

    def read(self) -> None:
        with open("texts/hp_sorcerer_stone.txt") as file:
            text = file.read()
        text = text.translate(str.maketrans(" ", " ", string.punctuation))
        text = text.lower()
        words = text.split()

        pre_word = None
        for word in words:
            if word not in self.vertices:
                self.vertices[word] = Vertex(word)
                if pre_word:
                    pre_vertex = self.vertices[pre_word]
                    pre_vertex.next[word] = pre_vertex.next.get(word, 0) + 1

    def compose(self, length: int) -> string:
        pass


def main() -> None:
    os.chdir("freeCodeCamp_pythonBeginnerProjects/12.markov_chain_text_composer")
    c = composer()
    c.read()


if __name__ == "__main__":
    main()
