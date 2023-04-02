"""
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").
The domain name part of an email address may only consist of letters, digits, hyphens and dots. 
The local part, however, also allows a lot of different special characters. 
Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

"""
def email_domain(input_email):

    # get the last accurence of the '@' symbol in the input email to split the local and domain parts.
    at_index = input_email.rfind("@")

    # Extract the domain part of the input email.
    domain = input_email[at_index+1:]

    """
    If the domain part contains a pair of double quotes, find the last
    occurrence of the "@" symbol before the quotes to extract the
    correct domain part
    """
    if '"' in domain:
        domain = domain[:domain.rfing('"')].split('"')
        domain = domain[at_index+1:]
    
    #
    return domain

print(email_domain("prettyandsimple@example.com"))

