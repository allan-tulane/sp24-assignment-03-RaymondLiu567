import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    elif S[0] == T[0]:
        return MED(S[1:], T[1:])
    else:
        return 1 + min(
            MED(S, T[1:]),  # Insertion
            MED(S[1:], T),  # Deletion
            MED(S[1:], T[1:])  # Substitution
      )


def fast_MED(S, T, memo=None):
    if memo is None:
        memo = {}
    if (S, T) in memo:
        return memo[(S, T)]
    if S == "":
        memo[(S, T)] = len(T)
    elif T == "":
        memo[(S, T)] = len(S)
    elif S[0] == T[0]:
        memo[(S, T)] = fast_MED(S[1:], T[1:], memo)
    else:
        memo[(S, T)] = 1 + min(
            fast_MED(S, T[1:], memo),  # Insertion
            fast_MED(S[1:], T, memo),  # Deletion
            fast_MED(S[1:], T[1:], memo)  # Substitution
    )
    return memo[(S, T)]


def fast_align_MED(S, T, memo=None):
    if memo is None:
        memo = {}
    if (S, T) in memo:
        return memo[(S, T)]
    if S == "":
        memo[(S, T)] = (len(T), '-' * len(T) + S, T)
    elif T == "":
       memo[(S, T)] = (len(S), S, '-' * len(S) + T)
    elif S[0] == T[0]:
        cost, s_align, t_align = fast_align_MED(S[1:], T[1:], memo)
        memo[(S, T)] = (cost, S[0] + s_align, T[0] + t_align)
    else:
        ins_cost, s_ins, t_ins = fast_align_MED(S, T[1:], memo)
        del_cost, s_del, t_del = fast_align_MED(S[1:], T, memo)
        sub_cost, s_sub, t_sub = fast_align_MED(S[1:], T[1:], memo)

        if ins_cost <= del_cost and ins_cost <= sub_cost:
            memo[(S, T)] = (1 + ins_cost, '-' + s_ins, T[0] + t_ins)
        elif del_cost < ins_cost and del_cost <= sub_cost:
            memo[(S, T)] = (1 + del_cost, S[0] + s_del, '-' + t_del)
        else:
          memo[(S, T)] = (1 + sub_cost, S[0] + s_sub, T[0] + t_sub)

    return memo[(S, T)]
