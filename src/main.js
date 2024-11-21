import './app.css'
import App from './App.svelte'
import  io  from 'socket.io-client';


const app = new App({
  target: document.getElementById('app'),
})

// Initialize Socket.IO client
const socket = io('http://localhost:5173');

socket.on('connect', () => {
    console.log('Connected to WebSocket');
});

socket.on('notification', (data) => {
    console.log('Received notification:', data);
});

export default app
