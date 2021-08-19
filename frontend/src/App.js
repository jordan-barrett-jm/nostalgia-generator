import React from 'react';
import axios from 'axios';
import 'semantic-ui-css/semantic.min.css';
import { Message, Grid, Table, Form, Dimmer, Loader, Container, Header } from 'semantic-ui-react';

class App extends React.Component {
    constructor (props){
        super(props)
        this.state = {
            category: '',
            link: ''
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event){
        this.setState(
            {
                category: event.target.value
            }
        );
    }

    async handleSubmit(event){
        const API_ENDPOINT = "http://127.0.0.1:8000/link/";
        event.preventDefault();
        console.log(this.state.category);
        axios.post(API_ENDPOINT, {"category": this.state.category}).then(
            res => {
                //console.log(res.data);
                this.setState({
                    'link': res.data.link
                });
                console.log(res.data.link);
            }
        )
    }

    render(){
        return (
            <Container style={{ margin: 20 }} textAlign='center'>
                <Form onSubmit={this.handleSubmit}> 
                    <Form.Input onChange={this.handleChange} value={this.state.category}/>
                    <Form.Button>Generate Nostalgia</Form.Button>
                </Form>
                {this.state.link ?
                    <a href={this.state.link}>Video Link</a>
                : ""
                }
            </Container>
        )
    }
    
}

export default App;
