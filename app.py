import json
from flask import Flask, render_template, request
api = Flask(__name__, template_folder='back/templates')


cars = []
cars_file = 'cars.json'

try:
    with open(cars_file, 'r') as file:
        cars = json.load(file)
except FileNotFoundError:
    cars=[]








@api.route('/')
def hello():
    return 'Hello, World!'

@api.route('/welcome')
def welcome():
    return render_template('welcome.html')




@api.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        color= request.form.get('color')
        Brand = request.form.get('Brand')
        model = request.form.get('model')
        licencenumber = request.form.get('licencenumber')
       
        for car in cars : 
            if car.get("licencenumber")==licencenumber:
                errormsg ='licencenumber is allready registered'
                return render_template('welcome.html',errormsg= errormsg)
            
        new_car = {'licencenumber': licencenumber, 'Brand': Brand, 'color': color, 'model': model}
        cars.append(new_car)


        with open(cars_file, 'w') as file:
    # Use json.dump() to write the data to the file
            json.dump(cars, file)

        # Add your signup logic here
        # Example: Store the car information in a database

        return render_template('welcome.html')
    


    return render_template('signup.html')



@api.route('/login', methods=['GET', 'POST'])
def login():
    global cars
    print(cars)
    
    
    if request.method == 'POST':
        print("ssssssssssssss")
        req_licencenumber = request.form['licencenumber']
        req_Brand = request.form['Brand']
        print("req_licencenumber")
        print("req_Brand")
        for car in cars:
            if (req_licencenumber == car['licencenumber']  and  car['Brand'] == req_Brand):
                return render_template('welcome.html')
        return render_template('login.html')
    else:
        return render_template('login.html')



if __name__ == '__main__':
    api.run(debug=True)