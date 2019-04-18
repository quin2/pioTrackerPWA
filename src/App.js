import React, { Component } from 'react';
import {Container} from 'react-bootstrap';
import moment from 'moment';
import axios from 'axios';
import './App.css';

const url = 'http://34.220.171.44/locations.json';


// const reformatStops = function(stops) {
//   var info = 
  
//   return info;
// }

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      date: moment(),
      location: []
    }
  }

  componentWillMount() { 
    axios.get(url)
    .then(response => 
      this.setState({location: response.data}));
    
  }



  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h3>PioTracker 2.0</h3>
          <h4> <br/> {this.state.date.format("LTS")}</h4>
        </header>
        <body>
          <Container>
            <div className="arrivalTimes">
             {/* Just some hardcoded example times, hopefully we can mess around with the moment library and Pio Location  */}
              <p>
                The bus will arrive at {this.state.location[0]} 
              </p>

            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>The bus will arrive at {this.state.location[1]}</p>
            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>The bus will arrive at {this.state.location[2]} </p>
            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>The bus will arrive at {this.state.location[3]}</p>
            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>The bus will arrive at {this.state.location[4]}</p>
            </div>
          </Container>
        </body>
      </div>
    );
  }
}

export default App;
