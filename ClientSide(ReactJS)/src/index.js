import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Optimizer from './Optimizer';
import prod from './prod';
import Supp from './supplier';
import his from './history';
import * as serviceWorker from './serviceWorker';
import { BrowserRouter } from 'react-router-dom'
import { Link, Route } from 'react-router-dom'

const route = (
    <BrowserRouter>
    <div>
        <Route exact path = "/" component={App}/>
        <Route path = "/optimizer" component={Optimizer}/>
        <Route path = "/prod" component={prod}/>
        <Route path = "/his" component={his}/>
        <Route path = "/supp" component={Supp}/>
    </div>
    </BrowserRouter>
)


/*
 <Route path = "/dash" component={dash}/>
        <Route path = "/admin" component={admin}/>
        <Route path = "/profile" component={profile}/>
        <Route path = "/league" component={league}/>
        <Route path = "/lead" component={lead}/>
 */

ReactDOM.render(route, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
