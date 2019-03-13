import React, { Component } from 'react';
import {Container} from 'react-bootstrap';
import moment from 'moment';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      date: moment(),
      location: ['Templeton', 'Shattuck Hall', 'Fred Meyer']
    }
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h3>PioTracker 2.0</h3>
        </header>
        <body>
          <Container>
            <div className="arrivalTimes">
             {/* Just some hardcoded example times, hopefully we can mess around with the moment library and Pio Location  */}
              <p>The bus will arrive at {this.state.location[2]} {this.state.date.subtract(10, "minutes").toNow() }</p>
            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>The bus will arrive at {this.state.location[0]} {this.state.date.subtract(10, "minutes").toNow() }</p>
            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>The bus will arrive at {this.state.location[1]} {this.state.date.add(15, "minutes").toNow() }</p>
            </div>
          </Container>
        </body>
      </div>
    );
  }
}

export default App;
