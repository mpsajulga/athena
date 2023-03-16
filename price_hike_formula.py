original_price = int(input("Input Original Price: "))
initial_price_hike = int(input("Input initial price hike in percent: ")) #0.3 #rate of increase
initial_price_hike = initial_price_hike/100
additional_price_hike = int(input("Input additional price hike: "))


initial_hike = (original_price*initial_price_hike)+original_price

print(f"The initial price hike is {initial_hike} USD.")

total_hike = initial_hike + additional_price_hike

print(f"The additional price hike amounts to {total_hike} USD.")

#find the total price increase 

total_price_increase = total_hike - original_price

#find the percentage

total_percent = int((total_price_increase/original_price)*100)

print(f"The price goes up to {total_percent} percent of its original price.")

