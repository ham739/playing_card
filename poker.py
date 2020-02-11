import random
import sys
import re
from itertools import groupby

def check():

    hand = []
    main()

def make_deck():
    """
    使うトランプを渡す
    output
        各トランプを表す文字列が入った配列を返却

    """

    return [
        '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
        '♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
        '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
        '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K'
    ]

def draw_from_deck(deck, hand, n=1):
    """
    役を確定させる

    input
        deck:make_deckの配列
        hand:手札を入れる配列。基本的に空
        n:引く枚数。指定がなければ1枚
    output
        hand:引いた後の手札。指定がなければ5枚

    """

    for i in range(n):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)

    return hand


def mulligan(hand):

    """
    手札を交換する

    input
        hand:手札のカードをそれぞれ配列にいれたもの
    output
        sa:手札を交換する位置を指定した配列

    """
    print("捨てるカードを選択します。ない場合はそのままエンターを押してください")
    print("")
    sa = []
    try:
        a = input("捨てるカード選択1:")
        at = int(a) -1
        sa.append(at)

        b = input("捨てるカード選択2:")
        bt = int(b) - 1

        if bt in sa:
            print("同じカード番号は選択できません")
        else:
            sa.append(bt)

        c = input("捨てるカード選択3:")
        ct = int(c) - 1

        if ct in sa:
            print("同じカードは選択できません")
        else:
            sa.append(ct)

        d = input("捨てるカード選択4:")
        dt = int(d) - 1

        if dt in sa:
            print("同じカードは選択できません")
        else:
            sa.append(dt)

        e = input("捨てるカード選択5:")
        et = int(e) - 1

        if et in sa:
            print("同じカードは選択できません")
        else:
            sa.append(et)

    except ValueError:
        print("")
        print("手札交換を終了します")
        print("")
    finally:
        return sa

def pat(cards,hand):
    """
    役を確定させる

    input
        cards:手札のカードを一つの文字列としたもの
        hand:手札のカードをそれぞれ配列にいれたもの
    output
        それぞれ役に対する数字が返却。
        もしくは、errorの文字列が返却

    """
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    point = 0
    cb = 0

    if re.search("♦10",cards) and re.search("♦J",cards) and re.search("♦Q",cards) and re.search("♦K",cards) and re.search("♦A",cards):
        return 10
    if re.search("♦10",cards) and re.search("♦J",cards) and re.search("♦Q",cards) and re.search("♦K",cards) and re.search("♦A",cards):
        return 10
    if re.search("♦10",cards) and re.search("♦J",cards) and re.search("♦Q",cards) and re.search("♦K",cards) and re.search("♦A",cards):
        return 10
    if re.search("♦10",cards) and re.search("♦J",cards) and re.search("♦Q",cards) and re.search("♦K",cards) and re.search("♦A",cards):
        return 10
    if re.search("10",cards) and re.search("J",cards) and re.search("Q",cards) and re.search("K",cards) and re.search("A",cards):
        return 4

    for w in hand:
        if re.search("♥",w):
            a_count += 1
        if re.search("♦",w):
            b_count += 1
        if re.search("♣",w):
            c_count += 1
        if re.search("♠",w):
            d_count += 1

    e_count = a_count + b_count + c_count + d_count
    if not e_count == 5:
        return "error"


    if a_count == 5 or b_count == 5 or c_count == 5 or d_count == 5:
        point += 5

    if not len(hand) == 5:
        return "error"

    try:
        r = re.compile(".([\dJQKA]+)"*5)
        g = r.match(cards).groups()
    except:
        return "error"

    jf = list(g)
    yu = []

    for s in jf:
        if s == "A" or s == "J" or s == "Q" or s == "K":
            ds = s.replace("A","1").replace("J","11").replace("Q","12").replace("K","13")
            es = int(ds)
            yu.append(es)

        else:
            ss = int(s)
            yu.append(ss)

    dd = sorted(yu)

    for a in dd:

        if cb == 0:
            cb += 1
            continue

        gf = cb - 1
        if a == dd[gf] + 1:
            if cb == 4:
                point += 4
            else:

                cb += 1
                continue

        else:
            break

    if point:
        return point

    pats = {
            (2, 3): 6,
            (1, 1, 3): 3,
            (1, 2, 2): 2,
            (1, 1, 1, 2): 1,
            (1, 4): 7,
            (1, 1, 1, 1, 1): 0
           }
    trumps = tuple(sorted(len(list(g)) for k, g in groupby(sorted(g))))
    return pats[trumps]

def count(point):
    """
    patで渡された数字を元に役を表示する

    input
        point:patで確定した数字
    output
        それぞれ点数に対する役が返却。

    """

    if point == 1:
        return "1ペア"
    elif point == 2:
        return "2ペア"
    elif point == 3:
        return "3カード"
    elif point == 6:
        return "フルハウス"
    elif point == 7:
        return "4ペア"
    elif point == 5:
        return "フラッシュ"
    elif point == 4:
        return "ストレート"
    elif point == 10:
        return "ロイヤルストレートフラッシュ"
    elif point == 9:
        return "ストレートフラッシュ"
    else:
        return "ブタ"

def main():
    deck = make_deck()
    hand = draw_from_deck(deck,[], 5)
    print("")
    print('初期手札:', hand)

    hand4 = draw_from_deck(deck, [], 5)

    ja = mulligan(hand)

    if ja:
        ja.sort(reverse=True)
        if ja[0] > 4:
            print("手札交換に失敗しました。システムを終了します")
            sys.exit()
        for pa in ja:
            hand.pop(pa)

        hand2 = draw_from_deck(deck, [],len(ja))
        hand = hand + hand2

    abc = ""
    cde = ""

    for a in hand:
        abc = abc + a

    for t in hand4:
        cde =  cde + t

    mypoint = pat(abc,hand)
    enemypoint = pat(cde,hand4)

    myhand = count(mypoint)
    enemyhand = count(enemypoint)

    print("")
    print("自分の手札:",hand)
    print("自分の手札の役は{}でした".format(myhand))
    print("")
    print("相手の手札:",hand4)
    print("相手の手札の役は{}でした".format(enemyhand))

    print("")
    print("-------------------------")
    if mypoint > enemypoint:
        print("|       You Win         |")
    elif mypoint < enemypoint:
        print("|       You Lose        |")
    else:
        print("|       Drow            |")
    print("-------------------------")

    print("")
    flag = input("もう一回遊びますか? [Yes/No]")
    if flag.lower() in ["y", "yes"]:
        check()

    print("終了")



if __name__ == '__main__':
    main()