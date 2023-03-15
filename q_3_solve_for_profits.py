print("Three friends start a business and decide to split the profits equally. Jim invests $2,000, Mary invests $3,000, and Sally invests $5,000. If the profits are $3,000, how much of the profits would Sally receive if the profits were divided proportional to how much each friend invested?")

jim_investment = 2000
mary_investment = 3000
sally_investment = 5000

profits = 3000


# Plug in the amount that each of them invested. Divide each part by a common factor which is 1,000.
# ratio = investment/1000 (common factor)

jim_ratio = jim_investment/1000
mary_ratio = mary_investment/1000
sally_ratio = sally_investment/1000

print(f"Jim's ratio, Mary's ratio, and Sally's ratio {jim_ratio}:{mary_ratio}:{sally_ratio}")

# Add the parts of the ratio

add_ratio = jim_ratio+mary_ratio+sally_ratio
print(add_ratio)

#Divide profits by 10

profits_divided_by_the_total_ratio = profits/10

jim_profits = jim_ratio * profits_divided_by_the_total_ratio
mary_profits = mary_ratio * profits_divided_by_the_total_ratio
sally_profits = sally_ratio * profits_divided_by_the_total_ratio
total_profits = jim_profits+mary_profits+sally_profits

print(f"jim_profits {jim_profits} USD")
print(f"Mary profits {mary_profits} USD")
print(f"Sally profits {sally_profits} USD")
print(f"For the total of {total_profits} USD")



