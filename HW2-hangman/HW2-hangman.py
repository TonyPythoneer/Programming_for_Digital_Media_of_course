# -*- coding:UTF-8 -*-
#================================
#Question:
#  Part 1: The overall goal
#  Part 2: The approach
#  Part 3: Designing
#  Part 4: Hints (Functions)
#  Part 5: Hints (special string functions)
#  Part 6: Finished?
#  Part 7: A very big hint
#=================================


def guess_a_letter(now_alphabet_table):
    #防呆裝置，限玩家猜測一個字
    only_a_letter = False
    while not only_a_letter :
        guess = raw_input("Please guess a letter:")
        #確實輸入一個字母
        if len(guess) == 1 :
            guess = guess.upper()
            #確實是還未猜過的字母
            if guess in now_alphabet_table :
                only_a_letter = True
                alphabet_index = now_alphabet_table.index(guess)
                now_alphabet_table[alphabet_index] = ' '
                return guess,now_alphabet_table
            else :
                print "Error!已經使用過了!"
        else :
            print "Error!Only a letter!"

#初始化並建立字母列表--供使用者猜測
def build_alphabet_table():
    table = []
    for i in range(65,65+26):
        table.append(chr(i))
    return table

#展開字母列表--供使用者猜測目前能猜的字母
def display_alphabet_table(table):
    print "==================="
    print "= alphabet  table ="
    print "==================="
    for i in [0,10,20] :
        print ' '.join(table[i:i+10])
    print "==================="


#檢查是否該字母有在密語中
def check(guess,correct_word):
    if guess in correct_word :
        i=0
        num = 0
        while i < len(correct_word):
            if correct_word[i] == guess_letter :
                hide_word[i] = guess_letter
                num = num + 1
            i = i + 1
        msg1_guess_result = "You guessed '" + guess + "'. " + str(num) + " '" +  guess + "'s in the word Guess the word: "
        msg2_upgrade_word = ' '.join(hide_word)
        msg3_guesses_left = " (" + life + " guesses left)"
        #You guessed 'E'. 2 'E's in the word Guess the word: _ E _ E _ _ (5 guesses left)
        print "猜對 " + str(num) + "個!"
        print ' '.join(hide_word)
    else :
        life = life - 1

#建置隱藏答案
def encrypt(string):
    encryption = []
    for i in range(0,len(string)):
        encryption.append('_')
    return encryption

#
def sketch_hungman(life):
    man = hangman()
    print ""
    print "　　＋－－－－－＋　"
    print "　　｜　　　　　｜　"
    print "　　｜　　　　　" + man.head(life)
    print "　　｜　　　　" + man.left_hand(life) + man.body(life) + man.right_hand(life)
    print "　　｜　　　　" + man.left_leg(life) + "　" + man.right_leg(life)
    print "　　｜　　"
    print "　口口口　"
    print "口口口口口"
    print ""

#類別--吊死鬼
class hangman() :
    def head(self,integer):
        if integer <= 5 :
            return "Ｏ"
        return "　"
    def body(self,integer):
        if integer <= 4 :
            return "｜"
        return "　"
    def left_hand(self,integer):
        if integer <= 3 :
            return "－"
        return "　"
    def right_hand(self,integer):
        if integer <= 2 :
            return "－"
        return "　"
    def left_leg(self,integer):
        if integer <= 1 :
            return "／"
        return "　"
    def right_leg(self,integer):
        if integer <= 0 :
            return "＼"
        return "　"


#main start
if __name__ == '__main__':
    # == 初始值設定 ==
    game_over = False
    life      = 6
    # == 初始化 開始 ==
    # 1.建立字母表
    alphabet_table = build_alphabet_table()
    # 2.建立正確答案和隱藏答案
    correct_word = raw_input("Enter secret word:")
    correct_word = correct_word.upper()
    hidden_word  = encrypt(correct_word)
    # 3.遊戲訊息開始
    print "Game start!"
    print "Guess a letter: " + ' '.join(hidden_word) + " (6 guesses left)"
    # == 初始化 結束 ==
   #進入遊戲迴圈
    while ( not game_over ) and ( life != 0 ) :
        print "=================================================================="
        sketch_hungman(life)
        display_alphabet_table(alphabet_table)
        guess_letter , alphabet_table = guess_a_letter(alphabet_table)
        
        guess = guess_letter
        hide_word = hidden_word

        if guess in correct_word :
            i=0
            num = 0
            while i < len(correct_word):
                if correct_word[i] == guess_letter :
                    hide_word[i] = guess_letter
                    num = num + 1
                i = i + 1
            #correct msg
            msg1_guess_result = "You guessed '" + guess + "'. " + str(num) + " '" +  guess + "'s in the word Guess the word: "
            msg2_upgrade_word = ' '.join(hide_word)
            msg3_guesses_left = " (" + str(life) + " guesses left)"
            print msg1_guess_result + msg2_upgrade_word + msg3_guesses_left
        else :
            life = life - 1
            #error msg
            msg1_guess_result = "You guessed '" + guess + "'. No '" +  guess + "' in the word ! Guess the word: "
            msg2_upgrade_word = ' '.join(hide_word)
            msg3_guesses_left = " (" + str(life) + " guesses left)"
            print msg1_guess_result + msg2_upgrade_word + msg3_guesses_left
        hidden_word = hide_word

        if correct_word == ''.join(hidden_word) :
            game_over = True
            print "Congratulations!You win!"
        if life == 0 :
            sketch_hungman(life)
            print "Hangman die!You lose!"
