import random
import sys
import re


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
    手札を確定する

    input
        deck:make_deckの配列
        hand:手札を入れる配列。基本的に空
        n:引く枚数。指定がなければ1枚
    output
        hand:引いた後の手札

    """

    for i in range(n):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)

    return hand

def pat(cards,card_hands=1):
    """
    点数を確定する

    input
        card:手札にある各カード
        card_hands:手札の枚数
    output
        total:手札に応じた点数

    """

    total = 0
    A_count = 0

    r = re.compile(".([\dJQKA]+)"* card_hands)
    card_groups = r.match(cards).groups()

    card_role = list(card_groups)

    for s in card_role:

        if s == "J" or s == "Q" or s == "K":
            picture_card = s.replace("J","10").replace("Q","10").replace("K","10")
            int_picture_card = int(picture_card)
            total = int_picture_card + total
        elif s == "A":
            picture_card = s.replace("A","11")
            int_picture_card = int(picture_card)
            total = int_picture_card + total
            A_count += 1
        else:
            number = int(s)
            total = number + total


    if total > 21 and A_count > 0 :

        for i in range(A_count):

            if total > 21:
                total -= 10

    if total > 21:
        return total

    return total

def is_continue():
    """
    カードを追加して引くかを確認する

    output
        Trueならもう一枚引く。
        Falseなら追加しない。

    """

    while True:
        flag = input("もう一枚引きますか? [Yes/No]")
        if flag.lower() in ["y", "yes"]:
            return True
        if flag.lower() in ["n", "no"]:
            return False
        if flag.lower() in ["q", "quit"]:
            sys.exit()
        print("Invalid value. Please input yes or no.")


def main():
    deck = make_deck()
    hand = draw_from_deck(deck,[], 2)
    print("")
    print('プレイヤー初期手札:', hand)

    hand4 = draw_from_deck(deck, [], 1)

    print('ディーラー初期手札:', hand4)
    print("")

    abc = ""
    cde = ""

    i = 0
    w = 0

    for a in hand:
        abc = abc + a
        i += 1

    mypoint = pat(abc,i)
    enemypoint = pat(cde,w)

    while True:

        if not is_continue():
            print("")
            break

        hand2 = draw_from_deck(deck,[], 1)
        hand = hand + hand2

        dew = ""
        c = 0

        for t in hand:
            dew =  dew + t
            c += 1

        mypoint = pat(dew,c)
        print("")
        print("プレイヤーの手札",hand)

        if mypoint > 21:
            print("----------------------------------------------")
            print("|       プレイヤーはバーストしました         |")
            print("----------------------------------------------")

            print("")
            flag = input("もう一回遊びますか? [Yes/No]")
            if flag.lower() in ["y", "yes"]:
                check()

            sys.exit()


    print("----------------------------------------------")
    print('ディーラー初期手札:', hand4)
    print("")

    while enemypoint < 17:

        w = 0
        cde = ""

        hand5 = draw_from_deck(deck,[], 1)
        hand4 = hand4 + hand5

        for t in hand4:

            cde =  cde + t
            w += 1

        enemypoint = pat(cde,w)

        print("ディーラーは追加で手札を引きました")
        print("手札:{}".format(hand4))
        print("")


    if enemypoint > 21:
        print("----------------------------------------------")
        print("|       ディーラーはバーストしました         |")
        print("----------------------------------------------")

        print("")
        flag = input("もう一回遊びますか? [Yes/No]")
        if flag.lower() in ["y", "yes"]:
            check()
        sys.exit()

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