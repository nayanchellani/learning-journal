import express from 'express'

const app = express()
app.use((req , res , next) =>{
    console.log("middlware running ");
})
app.get('/', (req, res) => {
  res.send('Hello World')
})

app.listen(3000)