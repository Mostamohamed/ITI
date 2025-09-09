// 1. Find documents where the "tags" field exists. 
db.inventory.find({ tags: { $exists: true } });


// 2. Find documents where the "tags" field does not contain values "ssl" or "security." 
db.inventory.find({
  tags: { $nin: ["ssl", "security"] }
});


// 3. Find documents where the "qty" field is equal to 85. 
db.inventory.find({
  qty: { $eq: 85 }
});


// 4. Find documents where the "tags" array contains all of the values [ssl, security] using the `$all` operator. 
db.inventory.find({
  tags: { $all: ["ssl", "security"] }
});


// 5. Find documents where the "tags" array has a size of 3. 
db.inventory.find({
  tags: { $size: 3 }
});


// 6. Update the "item" field in the "paper" document, setting "size.uom" to "meter" and using the `$currentDate` operator. 
//       Also, use the upsert option and change filter condition item:”paper”. 
//       Use the `$setOnInsert` operator. 
//       Try `updateOne`, `updateMany`, and `replaceOne`.
db.inventory.find({item:"paper"},{})

db.inventory.updateOne({
    item:"paper"
}
,{
    $set:{"size.uom":"meter"},
    $currentDate:{lastModified : true},
    $setOnInsert:{createdtime: new Date()}
},
{
    upsert : true
})

db.inventory.find({item:"paper","size.uom":"meter"},{})


db.inventory.find({item:"paper"},{})

db.inventory.updateMany({
    item:"paper"
}
,{
    $set:{"size.uom":"meter"},
    $currentDate:{lastModified : true},
    $setOnInsert:{createdtime: new Date()}
},
{
    upsert : true
})

db.inventory.find({item:"paper","size.uom":"meter"},{})



db.inventory.find({item:"paper"},{})

db.inventory.replaceOne({
    item:"paper"
}
,{
    item:"paper",
    size : {uom : "meter"},
    lastModified : new Date()
},
{
    upsert : true
})

db.inventory.find({item:"paper"},{})




// 7. Insert a document with incorrect field names "neme" and "ege," then rename them to "name" and "age." 
db.inventory.insertOne({
  neme: "mostafa",
  ege: 24,
  city: "alexandria"
})

db.inventory.find({neme:"mostafa"},{})

db.inventory.updateOne(
  { 
      neme: { $exists: true }, 
      ege: { $exists: true } 
  },  
  { $rename: { "neme": "name", "ege": "age" }
  }          
)

db.inventory.find({name:"mostafa"},{})


// 8. Try to reset any document field using the `$unset` function. 
db.inventory.find({name:"mostafa"},{})

db.inventory.updateOne(
  { _id: ObjectId("68b191212914eebb0a44152e") },            
  { $unset: { city: "" } } 
)

db.inventory.find({name:"mostafa"},{})


// 9. Try update operators like `$inc`, `$min`, `$max`, and `$mul` to modify document fields. 
//        Important: Use a different field for each operation listed below. Insert Data If Not Existing 
//        Apply the following MongoDB update operators to the specified fields: 
//        Use $max on the field: salary 
//        Use $min on the field: overtime 
//        Use $inc on the field: age 
//        Use $mul on the fields: quantity and price
db.inventory.find({name:"aly"},{})


db.inventory.updateOne(
  { _id: 1000 }, 
  { 
    $setOnInsert: { 
      name: "aly",
      salary: 4000,
      overtime: 10,
      age: 25,
      quantity: 5,
      price: 100
    } 
  },
  { upsert: true }
)

db.inventory.find({_id:1000},{})


db.inventory.updateOne(
  { _id: 1000 },
  { 
    $max: { salary: 7000 },     
    $min: { overtime: 8 },      
    $inc: { age: 1 },           
    $mul: {           // Update operator          
      quantity: 2,              
      price: 1.1                
          }
  }
)

db.inventory.find({_id:1000},{})


// 10. Calculate the total revenue for product from sales collection documents within 
//    the date range '01-01-2020' to '01-01-2023' and then sort them in descending order by total revenue. 
//    Total Revenue=  Sum (Quantity * Price) 
db.sales.find({},{product:1 })

db.sales.aggregate([
  {
    $match: {
      date: {
        $gte: ISODate("2020-01-01"),
        $lte: ISODate("2023-01-01")
            }
            }
  },
  {
    $group: {
      _id: "$product",  
      totalRevenue: {
        $sum: {                                         //Aggregation operator
                $multiply: ["$quantity", "$price"]
              }   
                    }
            }
  },
  {
    $sort: { totalRevenue: -1 } 
  }
])


// 11. Calculate the average salary for employees for each department from the employee’s collection. 

db.employees.find({})

db.employees.aggregate([
  {
    $group: {
      _id: "$department",                  
      averageSalary: { $avg: "$salary" }   
            }
  }
])



// 12. Use likes Collection to calculate max and min likes per title 


db.likes.find({})

db.likes.aggregate([
  {
    $group: {
      _id: "$title",  
      MinLikes: { $min: "$likes" },                
      MaxLikes: { $max: "$likes" }
            }
  }
])
