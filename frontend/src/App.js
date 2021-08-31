import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home';
import Login from './Login';
import NotFound from './NotFound';
import Dashboard from './Dashboard';

function App() {
  return (
    <div className="App">
      <Router>
        <div className="contents">
          <Switch>
            <Route exact path="/">
              <Dashboard />
            </Route>
            <Route exact path="/hello">
              <Home />
            </Route>
            <Route exact path="/login">
              <Login />
            </Route>
            <Route path="*">
              <NotFound />
            </Route>
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
