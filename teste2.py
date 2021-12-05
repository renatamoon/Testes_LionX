"""2) Given two non-empty arrays of integers (array_value and sequence), write a function that
determines whether the second array is a subsequence of the first one.

Inputs:
array_value = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Outputs:
It’s a boolean value"""

array_value = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def validation_subsequence_array(array_value, sequence):
    sequenc_cont = 0
    length_sequence = len(sequence)
    for i in array_value:
        if sequenc_cont == length_sequence:
            if i == sequence[sequenc_cont]:
                sequenc_cont += 1
        if sequenc_cont == length_sequence:
            return True
        else:
            return False

print(validation_subsequence_array(array_value, sequence))