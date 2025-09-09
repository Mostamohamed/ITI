// 2. Create a Collection named "Staff". 
db.createCollection("Staff")


// 3. Insert one document into the "Staff" collection: {_id, name, age, gender, department}. 
db.Staff.insertOne({
  _id: "1",
  name: "Mostafa",
  age: 24,
  gender: "male",
  department: "sales"
})

db.Staff.find({})


// 4. Insert many documents into the "Staff" collection: 
//    Object: {_id, name, age: 20, gender: "male", department} 
//    Object: {_id, name, age: 25, gender: "female", managerName, department} 
//    Object: {_id, name, age: 15, gender, DOB} 

db.Staff.insertMany([{_id: "2", name: "aly" , age: 20, gender: "male", department: "hr"} ,
{_id: "3", name: "rowan", age: 25, gender: "female", managerName: "Mostafa", department: "sales"} ,
{_id: "4", name: "safaa", age: 15, gender: "female", DOB: "31/10/1973"}])

db.Staff.find({})


// 5. Query to find data from the "Staff" collection: 
//    1) Find all documents. 
db.Staff.find({})

//    2) Find documents where gender is "male". 
db.Staff.find({gender: "male"},{gender:1})

//    3) Find documents with age between 20 and 25. 
db.Staff.find({ age: { $gte: 20, $lte: 25 } },{});

//    4) Find documents where age is 25 and gender is "female".
db.Staff.find({ $and: [ { age: 25}, { gender: "female" } ] },{})

//    5) Find documents where age is 20 or gender is "female". 
db.Staff.find({ $or: [ { age: 20}, { gender: "female" } ] },{})




// 6. Update one document in the "Staff" collection where age is 15, set the name to "new student". 
db.Staff.find({})
db.Staff.updateOne({age: 15},{$set:{name: "new student"}})
db.Staff.find({})



// 7. Update many documents in the "Staff" collection, setting the department to "AI". 
db.Staff.updateMany( {}, { $set: { department: "AI" } })
db.Staff.find({})


// 8. Create a new collection called "test" and insert documents from Question 4. 
db.createCollection("test")

db.test.insertMany([{_id: "1", name: "aly" , age: 20, gender: "male", department: "hr"} ,
{_id: "2", name: "rowan", age: 25, gender: "female", managerName: "Mostafa", department: "sales"} ,
{_id: "3", name: "safaa", age: 15, gender: "female", DOB: "31/10/1973"}])
db.test.find({})



// 9. Try to delete one document from the "test" collection where age is 15. 
db.test.deleteOne({age: 15})
db.test.find({})


// 10. try to delete all male gender 
db.test.deleteMany({gender : "male"})
db.test.find({})


// 11. Try to delete all documents in the "test" collection. 
db.test.deleteMany({})

db.test.find({})




