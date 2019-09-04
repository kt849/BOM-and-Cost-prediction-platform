import React from 'react';
import './App.css';
import './bootstrap.css';
import { Link, Route } from 'react-router-dom';

class optimizer extends React.Component
{
    constructor(props)
    {

        super(props);
        this.state = {
            HDD:"",
            SSD:"",
            RAM:"",
            CPU:"",
            GPU:"",
            Screen:"",
            HDD2:"",
            SSD2:"",
            RAM2:"",
            CPU2:"",
            GPU2:"",
            Screen2:"",
            Config:[['Component','Price','Company','Rating']]
        };
    }
        
    handleChange = event => {
        if(event.target.id == "HDD")
        {
            this.setState({
                    HDD : event.target.value
                }
            )
        }
        else if(event.target.id == "SSD")
        {
            this.setState({
                    SSD : event.target.value}
            )
        }
        else if(event.target.id == "RAM")
        {
            this.setState({
                    RAM : event.target.value}
            )
        }else if(event.target.id == "CPU")
        {
            this.setState({
                    CPU : event.target.value}
            )
        }else if(event.target.id == "GPU")
        {
            this.setState({
                    GPU : event.target.value}
            )
        }else if(event.target.id == "Screen")
        {
            this.setState({
                    Screen : event.target.value}
            )
        }else if(event.target.id == "HDD2")
        {
            this.setState({
                    HDD2 : event.target.value}
            )
        }else if(event.target.id == "SSD2")
        {
            this.setState({
                    SSD2 : event.target.value}
            )
        }else if(event.target.id == "RAM2")
        {
            this.setState({
                    RAM2 : event.target.value}
            )
        }else if(event.target.id == "CPU2")
        {
            this.setState({
                    CPU2 : event.target.value}
            )
        }else if(event.target.id == "GPU2")
        {
            this.setState({
                    GPU2 : event.target.value}
            )
        }else if(event.target.id == "Screen2")
        {
            this.setState({
                    Screen2 : event.target.value}
            )
        }
    }

    changeState = tmp=> {
        this.setState({
            Config: tmp
        })
    }

    btnClick = event => {
        console.log(this.state);
        var tmp = [];
        var t0 = [];
        t0.push("Component")
        t0.push("Company")
        t0.push("Price")
        t0.push("Rating")
        tmp.push(t0);
        var xhr = new XMLHttpRequest();
            var url = "http://10.6.11.196:3000/optimise";
            xhr.open("POST", url,true);
            xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhr.onreadystatechange =  ()=> {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    console.log(xhr.responseText)
                    var json = JSON.parse(xhr.responseText);
                    
                    var t1 = []
                    t1.push(1)
                    t1.push(json["graphics"][0][1])
                    t1.push(json["graphics"][0][2])
                    t1.push(json["graphics"][0][3])

                    var t2 = []
                    t2.push(2)
                    t2.push(json["ssd"][0][1])
                    t2.push(json["ssd"][0][2])
                    t2.push(json["ssd"][0][3])
                    
                    var t3 = []
                    t3.push(3)
                    t3.push(json["ram"][0][1])
                    t3.push(json["ram"][0][2])
                    t3.push(json["ram"][0][3])
                    
                    var t4 = []
                    t4.push(4)
                    t4.push(json["screen"][0][1])
                    t4.push(json["screen"][0][2])
                    t4.push(json["screen"][0][3])
                    
                    var t5 = []
                    t5.push(5)
                    t5.push(json["hdd"][0][1])
                    t5.push(json["hdd"][0][2])
                    t5.push(json["hdd"][0][3])
                    
                    var t6 = []
                    t6.push(6)
                    t6.push(json["cpu"][0][1])
                    t6.push(json["cpu"][0][2])
                    t6.push(json["cpu"][0][3])
                    
                  
                    tmp.push(t1)
                    tmp.push(t2)
                    tmp.push(t3)
                    tmp.push(t4)
                    tmp.push(t5)
                    tmp.push(t6)
                    this.setState({
                        Config: tmp
                    })
                    
                }
            };
            var data = {HDD:this.state.HDD,SSD:this.state.SSD,RAM:this.state.RAM,CPU:this.state.CPU,GPU:this.state.GPU,Screen:this.state.Screen,
                HDD2:this.state.HDD2,SSD2:this.state.SSD2,RAM2:this.state.RAM2,CPU2:this.state.CPU2,
                GPU2:this.state.GPU2,Screen2:this.state.Screen2};
            console.log(data);
            xhr.send(JSON.stringify(data));
    }
    
    render()
    {
        return(
            <div className="App">
                <div className="loginbox1">
                    <br></br>
                    <br></br>
                    <div className="row">
                        <div className="col-md-4">
                        <span class = "homme" ></span>   
                        <Link to = "/" class="LinkTest"> <p class="title">Home</p></Link>
                        </div>
                        <div className="col-md-4">
                            <h1>Optimizer</h1>
                        </div>
                        <div className="col-md-4">

                        </div>
                    </div>
                    <br></br>
                    <br></br>
                    <br></br>
                    <div className="row">
                        <div className="col-md-4">
                        <p class="text"> Choose from the given list:</p>
                        </div>
                        <div className="col-md-4">
                            
                        </div>
                        <div className="col-md-4">
                        </div>
                    </div>
                    <div className="row">
                        <div className="col-lg-3">
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <p class="title">HDD</p>
                            <select class="HDD" id= "HDD" value={this.state.selectValue}   onChange={this.handleChange }>
                                <option value="xsd"></option>
                                <option value="0">512 GB</option>
                                <option value="1">1 TB</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title" >SSD</p>
                            <select name="SSD" id = "SSD" value={this.state.selectValue}   onChange={this.handleChange}>
                                <option value="xsd"></option>
                                <option value="0">512 GB</option>
                                <option value="1">1 TB</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">RAM</p>
                            <select name="RAM" id = "RAM" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="0">8 GB</option>
                                <option value="1">16 GB</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">CPU</p>
                            <select name="CPU" id="CPU" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="0">i5</option>
                                <option value="1">i7</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">GPU</p>
                            <select name="GPU" id="GPU" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="0">GTX 2060</option>
                                <option value="1">GTX 2080Ti</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">Screen Size</p>
                            <select name="Screen" id="Screen" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="0">13 inch</option>
                                <option value="1">15 inch</option>
                            </select>
                            <br></br>
                            <br></br>
                        </div>
                        <div className="col-lg-1">
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <p class="title">Speed (rpm) </p>
                            <select name="Quality" id = "HDD2" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="1">1800 rpm</option>
                                <option value="2">3600 rpm</option>
                                <option value="3">5400 rpm</option>
                                <option value="4">7200 rpm</option>
                                <option value="5">9000 rpm</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">SSD Type</p>
                            <select name="Quality" id="SSD2" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="1">2.5" SSD</option>
                                <option value="2">mSATA </option>
                                <option value="3">M.2</option>
                                <option value="4">PCI-E</option>
                                <option value="5">PCI-F</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">RAM Speed</p>
                            <select name="Quality" id="RAM2" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="1">1800 Mhz</option>
                                <option value="2">2133 Mhz</option>
                                <option value="3">2400 Mhz</option>
                                <option value="4">2800 Mhz</option>
                                <option value="5">3000 Mhz</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">CPU Speed</p>
                            <select name="Quality" id="CPU2" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="1">1.6 Ghz</option>
                                <option value="2">2.0 Ghz</option>
                                <option value="3">3.0 Ghz</option>
                                <option value="4">4.0 Ghz</option>
                                <option value="5">5.0 Ghz</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">GPU Memory</p>
                            <select name="Quality" id="GPU2" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="1">2 GB DDR3</option>
                                <option value="2">4 GB DDR3</option>
                                <option value="3">2 GB GDDR5</option>
                                <option value="4">4 GB GDDR5</option>
                                <option value="5">6 GB GDDR5</option>
                            </select>
                            <br></br>
                            <br></br>
                            <p class="title">Resolution</p>
                            <select name="Quality" id="Screen2" value={this.state.selectValue}   onChange={this.handleChange}>
                            <option value="xsd"></option>
                                <option value="1">1280 x 720</option>
                                <option value="2">1600 x 900</option>
                                <option value="3">1920 x 1080</option>
                                <option value="4">2960 x 1440</option>
                                <option value="5">3840 x 2160</option>
                            </select>
                            <br></br>
                            <br></br>
                        </div>
                        
                        <div className="col-lg-8">                                           
                        <div>
                {
                  this.state.Config.map(function(item, i){
                        return(
                            <div>
                                <div class="row">
                                    <div class = "col-md-3">
                                        {item[0]}
                                    </div>
                                    <div class="col-md-3">
                                        {item[1]}
                                    </div>
                                    <div class="col-md-3">
                                        {item[2]}
                                    </div>
                                    <div class="col-md-3">
                                        {item[3]}
                                    </div>
                                </div>
                                <br></br>
                            </div>   
                        )
                    })
                }
            </div>
                        
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-5">
                        <button type="button" className="btn btn-warning" onClick={this.btnClick}>Go</button>
                        </div>
                        <div class="col-md-4">

                        </div>
                        <div class="col-md-3">

                        </div>

                    </div>
                </div>
            </div>
        )
    }
}



/*
<table>
                            <thead>
                                <th>Part</th> 
                                <th>Price</th>
                                <th>Company</th>
                            </thead>
                            <tbody>
                                {this.state.Config.map((data, i) => {
                                return (
                                    <tr key={i}>
                                    <td>{data.Part}</td> 
                                    <td>{data.Price}</td>
                                    <td>{data.Company}</td> 
                                    </tr>
                                )
                                })}
                            </tbody>
                        </table>
*/
export default optimizer;