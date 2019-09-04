import React from 'react';
import './App.css';
import './bootstrap.css';
import { Link, Route } from 'react-router-dom';
import axios from 'axios';

export  class supplier extends React.Component
{
    constructor(props)
    {
        super(props);
        this.state = {
            value:''
        };
    }

    
    handleChange = event => {
        this.setState(
            {
                value:event.target.value
            }
        )
    }

    btnClick = event => {
            
            console.log(this.state.value);
            var xhr = new XMLHttpRequest();
            var url = "http://10.6.11.196:3000/test";
            xhr.open("POST", url,true);
            xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    console.log(xhr.responseText)
                    var json = JSON.parse(xhr.responseText);
                     console.log(json.message);
                }
            };
            var data = {supplier: this.state.value};
            console.log(data);
            xhr.send(JSON.stringify(data));       
    }



    
    
    render()
    {
        var message='You selected '+this.state.selectValue;
       
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
                            <h1>Supplier Details</h1>
                        </div>
                        <div className="col-md-4">

                        </div>
                    </div>
                    <br></br>
                    <br></br>
                    <br></br>
                    <div className="row">
                        <div className="col-md-4">
                        <p class="text"> Choose a supplier from the given list:</p>
                        </div>
                        <div className="col-md-4">
                            
                        </div>
                        <div className="col-md-4">

                        </div>
                    </div>
                    <br></br>
                    <div className="row">
                        <div className="col-lg-3">
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <select class="suppliers" value={this.state.selectValue}   onChange={this.handleChange} >
                                <option value="Samsung"></option>
                                <option value="Western Digital">Western Digital</option>
                                <option value="Transcend">Transcend</option>
                                <option value="Nvidia">Nvidia</option>
                            </select>
                            
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <button type="button"  className="btn btn-warning" onClick={this.btnClick}>Go</button>
                        </div>
                        <div className="col-lg-9">
                        
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}






export default supplier;