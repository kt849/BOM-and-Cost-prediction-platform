import React from 'react';
import './App.css';
import './bootstrap.css';
import { Link, Route } from 'react-router-dom'

class history extends React.Component
{
    render()
    {
        return(
            <div className="App">
      <div className="loginbox1">
        <div className="row">
        <div className="col-md-4">
              <br></br>
              <div className="sidebar">
                <div class="link">
                <li className="nav-item">
                  <a className="nav-link" > <Link to = "/">Home</Link></a>
                </li>
                </div>
                <div class="link">
                <li className="nav-item">
                  <a className="nav-link" > <Link to = "/optimizer">Optimizer</Link></a>
                </li>
                </div>
                <div class="link">
                <li className="nav-item">
                  <a className="nav-link" > <Link to = "/his">Transaction History</Link></a>
                </li>
                </div>
                <div class="link">
                <li className="nav-item">
                  <a className="nav-link" > <Link to = "/supp">Change Suppliers</Link></a>
                </li>
                </div>
                <div class="link">
                <li className="nav-item">
                  <a className="nav-link" > <Link to = "/help">Help</Link></a>
                </li>
                </div>
              </div>   
            </div>
            <div className="col-md-6">
                <h1>HISTORY</h1>
            </div>
        </div>  
      </div>
    </div>
        )
    }
}


export default history;