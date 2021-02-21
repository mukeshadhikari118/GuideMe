import React from 'react';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Switch,Route } from 'react-router-dom';
import Navbars from './components/Navbars';

import Footer from './components/pages/Footer/Footer';






function App() {
  return (
    <Router>
      <Navbars />
      <Switch>
        <Route path='/' exact component = {Home}/>
      </Switch>
      <Footer />
    </Router>

  );
}

export default App;
