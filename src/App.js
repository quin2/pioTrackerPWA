import React, { Component } from 'react';
import {Container, Row} from 'react-bootstrap';
import moment from 'moment';
import axios from 'axios';
import './App.css';

const url = 'http://174.129.44.93/api/v0/all';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      date: moment(),
      location: []
    }
  }


  componentWillMount() { 

   let addStops = (response) => { 
      var data = [];
      for(var i = 0; i < 6; i++) {
        data[i] = response.data[i].formatted;
      }
      this.setState({location: data});
      return data;
    }
   
    axios.get(url)
    .then(function (response) {
      addStops(response);
      
      
    })
    .catch(function (error) {
      console.log(error);
    });

    
}



  



  render() {
    return (
      <div className="App">
        <header className="App-header">
        <Container>
          <Row><h1>PioTracker 2.0 </h1></Row>
          <Row><em>Never miss the Pio again</em></Row>
          <Row>
            <h3> {this.state.date.format("LTS")}</h3>
          </Row>
        </Container>
        </header>
        <body>
          <Container>
            <div className="arrivalTimes">
             {/* Just some hardcoded example times, hopefully we can mess around with the moment library and Pio Location  */}
              <p>
                Bus 1 is currently at {this.state.location[0]} 
              </p>

            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>Bus 2 is currently at {this.state.location[1]}</p>
            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>Bus 3 is currently at {this.state.location[2]} </p>
            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>Bus 4 is currently at {this.state.location[3]}</p>
            </div>
          </Container>
          <Container>
            <div className="arrivalTimes">
              <p>Bus 5 is currently at {this.state.location[4]}</p>
            </div>
          </Container>

        </body>
      </div>
    );
  }
}

export default App;
