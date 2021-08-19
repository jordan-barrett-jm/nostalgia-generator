import React from 'react';
import axios from 'axios';
import 'semantic-ui-css/semantic.min.css';
import { Message, Grid, Table, Form, Dimmer, Loader, Container, Header } from 'semantic-ui-react';

class App extends React.Component {
    constructor (props){
        super(props)
        this.state = {
            category: '1990s',
            link: ''
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event, result){
        console.log(result.value)
        this.setState(
            {
                category: result.value
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

    getEmbedURL(url){
        const video_id = url.split('v=')[1];
        const embed_url = `https://www.youtube.com/embed/${video_id}`;
        return embed_url;
    }

    render(){
        const options = [
            {
                key: '2000s',
                text: "00's kid",
                value: "2000s"
            },
            {
                key: '1990s',
                text: "90's kid",
                value: "1990s"
            },
            {
                key: '1980s',
                text: "80's kid",
                value: "1980s"
            }
        ]
        return (
            <Container style={{ margin: 20 }} textAlign='center'>
                <Header size="huge">I'm a...</Header>
                <Form onSubmit={this.handleSubmit}> 
                    <Form.Dropdown style={{fontSize: '20px'}} onChange={this.handleChange} options={options} defaultValue="1990s"/>
                    <Form.Button size="huge" color="blue">Generate Nostalgia</Form.Button>
                </Form>
                {this.state.link ?
                    <Container style={{ margin: 20 }}>
                        <iframe width="560" height="315" src={this.getEmbedURL(this.state.link)} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </Container>
                : ""
                }
            </Container>
        )
    }
    
}

export default App;
