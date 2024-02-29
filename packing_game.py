max_weight = 80
max_items = 6




class item:
     def __init__(self,weigth,name):
          self.weight = weigth
          self.name = name

     def print(self):
          print(self.name , self.weight)


class tech_item(item):
     def __init__(self, weigth,name,brand):
          super().__init__(weigth,name)
          self.brand = brand

class Passport(item):
     def __init__(self, weigth,name,color,cost,bought_from):
          super().__init__(weigth,name) 
          self.color = color 
          self.cost = cost
          self.bought_from = bought_from

class Sunglasses(item):
     def __init__(self, weigth,name,haveCase,color,origin):
          super().__init__(weigth,name)
          self.haveCase = haveCase
          self.color = color 
          self.origin = origin

class Sneakers(item):
     def __init__(self, weigth,name,brand,new,bought_from):
          super().__init__(weigth,name)
          self.brand = brand 
          self.new = new
          self.bought_from = bought_from
          
class SmartPhone(tech_item):
     def __init__(self, weigth,name, brand,os,storage,display,camera,
                   materials):
          super().__init__(weigth,name, brand) 
          self.os = os
          self.storage = storage
          self.display = display
          self.camera = camera   
          self.materials = materials


class Laptop(tech_item):
     def __init__(self, weigth,name, brand,processor,RAM,storage,graphics):
          super().__init__(weigth,name, brand)
          self.processor = processor
          self.RAM = RAM
          self.storage = storage
          self.graphics = graphics
            
class SmartWatch(tech_item):
     def __init__(self, weigth,name, brand,display,battery_life,fitness_features,connectivity):
          super().__init__(weigth,name, brand)
          self.display = display
          self.battery_life = battery_life
          self.fitness_features = fitness_features
          self.connectivity = connectivity
            
class Campus(tech_item):
     def __init__(self, weigth,name, brand, accuracy, price, materials):
          super().__init__(weigth,name, brand)
          self.accuracy = accuracy
          self.price = price
          self.materials = materials


class UniversalCharger(tech_item):
     def __init__(self, weigth,name, brand,color,price,size):
          super().__init__(weigth,name, brand)
          self.color = color
          self.price = price
          self.size = size

universal_charger = UniversalCharger(12,'universal charger','Lenovo','black',50,'Medium')
passport = Passport(1,'passport','blue',50,'USA')
sunglasses = Sunglasses(10,'sunglasess','yes','black','italy')
sneakers = Sneakers(14,'sneakers','New balance',False,'Spain')
smartPhone = SmartPhone(2,'smartphone','Apple','IOS',128,'AMOLED','Dual Lens','lithium, plastic')
laptop = Laptop(60,'Laptop','Dell','Intel i7',16, 512,'NVIDIA GeForce4')
smartWatch = SmartWatch(44,'smartwatch','Samsung','touchscreen','3 days', 'heart rate monitor','Blutooth' )
campus = Campus(4, 'campus', 'Samsung','high',50,'iron,plastic')


class bag:
    def __init__(self,curr_weight,items_num,max_weight,max_items,items_list):
       self.curr_weight = curr_weight
       self.items_num = items_num
       self.max_weight = max_weight
       self.max_items = max_items
       self.items_list = items_list
    
    def add_item(self, item):
        if item.weight + self.curr_weight <= self.max_weight and 1 + self.items_num <= self.max_items:
            self.items_list.append(item)
            self.curr_weight += item.weight
            self.items_num += 1
            print('The item was added successfully')
        elif self.items_num > self.max_items:
             print('The item limit is surpassed!')
        if self.curr_weight >= self.max_weight:
             print('The weight limit is surpassed!')

    def remove_item(self, item):
            if item in self.items_list: 
                self.items_list.remove(item)
                self.curr_weight -= item.weight
                self.items_num -= 1
                print('The item was removed successfully')

            else :
                 print("The item doesn't exist in the list")

    def print_all_items(self):
         for item in self.items_list:
              item.print()
    def print_all_items_by_category(self):
         tech_list = []
         others = []
         for item in self.items_list:
              if issubclass(type(item),tech_item):
                   tech_list.append(item)
              else:
                   others.append(item)
         print('***** Tech items *****')
         for item in tech_list:
              item.print()
         print('\n')

         print('******* Others *******')
         for item in others:
              item.print()          
         print('\n')

    def print_all_items_by_given_category(self,category):
         for item in self.items_list:
              if issubclass(type(item),category):
                   item.print()





# ********************************************************************

items = {1:universal_charger,
         2:passport,
         3:sunglasses,
         4:sneakers,
         5:smartPhone,
         6:laptop,
         7:smartWatch,
         8:campus}


mainBag = bag(0,0,max_weight,max_items,[])


while(True):
    x = input("To add an item to the bag enter 'a' to remove an item enter 'r':"  )
    if x=='a':
         n = int(input('Please choose one item from the list to add to the bag, for example if you want to choose sunglasses enter 3: '))
        #  print(items)
         mainBag.add_item(items[n])
    elif x == 'r':
         n = int(input('Please choose one item from the list to remove from the bag, for example if you want to choose sunglasses enter 3: '))
        #  print(items)
         mainBag.remove_item(items[n])

    else: 
         print("Invalid Input!")
    
    mainBag.print_all_items_by_category()
    x= input("If you are done press 'd' else press 'Enter: ")
    if x == 'd':
         break
    else:
         continue
    
    


         
        
    