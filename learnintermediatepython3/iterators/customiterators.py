class CustomerCounter:
# Write your code below:
  def __iter__(self):
    self.count = 0
    return self

  def __next__(self):
    self.count += 1
    if self.count > 100:
      raise StopIteration

    return self.count

customer_counter = CustomerCounter()

for customer in customer_counter:
  print(customer)