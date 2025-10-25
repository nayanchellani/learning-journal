import http from 'http';

const myServer = http.createServer((req , res)=>{
    console.log('Server is running');
    res.end('Hello from server');
        
});
myServer.listen(3000, ()=>{
    console.log('Server running on port 3000');
});