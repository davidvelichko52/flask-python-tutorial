from pymongo import MongoClient


host = 'localhost'
port = 27017
client = MongoClient()
db = client.test_database

op = db.dinosaur_collection

floorDivision = {
  "name": "Floor Division",
  "description": "Division that rounds down to the nearest integer. Also known as integer division.",
  "symbol": "//",
  "example": "3 // 2 == 1",
  "uses": "A common situation we might see this operator is when we need to calcuate a list index, which will need to be a whole number. For example, perhaps we are trying to find the middle index of a list, but there are an even number of elements. In this case, we could use floor division to select the leftmost element in the list by default."
}

add = {
  "name": "Add",
  "description": "Adds numbers together.",
  "symbol": "+",
  "example": "3 + 2 == 5",
  "uses": "A common situation we might see this operator is when we need to calcuate a list index, which will need to be a whole number. For example, perhaps we are trying to find the middle index of a list, but there are an even number of elements. In this case, we could use floor division to select the leftmost element in the list by default."
}

sub = {
  "name": "Sub",
  "description": "subtracts numbers together.",
  "symbol": "-",
  "example": "3 - 2 == 1",
  "uses": "A common situation we might see this operator is when we need to calcuate a list index, which will need to be a whole number. For example, perhaps we are trying to find the middle index of a list, but there are an even number of elements. In this case, we could use floor division to select the leftmost element in the list by default."
}

db.op.insert_many([floorDivision, add, sub])