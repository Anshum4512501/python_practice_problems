
class OuterClass(object):

	def __init__(self,out_var_one,out_var_two):
	
		self.out_var_one =out_var_one
		self.out_var_two =out_var_two
		print(self.show())

	def show(self):
		
		print(str(self.out_var_one) + " , " +str(self.out_var_two))	

	class InnerClass:

		def __init__(self,inner_var_one,inner_var_two):

			self.inner_var_one = inner_var_one
			self.inner_var_two = inner_var_two

		def show(self):
		
			print(str(self.inner_var_one) + " , " +str(self.inner_var_two))

inner_object_one = OuterClass(2,3).InnerClass(3,5)


print(inner_object_one.show())		

from datetime import datetime, timedelta

current_datetime = datetime.now()

# future dates
one_year_future_date = current_datetime + timedelta(days=365)

print('Current Date:', current_datetime)
print('One year from now Date:', one_year_future_date)

# past dates
three_days_before_date = current_datetime - timedelta(days=3)
print('Three days before Date:', three_days_before_date)

print(current_datetime.time()+timedelta(hour=1))