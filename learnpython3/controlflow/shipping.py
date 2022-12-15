weight = 41.5

# Ground shipping
cost_ground = 0
premium_cost_ground = 125.00

if weight <= 2:
  cost_ground = weight * 1.5 +20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20
elif weight > 10:
  cost_ground = weight * 4.75 +20

print(cost_ground)

#Drone Shipping

cost_drone = 0
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00 
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00 
elif weight > 10:
  cost_drone = weight * 14.25

print(cost_drone)