# AirBnB_clone - Console to manage the models of an AirBnB-like application.
Welcome to the Airbnb Clone project, a console built from scratch. In this project, I created an application similar to Airbnb that allows users to search, create and manage models.
![815046647d23428a14ca](https://user-images.githubusercontent.com/96546108/223804341-20173eec-4c77-48b6-b0ae-7070a8d734e6.png)


#### To achieve this, we implemented the following tasks:
- A parent class (called **BaseModel**) to initialize, serialize, and deserialize future instances of our classes.
- A simple serialization / deserialization flow:
	`Instance <-> Dictionary <-> JSON String <-> File.`

- Create all the classes used for AirBnB (User, State, City, Place...) that inherit from the BaseModel class.
- Create my first** storage engine**: Storage in a json file.
- Create unit tests to validate our classes and the storage engine.

## Description of the proyect
In this project, we apply object-oriented programming, Python data translation, and command interpretation logic to deliver a local database that can be modified by commands.

## Prerequisites
The only requirement is to have python 3.6 or higher.
- [Python3.6+](http://https://www.python.org/downloads/ "Python3.4+")

## Installation
To have access to the console use the following command:

  `git clone https://github.com/jgnacio/holbertonschool-AirBnB_clone.git; cd holbertonschool-AirBnB_clone`

## Start the console
If you want to execute the console use:

`python3 console.py`

or

`./console.py`

## Use
### Available commands
| Command  |  Explanation |
| ------------ | ------------ |
| create | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.  |
| show  | Prints the string representation of an instance based on the class name and id.  |
| all  | Prints all string representation of all instances based or not on the class name.  |
| update  | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).  |



### Command input
|Command |Example |
| ---- | -------|
|create | ` create <class-name>`|
| show | `show <class-name> <id>` |
| all | `all <class-name> <id>` |
| update | `update <class-name> <id> <arg-name> <arg-value>` |


## Available classes
| Class name | Attributes |
| ----- | -----|
| BaseModel | `created_at`, `updated_at`, `id` |
| User |  `first_name`, `last_name`, `email`, `password`|
| State | `name`, `state_id`|
| City | `name` |
| Amenity | `name` |
| Place | `name`, `description`, `number_rooms`, `city_id`, `user_id`, `price_by_night`, `max_guest`, `number_bathrooms`, `longitude`, `latitude`, `amenity_ids`|
| Review | `place_id`,  `user_id`, `text`|

 every model inherits attributes from BaseModel




## Usage
The basic use of the console.
![Use example gif](https://user-images.githubusercontent.com/96546108/223802541-bf27387a-56d2-41e6-97f6-ecbf98e79c20.gif)


## All (command)
![all gif](https://user-images.githubusercontent.com/96546108/223802588-e57d26b9-abbe-4658-8783-03956f128307.gif)

## Destroy (command)
![destroy gif](https://user-images.githubusercontent.com/96546108/223802660-7b150c13-1c10-4c41-a0b3-1c1c66c284aa.gif)

## Update (command)
![update gif](https://user-images.githubusercontent.com/96546108/223802694-eb952ff4-82a1-4ff5-95e3-f1fef9196f44.gif)

## File storage
![recover-objs gif](https://user-images.githubusercontent.com/96546108/223802756-7dc88076-1adf-4d18-bc92-7c8a98cb890f.gif)

At startup it makes a reload of the file `"recover_objs.json"` that by deserializing the json file creates a dictionary to store all the instances with the following format: <class-name>.<id> as key, and the reference of the object itself as value.
  
Thanks so much for taking a look at the project! I hope you liked what you have seen. If you have any comments let me know.
