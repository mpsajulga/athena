print("An electrician has 350 clients. If the electrician can see 5 clients per day; how many days will it take for him to see 30% of his clients?")

clients = int(input("Total clients: ")) #350
number_of_clients_per_day = int(input("Total number of clients that he can see per day: ")) # 5
percentage_of_clients_he_needs_to_see = float(input("Percentage of clients that he needs to see:__%: ")) #30%
percent_to_decimal = percentage_of_clients_he_needs_to_see/100

print(percent_to_decimal)
#multiply

thirty_percent_clients = int(clients * percent_to_decimal)

print(f"30% of his clients is equal to {thirty_percent_clients} clients.")

#divide

total_of_days = thirty_percent_clients / number_of_clients_per_day

print(f"The electrician will take {total_of_days} to see {thirty_percent_clients}% of his clients.")