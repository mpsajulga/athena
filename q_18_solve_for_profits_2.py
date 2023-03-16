print("Three friends start a business and decide to split the profits equally. Susan invests $6,000, John invests $4,000, and Pria invests $7,000. If the profits are $12,000, how much of the profits would Pria receive if the profits were divided proportional to how much each friend invested?")

susan_investment = 6000
john_investment = 4000
pria_investment = 7000

profits = 12000


# Plug in the amount that each of them invested. Divide each part by a common factor which is 1,000.
# ratio = investment/1000 (common factor)

susan_ratio = susan_investment/1000
john_ratio = john_investment/1000
pria_ratio = pria_investment/1000

print(f"Susan's ratio, John's ratio, and Pria's ratio {susan_ratio}:{john_ratio}:{pria_ratio}")

# Add the parts of the ratio

add_ratio = susan_ratio+john_ratio+pria_ratio
print(add_ratio)

#Divide profits by the total ratio

profits_divided_by_the_total_ratio = profits/add_ratio

susan_profits = susan_ratio * profits_divided_by_the_total_ratio
john_profits = john_ratio * profits_divided_by_the_total_ratio
pria_profits = pria_ratio * profits_divided_by_the_total_ratio
total_profits = susan_profits + john_profits + pria_profits

print(f"Susan profited {susan_profits} USD")
print(f"John profited {john_profits} USD")
print(f"Pria profited {pria_profits} USD")
print(f"For the total of {total_profits} USD")



