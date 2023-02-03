class ROI_Calculator:

    def income(self):
        print("The first thing to do is calculate your total monthly income.")
        rental_income = int(input("\nWhat is the rental income?\n\n"))
        laundry = int(input("\nDo you have any laundry income? If so, how much?\n\n"))
        storage = int(input("\nWhat amount of storage income do you have?\n\n"))
        misc = int(input("\nAre there any other sources of income? If so, what is the total from all other sources?\n\n"))
        total_income = (rental_income + laundry + storage + misc)
        print(f"Your total monthly income is ${total_income}")
    
    def expenses(self):
        print("Now we need to go over your monthly expenses.")
        tax = int(input("\n How much do you pay in taxes? \n\n"))
        insurance = int(input("\n How much does insurnace cost? \n\n"))
        print("The next few questions will cover the utilities. Enter $0 if any do not apply to you.")
        electric = int(input("\n What is the average of your electric bill? \n\n"))
        water = int(input("\n What is the average of your water bill? \n\n"))
        sewer = int(input("\n What is the average of your sewage bill? \n\n"))
        garbage = int(input("\n How much do you pay for garbage? \n\n"))
        gas = int(input("\n What is the average cost for gas?\n\n"))
        print("Okay. Now we will look at other home expenses.")
        hoa = int(input("\n Do you have any HOA fees? If so, how much? \n\n"))
        lawn_snow = int(input("\n Do you pay for lawn/snow care? If so, how much? \n\n"))
        vacancy = int(input("\n Do you set money aside for vacancy? If so, how much? *TIP- a good rule of thumb is to set aside 5 percent of the rental income for this* \n\n"))
        repairs = int(input("\n How much money is spent on any repairs? *TIP- putting $100 a month aside is a good rule-of-thumb* \n\n"))
        cap_ex= int(input("\n How much money is put aside for capital expenditures? *TIP- putting $100 aside for this is a good rule-of-thumb* \n\n"))
        property_management = int(input("\n How muchh is spent on propery management? \n\n"))
        mortgage = int(input("\n Last but not least, how much is the mortgage? \n\n"))
        total_expenses = (tax + insurance + electric + water + sewer + garbage + gas + hoa + lawn_snow + vacancy + repairs + cap_ex + property_management + mortgage)
        print(f"Your total month expenses is ${total_expenses}")
    
    def cash_flow(self, total_income, total_expenses):
        self.total_income = total_income
        self.total_expenses = total_expenses 
        total_cash_flow = (total_income - total_expenses)
        print(f"Based off your answers, your total monthly cash flow is {total_cash_flow}")
        annual_cash_flow = (total_cash_flow * 12)
        print(f"Looking at your monthly cash flow, your annual cash flow is calculated to be ${annual_cash_flow}")

    def invesments(self):
        print("Now we're going to go over the money you put into the rental property.")
        down_payment = int(input("\n What amount did you put towards the down payment? \n\n"))
        closing_costs = int(input("\n What amount did you put towards the closing costs? \n\n"))
        repair_money = int(input("\n What amount did you put towards repairs? \n\n"))
        other = int(input("\n Are there any other expenses you put forth? \n\n"))
        total_investment =(down_payment + closing_costs + repair_money + other)
        print(f"Basef off what you answered, your total invesment is ${total_investment}")

    def cash_on_cash(annual_cash_flow, total_investment):
        cash_on_cash = ((annual_cash_flow / total_investment) *100 )
        print(f"We have calculated your ROI! Based off your answers, your cash on cash Return On Investment is {cash_on_cash}%")

    def run(self):
        while True:
            ask = input("Welcome to the ROI Calculator! If you're interested in seeing what your Return On Investment is for your rental property, enter 'Y' to continue, otherwise enter 'N'.")
            if ask == 'Y':
                self.income()
                self.expenses()
                self.cash_flow()
                self.invesments()
                self.cash_on_cash()
            elif ask == 'N':
                print("Have a nice day! Come back soon.")
            else:
                print("Invalid answer. Enter 'Y' or 'N'.")

roi = ROI_Calculator()

roi.run()

        






        

