var express = require("express");
var app1 = express();
var bodyParser = require("body-parser");



app1.use(bodyParser.urlencoded({extended:true}));
// app1.use(bodyParser.json());
app1.get("/",function(req,res){
	res.send("HElloo");
})

app1.post("/optimise",function (req,res){
     console.log(req);
});

app1.listen(3000,function(){
console.log("Server started");
});
