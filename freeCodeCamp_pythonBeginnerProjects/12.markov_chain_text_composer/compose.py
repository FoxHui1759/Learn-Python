import os
import string
import random
from vertex import Vertex


class composer:
    def __init__(self) -> None:
        self.vertices = {}

    def read_text(self, target_file_path: str) -> list[str]:
        with open("texts/hp_sorcerer_stone.txt") as file:
            text = file.read()
        text = text.translate(str.maketrans(" ", " ", string.punctuation))
        text = text.lower()
        words = text.split()
        return words

    def build_graph(self, words: list[str]) -> None:
        pre_word = None
        for word in words:
            if word not in self.vertices:
                self.vertices[word] = Vertex(word)
            if pre_word:
                pre_vertex = self.vertices[pre_word]
                if word in pre_vertex.next_vertices:
                    pre_vertex.frequency[pre_vertex.next_vertices.index(word)] += 1
                else:
                    pre_vertex.next_vertices.append(word)
                    pre_vertex.frequency.append(1)
            pre_word = word

    def get_weight(self, vertex: Vertex) -> list[int]:
        total = sum(vertex.frequency)
        return [i / total * 100 for i in vertex.frequency]

    def get_next_word(self, vertex: Vertex) -> None:
        w = self.get_weight(vertex)
        return random.choices(vertex.next_vertices, weights=w)[0]

    def gen_text(self, length: int) -> str:
        words = []
        vertex = random.choice(list(self.vertices.values()))
        for _ in range(length):
            words.append(vertex.value)
            vertex = self.vertices[self.get_next_word(vertex)]
        return " ".join(words)

    def compose(self, target_file_path: str, length: int) -> string:
        words = self.read_text(target_file_path)
        self.build_graph(words)
        result = self.gen_text(length)
        return result


def main() -> None:
    os.chdir("freeCodeCamp_pythonBeginnerProjects/12.markov_chain_text_composer")
    c = composer()
    result = c.compose(target_file_path="texts/hp_sorcerer_stone.txt", length=500)
    print(result)


if __name__ == "__main__":
    main()
