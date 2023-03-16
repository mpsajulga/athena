print("A doctor has 175 patients. If the doctor can see 10 patients per day; how many days will it take for him to see 40% of his patients?")

clients = int(input("Total clients: ")) #175
number_of_clients_per_day = int(input("Total number of clients that he can see per day: ")) # 10
percentage_of_clients_he_needs_to_see = int(input("Percentage of clients that he needs to see:__%: ")) #40%
percent_to_decimal = percentage_of_clients_he_needs_to_see/100

#multiply

percentage_of_clients = int(clients * percent_to_decimal)

print(f"{percentage_of_clients_he_needs_to_see}% of his {clients} patients is {percentage_of_clients} clients.")

#divide

total_of_days = int(percentage_of_clients / number_of_clients_per_day)

print(f"The electrician will take {total_of_days} days to see {percentage_of_clients_he_needs_to_see}% of his clients.")
