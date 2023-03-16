print("A car originally costs $30,000. Its price went up by 30% and then by another $6,000. How much did the price go up as a percentage of the original price?")

original_price = 30000
initial_price_hike = 0.3 #rate of increase
additional_price_hike = 6000


initial_hike = (original_price*initial_price_hike)+original_price

print(f"The initial price hike is {initial_hike} USD.") #39k

total_hike = initial_hike + additional_price_hike

print(f"The additional price hike amounts to {total_hike} USD.") #45k

#find the total price increase 

total_price_increase = total_hike - original_price #32k-24k

#find the percentage

total_percent = int((total_price_increase/original_price)*100)

print(f"The price goes up to {total_percent} percent of its original price.")
