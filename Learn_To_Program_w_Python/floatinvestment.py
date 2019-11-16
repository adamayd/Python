# Have user enter investment amount and expected interest
investment, interest = input('Enter your annual investment and interest rate: ').split()
investment = float(investment)
interest = float(interest) * .01

# Calculate each year investment + total investment * interest rate
annual_total = (investment * interest) + investment
# print('Year 1 total is {:.2f} with an investment of {:.0f} at {:.2f}% interest'.format(annual_total, investment, interest))
for i in range(1,11):

    print('Year {} total is {:.2f} with an investment of {:.0f} at {:.2f}% interest'.format(i, annual_total, investment, (interest * 100)))

    annual_total = (annual_total * interest) + investment + annual_total


    # Print out the earnings after a 10 year period.