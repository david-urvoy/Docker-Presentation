import React, { Component } from 'react';
import logo from './logo.svg';
import FilterableProductTable from './components/product/FilterableProductTable'

import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />

          <FilterableProductTable/>
        </header>
      </div>
    );
  }
}

export default App;
