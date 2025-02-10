#This program will scan an inputed email for keywords used in spam.
#If any keywords are found, they will be added to a score to be displayed.
#Any keyword used in the email will be displayed as well.

#tuple of spam keywords and phrases
keywords = ( "free", "big money", "info", "investment", "congratulations", "credit", "discount",
    "cheap", "chance", "deal", "cashback", "bank", "debt", "police", "cash subject",
    "avoid bankruptcy", "nigerian prince", "extra cash", "jail", "$", "hidden",
    "bonus", "billion", "satisfied", "win", "won", "secret", "special" )

#calculates the score based on keywords in the email
def scoreCalculator (email):
#initialzes the variables and list
    score = 0
    foundKeywords = []
#converts the email to lowercase to prevent keywords from not being caught
    email = email.lower()
#finds the keywords in email and adds the keyword to a list

    for keyword in keywords:
        if keyword in email:
            score += 1
            foundKeywords.append(keyword)

    return score, foundKeywords
#determines the possiblity of email being spam
def spamPercentage(score):
    if score == 0:
        return 'No spam detected'
    elif score <= 1:
        return 'Not likely spam'
    elif score <= 3:
        return 'Likely spam'
    else:
        return 'Definitely spam'
#gathers the information, then prints the  refined information
def main():
#prompts the user for the email
    email = input ('Please enter the email: ')

#calculates the spam score  and keywords
    score, foundKeywords = scoreCalculator(email)

#determines spam percentage
    likelihood = spamPercentage(score)

#displays the results
    print(f'Spam Score: {score}')
    print(f'Spam Likelihood: {likelihood}')
    print(f'Keywords found {foundKeywords}')

main()