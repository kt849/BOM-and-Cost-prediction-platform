import React from 'react';
//import logo from './logo.svg';
import './App.css';
import './bootstrap.css';
import { Link, Route } from 'react-router-dom'





function App() {
  return (
    <div className="App">
      <div className="loginbox1">
        <br></br>
        <br></br>
        <h1>BOM & Cost Prediction</h1>
        <br></br>
       <div className="nav">

       </div>
   <div class="content">
       <div class="card">
              <span class = "opti" ></span>
              <Link to = "/optimizer"> <p class="title">Optimizer</p></Link>
             <p class="text">Get optimized products</p>
       </div>
       <div class="card">
       <span class = "supp" ></span>
            <Link to = "/supp"> <p class="title">Know Your Supplier</p></Link>             
             <p class="text">Check all the proucts offered by a supplier in one place.</p>
       </div>
       <div class="card">
       <span class = "prod" ></span>
       <Link to = "/prod"> <p class="title">Know Your Product</p></Link>
             <p class="text">Get information about a particular product from different manufacturers</p>
       </div> 
    </div>
 </div>

      </div>        
    
  );
}

export default App;


/*
<ul>
          <li><a class="active" href="#home">Home</a></li>
          <li><a href="#news">News</a></li>
          <li><a href="#contact">Contact</a></li>
          <li><a href="#about">About</a></li>
        </ul>

 */


//<a><div class="text"><Link to ="/optimizer"></Link>Optimizer</div></a>
/*

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
                  <a className="nav-link" > <Link to = "/optimizer">Transaction History</Link></a>
                </li>
                </div>
                <div class="link">
                <li className="nav-item">
                  <a className="nav-link" > <Link to = "/optimizer">Change  Suppliers</Link></a>
                </li>
                </div>
                <div class="link">
                <li className="nav-item">
                  <a className="nav-link" > <Link to = "/optimizer">Help</Link></a>
                </li>
                </div>
              </div>   
            </div>
        </div>  
      </div> 
*/