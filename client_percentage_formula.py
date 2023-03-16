clients = int(input("Total clients: "))
number_of_clients_per_day = int(input("Total number of clients that he can see per day: "))
percentage_of_clients_he_needs_to_see = int(input("Percentage of clients that he needs to see:__%: "))
percent_to_decimal = percentage_of_clients_he_needs_to_see/100

#multiply

percentage_of_clients = int(clients * percent_to_decimal)

print(f"{percentage_of_clients_he_needs_to_see}% of his {clients} clients is {percentage_of_clients}.")

#divide

total_of_days = int(percentage_of_clients / number_of_clients_per_day)

print(f"The electrician will take {total_of_days} days to see {percentage_of_clients_he_needs_to_see}% of his clients.")

