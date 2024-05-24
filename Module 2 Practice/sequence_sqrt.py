# Author Jibran Gill
# Learning the application of sequences in Python

def print_sequence(seq):
    for i in seq:
        print(i, end = ' ')

def sqroot_sequence(seq):
    seq2 = [(x, x**2) for x in seq]
    return seq2

def seq_times_two(seq):
    seq2 = [(i * 2) for i in seq]
    return seq2

def seq_mod_3(seq):
    seq2 = [(i) for i in seq if i %3  == 0 ]
    return seq2


def main():
    seq = range(11)
    print('Sequence is: ')
    print_sequence(seq)
    print ('\n\nSequrce square root is:')
    tuple_sqroot = sqroot_sequence(seq)
    print_sequence(tuple_sqroot)
    print ('\n\nSequence times two is:')
    list_seq_times_two = seq_times_two(seq)
    print_sequence(list_seq_times_two)
    print ('\n\nSequence mod 3 is:')
    list_mod_3 = seq_mod_3(seq)
    print_sequence(list_mod_3)

if __name__ == "__main__":
    main()
