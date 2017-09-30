//import React, { Component } from 'react';
//import { BrowserRouter, Route, Switch } from 'react-router';
//import Router, { Route } from 'react-browser-router';

// import { Link } from 'react-router-dom';
import './App.css';
import Data from './components/Data';
import Header from './components/Header';
import Home from './components/Home';

var React = require('react');
//var Data = require('./components/Data');
var ReactRouter = require('react-router-dom');
var Router = ReactRouter.BrowserRouter;
var Route = ReactRouter.Route;


class App extends React.Component {
    constructor() {
        super();
        this.state = {
            data: []
        };
    }

    componentWillMount() {
        this.setState({
            data: [{
                title: 'Conclusion',
                image: 'graph',
                description: 'results'
            }]
        });
    }
    render() {
        return (
            <div>
                <Header />
                <Router >
                    <div className="container" >
                        <Route path='/' component={Home} />
                        <Route path="/data" component={Data} />

                    </div >
                </Router>
            </div>
        );
    }
}

export default App;