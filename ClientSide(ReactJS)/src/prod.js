import React from 'react';
import './App.css';
import './bootstrap.css';
import { Link, Route } from 'react-router-dom';
import axios from 'axios';

class prod extends React.Component
{
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
                        <h1>Product Details</h1>
                    </div>
                    <div className="col-md-4">

                    </div>
                </div>
                <br></br>
                <br></br>
                <div className="row">
                    <div className="col-md-4">
                    <p class="text"> Choose a product from the given list:</p>
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
                        <select name="suppliers">
                            <option value="Samsung">HDD</option>
                            <option value="Western Digital">SSD</option>
                            <option value="Transcend">Display</option>
                            <option value="Nvidia">Graphic Card</option>
                        </select>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <button type="button" className="btn btn-warning">Go</button>
                    </div>
                    <div className="col-lg-9">
                    <table class="TAB">
                        <tr>
                            <th>Supplier</th>
                            <th>Cost</th> 
                            <th>Rating</th>
                        </tr>
                        <br></br>
                        <tr>
                            <td>Samsung</td>
                            <td>$10</td>
                            <td>8</td>
                        </tr>
                        <br></br>
                        <tr>
                            <td>Western Digital</td>
                            <td>$20</td>
                            <td>9</td>
                        </tr>
                        <br></br>
                        <tr>
                            <td>LG</td>
                            <td>$15</td>
                            <td>8</td>
                        </tr>
                    </table>
                    </div>
                </div>
            </div>
        </div>
        )
    }
}


export default prod;