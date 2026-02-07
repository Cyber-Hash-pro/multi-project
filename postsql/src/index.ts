import pg from 'pg' 
import dotenv from 'dotenv'
import express from 'express'

dotenv.config()

const pgclient = new pg.Client({connectionString: process.env.DATABASE_URL})
const app = express()
app.use(express.json())
const db = async () => {
pgclient.connect()
  .then(() => console.log('Connected to PostgreSQL database'))
  .catch((err) => console.error('Error connecting to PostgreSQL database:', err))
}

db()



app.get('/', (req, res) => {
  res.send('Hello, World!')
})
// sql injection example
app.post('/addusers', async (req, res) => {
const {username, email,password} = req.body
try{
    const insertQuery = `INSERT INTO users (username,email,password) VALUES ('${username}', '${email}', '${password}')` // here sql injection happens if user send ab noramla data like 
    console.log(insertQuery) 
// noraml query example : INSERT INTO users (username,email,password) VALUES ('cy1wber', 'cyber1@wgmail.com', '123456')
// sql injection example : INSERT INTO users (username,email,password) VALUES ('cy1wber', 'cyber1@wgmail.com', ''); DELETE * FROM users')
// this happend user password field me   "password": "'); DELETE * FROM users" or query agar db chali to db 
// user table ke sare data delete ho jayega hae hota sql injection attack user pan wo kuch bhi send kar sakta hae 
//   const response = await pgclient.query(insertQuery) 
const inserQuerynotsqlInjection = 'INSERT INTO users (username,email,password) VALUES ($1, $2, $3)' // this is parameterized query and it is safe from sql injection attack
console.log(inserQuerynotsqlInjection)
const response = await pgclient.query(inserQuerynotsqlInjection, [username, email, password]) // this is parameterized query and it is safe from sql injection attack
// ese kya inserQuerynotsqlInjection as reach to dabase then and value matlab postsql dabase ek query and value and done alga alg hote hae first me query ke ssate value jara hi thi ab value and query alga alg hote hae to sql injection attack nhi hota hae
// ese query and value alga alg hote hae to sql injection attack nhi hota hae kyuki user input value ke sath query nahi jura hota hae to user input me kuch bhi send kar sakta hae but wo query ke sath nahi jura hota hae to sql injection attack nhi hota hae

    res.send('User added successfully')
} catch (err) {   
    console.error('Error adding user:', err)
    res.send('Error adding user')
 }
})
























app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000')
})