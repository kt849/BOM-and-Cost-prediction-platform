const readXlsxFile = require('read-excel-file/node');

var express = require("express");
var app = express();
var bodyParser = require("body-parser");

app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());
app.get("/",function(req,res){
	res.send("Heellooo");
});

app.post("/test",function(req,res){
	console.log(req.body);
	res.json({"message":"Hello"});
})

app.post("/optimise",optimise);
function optimise(req,res){
	var spawn = require("child_process").spawn;
	// console.log(req.query.par);
	// a = "Screen"
	console.log(req.body);
	var process = spawn('python3',["./Script1.py", 
                            req.body.GPU,req.body.GPU2,req.body.CPU,req.body.CPU2,req.body.SSD,req.body.SSD2,req.body.RAM,req.body.RAM2,req.body.Screen,req.body.Screen2,req.body.HDD,req.body.HDD2]); 
	process.stdout.on('data', function(data) { 
		console.log("I'm here")
		console.log(data)
		const fs = require('fs')
		let jsonData = JSON.parse(fs.readFileSync('opti.json', 'utf-8'))
		console.log(jsonData)
		res.json(jsonData);
		// console.log(JSON.parse(data))
        // res.json(JSON.stringify(JSON.parse(data))); 
    } ) 
    process.stderr.on('data', function(data) { 
          console.log(data.toString());
          console.log("I'm Back ");
      });
}

app.listen(3000,function(){
	console.log("Server started");
});
 