hands = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
p1 = []
p2 = []


def pokeranalyze(hand):
    handval = 0
    xof = []
    highcard = 0
    values = [hands[a[0]] for a in hand]
    suits = [a[1] for a in hand]
    if len(set(suits)) == 1:
        print('Found flush')
        handval = 5
        highcard = max(values)

    if len(set(values)) == 5 and set(values) == set(range(min(values), min(values) + 5)):
        if set(values) == {10, 11, 12, 13, 14} and handval == 5:
            print('Found royal flush')
            handval = 9
        else:
            if handval == 5:  #if flush
                print('Found straight flush')
                handval = 8
            else:
                print('Found straight')
                handval = 4
        highcard = max(values)

    for card in values:

        if values.count(card) == 4:
            print('Found four of a kind')
            handval = 7
            xof.append(card)
            highcard = set(hand).difference(set(card))
            break

        if values.count(card) == 3:
            print('Found three of a kind')
            if handval == 1:
                print('Found Full House')
                handval = 6
            else:
                handval = 3
            xof.append(card)
            highcard = max(values)
            break

        if values.count(card) == 2 and card not in xof:
            print('Found a pair of', card)
            xof.append(card)
            if handval == 1:
                print('Found two pair', xof[0], 'and', xof[1])
                handval = 2
            elif handval == 3:
                print('Found full house')
                handval = 6
            else:
                handval = 1
            highcard = max(values)

    if handval == 0:
        highcard = max(values)
        print('No hands found, highcard is', highcard)
    return [handval, xof, highcard]


def comparehands(hand1, hand2):
    if hand1[0] > hand2[0]:
        return 1
    elif hand2[0] > hand1[0]:
        return 2
    elif hand1[0] == hand2[0] and hand1[1] != [] and hand2[1] != []:
        if max(hand1[1]) > max(hand2[1]):
            return 1
        elif max(hand1[1]) < max(hand2[1]):
            return 2
    if hand1[2] > hand2[2]:
        return 1
    elif hand1[2] < hand2[2]:
        return 2
    return 0


def compare(i):
    print('Hand 1:', p1[i])
    a = pokeranalyze(p1[i])
    print('Hand 2:', p2[i])
    b = pokeranalyze(p2[i])
    i = comparehands(a, b)
    return i


f = open('54input.txt', 'r')
for line in f:
    t = line[:-1]
    t = t.rsplit(' ')
    p1.append(t[:5])
    p2.append(t[5:])
f.close()

p1w = 0
p2w = 0
match = 0

for i in range(len(p1)):
    print('Hand #', i)
    x = compare(i)
    if x == 1:
        print('P1 won')
        p1w += 1
    if x == 2:
        p2w += 1
        print('P2 won')
    if x == 0:
        print('Warning, hands match!!!!!!')
        match += 1

print('Player 1 has', p1w, 'hands won, and Player 2 has', p2w, 'hands won, and there were', match, 'matches')

