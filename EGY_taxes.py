class Calc_taxes:
    # Personal exemption
    exemption = 7000

    def get_year_salary(self, month_salary):
        return month_salary * 12

    def get_category(self, year_salary):
        if year_salary > 0 and year_salary <= 8000:
            return 1
        elif year_salary > 8000 and year_salary <= 30000:
            return 2
        elif year_salary > 30000 and year_salary <= 45000:
            return 3
        elif year_salary > 45000 and year_salary <= 200000:
            return 4
        else:
            return 5 

    def get_1st_category_tax(self, salary_tax):
        # reduce first category difference from salary
        salary_tax[0] -= 8000
        return salary_tax


    def get_2nd_category_tax(self, salary_tax):
        if salary_tax[0]-22000 > 0:
            salary_tax[0] -= 22000
            salary_tax[1] += (22000*0.1)
        else:
            salary_tax[1] += (salary_tax[0]*0.1)
            salary_tax[0] = 0
        return salary_tax


    def get_3ed_category_tax(self, salary_tax):
        if salary_tax[0] - 15000 > 0:
            salary_tax[0] -= 15000
            salary_tax[1] += (15000*0.15)
        else:
            salary_tax[1] += (salary_tax[0]*0.15)
            salary_tax[0] = 0
        return salary_tax


    def get_4th_category_tax(self, salary_tax):
        if salary_tax[0] - 155000 > 0:
            salary_tax[0] -= 155000
            salary_tax[1] += (155000*0.2)
        else:
            salary_tax[1] += (salary_tax[0]*0.2)
        return salary_tax


    def get_5th_category_tax(self, salary_tax):
        salary_tax[1] += (salary_tax[0]*0.225)
        return salary_tax


    def tax_per_month(self, month_salary):
        year_salary = self.get_year_salary(month_salary)
	
	# reduce personal exemption
        year_salary -= self.exemption
        category = self.get_category(year_salary)

        print(category) 
        salary_tax = [year_salary, 0]

        if category == 1:
            return 0

        elif category == 2:
            salary_tax = self.get_1st_category_tax(salary_tax)
            salary_tax = self.get_2nd_category_tax(salary_tax)
            # calc category reduction 
            salary_tax[1] -= (salary_tax[1]*0.85)

        elif category == 3:
            salary_tax = self.get_1st_category_tax(salary_tax)
            salary_tax = self.get_2nd_category_tax(salary_tax)
            salary_tax = self.get_3ed_category_tax(salary_tax)
            # calc category reduction
            salary_tax[1] -= (salary_tax[1]*0.45)

        elif category == 4:
            salary_tax = self.get_1st_category_tax(salary_tax)
            salary_tax = self.get_2nd_category_tax(salary_tax)
            salary_tax = self.get_3ed_category_tax(salary_tax)
            salary_tax = self.get_4th_category_tax(salary_tax)
            # calc category reduction
            salary_tax[1] -= (salary_tax[1]*0.075)

        elif category == 5:
            salary_tax = self.get_1st_category_tax(salary_tax)
            salary_tax = self.get_2nd_category_tax(salary_tax)
            salary_tax = self.get_3ed_category_tax(salary_tax)
            salary_tax = self.get_4th_category_tax(salary_tax)
            salary_tax = self.get_5th_category_tax(salary_tax)
        
        

        # return salary tax per month
        return salary_tax[1]/12

if __name__ == "__main__":
    #cc = Calc_taxes()
    print(Calc_taxes().tax_per_month(5000))
    print(Calc_taxes().tax_per_month(7000))  
    print(Calc_taxes().tax_per_month(3000)) 
