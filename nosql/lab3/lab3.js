// 1. Provide the MongoDB code for enforcing JSON schema validation when creating a collection named "employees" 
//    with required fields "name," "age" (min. 18), and "department" (limited to ["HR," "Engineering," "Finance"]). 

db.createCollection("employeesss", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "employee required input",
            required: ["name", "age", "department"],
            properties: {
                name: {
                    bsonType: "string",
                    description: "must be a string and is required"
                },
                age: {
                    bsonType: "int",
                    minimum: 18,
                    description: "must be an integer >= 18 and is required"
                },
                department: {
                    enum: ["HR", "Engineering", "Finance"],    //enumeration
                    description: "must be one of the predefined departments and is required"
                }
            }
        }
    },
    validationLevel: "strict",
    validationAction: "error"
})


// test  success
db.employeesss.insertOne({
    name: "Ali",
    age: 25,
    department: "HR"
})

// test invalid
db.employeesss.insertOne({
    name: "Sara",
    age: 16,
    department: "HRw"
})

db.employeesss.insertOne({
    name: "aly",
    age: 15,
    department: "HR"
})


db.employeess.insertOne({
    name: 234,
    age: 19,
    department: "HR"
})

db.employeesss.find({})
db.employeesss.deleteMany({age : 16})
//  2. Create new Database named Demo 
//     And Collections named trainningCenter1, trainningCenter2  
//     Insert documents into trainningCenter1 collection contains (Use Variable named data as Array) 
//                 _id , name as firstName lastName , age , address as array , status 
//     Using insert ONE from data Variable 
//     Using Same Variable (data) with same data and insert MANY into trainningCenter2 collection


use Demo


db.createCollection("trainningCenter1")
db.createCollection("trainningCenter2")


var data = [
    {
        _id: 1,
        name: { firstName: "mostafa", lastName: "mohamed" },
        age: 24,
        address: ["alexandria", "Egypt"],
        status: "Active"
    },
    {
        _id: 2,
        name: { firstName: "aly", lastName: "mohamed" },
        age: 28,
        address: ["Giza", "Egypt"],
        status: "Inactive"
    },
    {
        _id: 3,
        name: { firstName: "rowan", lastName: "mohamed" },
        age: 26,
        address: ["Alexandria", "Egypt"],
        status: "Active"
    }
]



db.trainningCenter1.insertOne(data)   // inserted this as one document
db.trainningCenter1.find()
db.trainningCenter1.deleteOne({ _id: ObjectId("68b2d69f5cf6a5c967441539") })

db.trainningCenter1.insertOne(data[0])   // just inserted the first one document
db.trainningCenter1.find()


db.trainningCenter2.insertMany(data)     // all document
db.trainningCenter2.find()


// 3. Use find. explain function (find by age field) and mention scanning type 

db.trainningCenter2.find({ age: 28 }).explain()   // scanning type : collaction scan



// 4. Create index on created collection named it “IX_age” on age field  

db.trainningCenter2.createIndex(
    { age: 1 },
    { name: "IX_age" }
)

db.trainningCenter2.getIndexes()


// 5. Use find. explain view winning plan for index created (find by age field) and mention scanning type 

db.trainningCenter2.find({ age: 28 }).explain()   // scanning type : index scan


// 6. Create index on created collection named it “compound” on firstNsme and lastName 
//         a. Try find().explain before create index and mention scanning type 
//         b. Try find().explain after create index and mention scanning type 

db.trainningCenter2.find({ "name.firstName": "aly", "name.lastName": "mohamed" }).explain()  // collaction scan

db.trainningCenter2.createIndex(
    { "name.firstName": 1, "name.lastName": 1 },
    { name: "compound" }
)

db.trainningCenter2.find({ "name.firstName": "aly", "name.lastName": "mohamed" }).explain()  // index scan


// 7. Drop Demo Database 

use Demo
db.dropDatabase()



show dbs






