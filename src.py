from tkinter import * 

Calculation = "" 

def press(symbol): 
	global Calculation 
	Calculation += str(symbol) 
	equation.set(Calculation) 
 
def equals(): 
	try: 

		global Calculation 
		Calculation = str(eval(Calculation)) 

		equation.set(Calculation) 

	
		Calculation = "" 


	except: 

		equation.set(" error ") 
		Calculation = "" 


 
def clear(): 
	global Calculation 
	Calculation = "" 
	equation.set("") 


# Driver code 
if __name__ == "__main__": 
	root = Tk() 
	root.configure(background="gray") 
	root.title("Simple Calculator") 
	root.geometry("460x275") 
	equation = StringVar() 
	Calculation_field = Entry(root, textvariable=equation, font= 24 ) 
	Calculation_field.grid(columnspan=4, ipadx=120, ipady=20)
	
# appearance

	button1 = Button(root, text=' 1 ', fg='white', bg='black', font= 20,
					command=lambda: press(1), height=1, width=9) 
	button1.grid(row=2, column=0) 

	button2 = Button(root, text=' 2 ', fg='white', bg='black', font= 20,
					command=lambda: press(2), height=1, width=9) 
	button2.grid(row=2, column=1) 

	button3 = Button(root, text=' 3 ', fg='white', bg='black', font= 20,
					command=lambda: press(3), height=1, width=9) 
	button3.grid(row=2, column=2) 

	button4 = Button(root, text=' 4 ', fg='white', bg='black', font= 20,
					command=lambda: press(4), height=1, width=9) 
	button4.grid(row=3, column=0) 

	button5 = Button(root, text=' 5 ', fg='white', bg='black', font= 20,
					command=lambda: press(5), height=1, width=9) 
	button5.grid(row=3, column=1) 

	button6 = Button(root, text=' 6 ', fg='white', bg='black',font= 20, 
					command=lambda: press(6), height=1, width=9) 
	button6.grid(row=3, column=2) 

	button7 = Button(root, text=' 7 ', fg='white', bg='black',font= 20, 
					command=lambda: press(7), height=1, width=9 )
	button7.grid(row=4, column=0) 

	button8 = Button(root, text=' 8 ', fg='white', bg='black', font= 20,
					command=lambda: press(8), height=1, width=9) 
	button8.grid(row=4, column=1) 

	button9 = Button(root, text=' 9 ', fg='white', bg='black', font= 20,
					command=lambda: press(9), height=1, width=9) 
	button9.grid(row=4, column=2) 

	button0 = Button(root, text=' 0 ', fg='white', bg='black', font= 20,
					command=lambda: press(0), height=1, width=9) 
	button0.grid(row=5, column=0) 

	plus = Button(root, text=' + ', fg='white', bg='black', font= 20,
				command=lambda: press("+"), height=1, width=9) 
	plus.grid(row=2, column=3) 

	minus = Button(root, text=' - ', fg='white', bg='black', font= 20,
				command=lambda: press("-"), height=1, width=9) 
	minus.grid(row=3, column=3) 

	multiply = Button(root, text=' * ', fg='white', bg='black', font= 20,
					command=lambda: press("*"), height=1, width=9) 
	multiply.grid(row=4, column=3) 

	divide = Button(root, text=' / ', fg='white', bg='black', font= 20,
					command=lambda: press("/"), height=1, width=9) 
	divide.grid(row=5, column=3) 

	equal = Button(root, text=' = ', fg='white', bg='black', font= 20,
				command=equals, height=1, width=9) 
	equal.grid(row=5, column=2) 

	clear = Button(root, text='Clear', fg='white', bg='black', font= 20,
				command=clear, height=1, width=9) 
	clear.grid(row=5, column='1') 

	Decimal= Button(root, text='.', fg='white', bg='black', font= 20,
					command=lambda: press('.'), height=1, width=9) 
	Decimal.grid(row=6, column=0) 

    
     
	root.mainloop() 

