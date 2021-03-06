import numpy as np

from .unit import Unit


class CharacterIndex(Unit):
    """
    CharacterIndexUnit for DIIN model.

    The input of :class:'CharacterIndexUnit' should be a list of word
    character list extracted from a text. The output is the character
    index representation of this text.

    :class:`NgramLetterUnit` and :class:`VocabularyUnit` are two
    essential prerequisite of :class:`CharacterIndexUnit`.

    Examples:
        >>> input_ = [['#', 'a', '#'],['#', 'o', 'n', 'e', '#']]
        >>> character_index = CharacterIndex(
        ...     char_index={
        ...      '<PAD>': 0, '<OOV>': 1, 'a': 2, 'n': 3, 'e':4, '#':5})
        >>> index = character_index.transform(input_)
        >>> index
        [[5, 2, 5], [5, 1, 3, 4, 5]]

    """

    def __init__(
        self,
        char_index: dict,
    ):
        """
        Class initialization.

        :param char_index: character-index mapping generated by
            :class:'VocabularyUnit'.
        """
        self._char_index = char_index

    def transform(self, input_: list) -> list:
        """
        Transform list of characters to corresponding indices.

        :param input_: list of characters generated by
            :class:'NgramLetterUnit'.

        :return: character index representation of a text.
        """
        idx = []
        for i in range(len(input_)):
            current = [
                self._char_index.get(input_[i][j], 1)
                for j in range(len(input_[i]))]
            idx.append(current)
        return idx
