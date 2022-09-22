########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed

import random
def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play = input('Play again? enter Y or yes to play more, N or no to stop')
    while play != 'N' and play != 'No' and play != 'nO':
        if play == 'Y' or play == 'yes' or play == 'Yes' or play == 'yEs' or play == 'yeS':
            return True
        elif play == 'N' or play == 'No' or play == 'nO':
            return False
        else:
            print('Invalid response, please try again')
            play = input('Play again? enter Y or yes to play more, N or no to stop')
     
def get_wager(bank):
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input('How many chips would you like to wager? '))
    if wager <= 0 or wager > bank:
        print('Please enter a valid amount, between zero and', bank)
        wager = int(input('How many chips would you like to wager? '))
    return wager         

def get_slot_results():
    ''' Returns the result of the slot pull '''
    reel1 = random.randrange(1,10)
    reel2 = random.randrange(1,10)
    reel3 = random.randrange(1,10)
    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc):
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0

def get_bank():
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input('How many chips do you have today? '))
    while bank <= 0 or bank > 100:
        print('please input a number between 1 and 100')
        bank = int(input('How many chips do you have today? '))
    return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched,
3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3 or matches == 2:
        payout = matches * wager
    else:
        payout = wager - (2 * wager)
    return payout


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        bankPrime = bank
        spins = 0
        most = bank
        while bank > 0:  
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spins += 1
            if bank > most:
                most = bank
        print("You lost all", bankPrime, "in", spins, "spins")
        print("The most chips you had was", most)
        playing = play_again()
